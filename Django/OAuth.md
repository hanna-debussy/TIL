# OAuth

일단 pjt09에서...

```bash
$ python manage.py loaddata movies.json
```

해주기



## django allauth

```bash
$ pip install django-allauth
```

https://django-allauth.readthedocs.io/en/latest/installation.html 에서 하라는 대로 한 후에 `python manage.py migrate` 해야 한다



## OAuth2

### google cloud platform

1. 콘솔로 들어와서
2. 새 프로젝트 만들기
3. OAuth에서 app 만들기
4. 사용자인증정보에서 OAuth 클라이언트 ID 만들기 < 해주기
   1. 웹 어플리케이션
   2. 승인된 리디렉션 URI에 https://django-allauth.readthedocs.io/en/latest/providers.html 를 참고해서 *Finally fill in `http://127.0.0.1:8000/accounts/google/login/callback/` in the “Authorized redirect URI” field.* 에 따라 저 주소를 적어준다
5. 그렇게 나온 클라이언트 ID와 클라이언트 보안 비밀번호를 우리 admin의 소셜 어플리케이션에 추가를 해준다



## 로그인 구멍 뚫어주기

https://django-allauth.readthedocs.io/en/latest/templates.html

```html
{% load socialaccount %}

<div>
    <a href="{% provider_login_url 'google' next='로그인후에돌아갈곳의url을 다 써주면 됨 /community/ 이렇게' %}">google login</a>
</div>
```



로그인 바로 넘어가기

```python
# settings.py
SOCIALACCOUNT_LOGIN_ON_GET = True
```



## Paginator

https://docs.djangoproject.com/en/4.0/topics/pagination/

```python
# views.py
from movies.models import Movie

@require_safe
def index(request):
    movies = Movie.objects.all()
    paginator = paginator(movies, 10)   # 10개씩 자르겠다 이말이야

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "movies": page_obj,
    }
    return render(request, "movies/index.html", context)

```



```html
<!-- index.html -->

<div class="pagination">
    <span class="step-links">
        {% if movies.has_previous %}
            <a href="?page=1">&laquo; first</a>
            <a href="?page={{ movies.previous_page_number }}">previous</a>
        {% endif %}

        <span class="current">
            Page {{ movies.number }} of {{ movies.paginator.num_pages }}.
        </span>

        {% if movies.has_next %}
            <a href="?page={{ movies.next_page_number }}">next</a>
            <a href="?page={{ movies.paginator.num_pages }}">last &raquo;</a>
        {% endif %}
    </span>
</div>
```



근데 못생김...

https://django-bootstrap-v5.readthedocs.io/en/latest/templatetags.html#bootstrap-pagination 

```bash
$ pip install django-bootstrap-v5
```

```python
# settings.py
INSTALLED_APP=[
    ...,
	'bootstrap5',    
]
```

```html
{% load bootstrap5 %}

<div>
    {% bootstrap_pagination movies %}
</div>
```



## Infinite Scroll

멋있다,,~

```bash
$ pip install djangorestframework
```

```python
# settings.py
INSTALLED_APPS= [
    ...,
    'rest_framework',
]
```

```html
<!-- base.html에서 구멍 뚫고 -->
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  {% block script %}{% endblock script %}
```

```html
<!-- index.html -->
{% block script %}

{% endblock script %}

```



저러면 우리는 응답을 html로 받게 되는데 우리가 필요한 건 json이므로 serializer를 만들어준다

```python
from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = "__all__"
```

