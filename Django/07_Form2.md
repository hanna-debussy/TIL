# Django Form Class

## create.html + update.html

생각해보면 그렇잖아 create나 update나 모양은 form 그대로인데 왜 우리는 페이지를 따로 만들어야 하는 거지? 
&rarr; 합치면 된다! (wow)

별 건 없고 그냥... 하나의 html을 공유하면 됨... 끝이야 어차피 update는 `instance=somethin`이기 때문에 저절로 갖고 들어가기 때문



## GET, POST

장고 모듈에는 이런 것이 있다

`from django.views.decorators.http`

얘는 요청 방법에 따라 엑세스를 제한할 수 있다. 이 데코레이터 안에는 네 가지가 있는데

1. `require_http_methods`: 특정 요청 방법만 허용하도록 하는 데코레이터
2. `require_POST`: POST 메소드만 허용하도록 하는 데코레이터
3. `require_safe`: GET 메소드만 허용



그렇다면 생각을 해보자... 각각은 어디서 쓰여야 할까?

일단 4. `require_safe`는 index와 detail에서 쓰여야 하겠지
그리고 우리가 create와 update에선 POST와 GET 모두 처리할 수 있도록 if문을 처리해뒀기 때문에 `require_http_methods(["GET", "POST"])` 라고 쓸 수 있을 것이다.
그리고 delete는 은밀하게 이루어져야 하니까 `@require_POST`가 마땅할 거다.

그러므로 우리는 이렇게 심어줘야겠지

```python
from django.views.decorators.http import require_POST, require_http_methods, require_safe
```

쓰임은 이렇게

```python
@require_safe
def index(request):
	blarblar    
    
@require_http_methods(["GET", "POST"])
def create(request):
	blarblar
    
@require_POST
def delete(request, pk):
	blarblar
```

적용할 함수 위에 `@`와 함께 적어주면 적용된다



그리고 delete에 POST만 오게 해줬으니까 delete 버튼도 그렇게 만들어줘야 한다.

```html
{% extends 'base.html' %}

{% block content %}

어쩌고저쩌고 

<div>
  <a href="{% url 'classroom:update' student.pk %}">
    <button>EDIT</button>
  </a>
</div>

<div>
  <form action="{% url 'classroom:delete' student.pk %}" method="POST">
    {% csrf_token %}
    <button>DELETE</button>
  </form>
</div>
{% endblock content %}  
```

위의 EDIT은 그냥 a>button 으로 처리해줬지만

밑의 DELETE는 `method="POST"`를 적용하기 위해서 form 태그로 소중히 감싸주었다.



## BOOTSTRAP

잠깐 말했지만 우리는 부트스트랩을 쓸 수 있다.



### 세팅

```bash
$ pip install django-bootstrap-v5
```

```python
# settings.py
INSTALLED_APPS = {
    'bootstrap5',
}
```



### base.html

```html
{% load bootstrap5 %}

<!DOCTYPE html>
<html lang="en">
<head>  
  {% bootstrap_css %}
  
  <title>Document</title>
</head>
<body>
  
  {% bootstrap_javascript %}
</body>
</html>
```

* 일단 `{% load bootstrap5 %}`는 ! 보다 더 위, 가장 첫 줄에 적어야 한다.
* css와 js는 저렇게 불러올 수 있지만 저 명령어가 사실 bootstrap의 가장 최신 버전을 들고 온다. 근데 그게 가끔 바로바로 적용이 안 되거나... 그래서 그냥 공홈에서 cdn을 직접 들고오는 게 낫다.



```html
{% extends "base.html" %}
{% load bootstrap5 %}

{% block content %}

<form method="POST">
  {% csrf_token %}
  
  {% bootstrap_form form %}
  <button class="btn btn-primary">GO</button>
</form>

{% endblock content %}
```

* 하지만? `{% load bootstrap5 %}` 위에 `{% extends "base.html" %}`가 있다... extends는 항상항상항상 최상단에 있어야 한다
* bootstrap은 직접 form을 제공하고 있기 때문에 `{{ form.as_p }}` 대신에  `{% bootstrap_form form %}`이라고 적어주면 된다.

* 그리고 당연히 bootstrap이 적용되고 있기 때문에 꼭 저런 형식이 아니어도 class로 입맛대로 바꿀 수 있다묭