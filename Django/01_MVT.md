# Django: Template, View, Routing

## Django

아하 '수레바퀴를 다시 만들지 말자'
서버를 구축하는 프레임워크고나 Python web framework



### Static web page

* 클라이언트가 서버에게 요청을 하면 미리 저장된 파일을 추가적 처리 과정 없이 그대로 전달(응답)

* 그래서 모든 상황에서 모든 사용자에게 동일한 정보를 표시하게 된다



### Dynamic web page

* 요청을 받으면 추가적인 처리를 해서 클라이언트한테 보내긔
* 방문자와 상호작용을 해서 페이지가 그때그때 달라지는 것



### 프레임워크 구조

보통 디자인은 MVC(Model-View-Controller) 디자인 패턴인데...? 장고는 MTV 패턴이래 어라 갑자기...? 아하 view를 template라고 부를래 controller를 view라고 부르고 그니까 둘이 걍 같은데 이름이 다르다는 거

* Model: db의 기록을 관리(추가 / 수정 / 삭제)
* Template: 실제 내용을 보이는 그... 것( 파일의 구조나 레이아웃
* View: http 요청 수신하고 응답 반환하는 것! 요청에 db 관련이 있다면 model과도 상호작용한다 그리고 응답 서식은 template에 맡기고
* http 요청 -> url을 거쳐 -> view에 도착 -> model / template과 상호작용 해서 -> 응답



## Intro

```bash
$ python -m venv venv  # 가상공간 만들고
$ source venv/Scripts/activate  # 그거 활성화... 하면 (venv)가 나온다
$ pip install django==3.2.12
```

지금 3.2.12 버전이 TLS(Long Term Support)라서 저 버전을 쓰는 게 좋다

```bash
# 프로젝트 생성
$ django-admin startproject firstpjt .
# firstpjt 자리에 플젝 이름 쓰면 대 근데 이름에 하이픈 사용 불가 내부 키워드 당연 불가

# 서버 시작하기
$ python manage.py runserver

# 그러면 거기에 마지막에 나온 주소에 들어가면 로켓이 나온다
# cf $python manage.py runserver 8001 하면 8001번에 할당하는 거네
```



이렇게 하면 프로젝트 이름의 폴더가 만들어지는데 안에 뭐가 좀 많다

* \__init__.py 이걸 하나의 패키지로 인식하라고 말하는 거... 열면 걍 휑함
* asgi.py: Asynchronous Server Gateway Interface 웹 서버와 연결/소통하는 건데 우린 안 건드릴 것
* settings.py: 이 장고 어플리케이션의 모든 설정을 포함 wow,,,
* urls.py: 이 사이트 url과 적절한 view의 연결을 지정
* wsgi.py: Web Server Gateway Interface 얘두... 안 건드릴 거래
* manage.py: 장고 프로젝트와 다양한 방법으로 상호작용하는 커맨드들의... 모임(?) 이 폴더 안에 있는 건 아니고 그 밖 venv 있는 폴더에 있음



```bash
# application 생성
$ python manage.py startapp articles  # articles가 앱의 이름인데 통상적으로 복수형으로 합니다
```

어라 하면 articles 폴더가 생김

* admin.py: 관리자용 페이지 설정하는 곳
* apps.py: 앱의 정보들이 기록되어 있으므로 수정하지 않을 것
* models.py: 오 그 모델입니다 앱에서 사용하는 모델을 정의하는 곳
* tests.py: 플젝 테스트 코드 작성하는 곳인데 우리는 안 써
* views.py: view 함수들이 정의되는 곳



어,,, 그럼 템플릿은?
자동으로 생성되지 않음 우리가 직접 생성해줘야 한대



## Project & Application

### project

* 프로젝트에는 여러 앱이 포함될 수 있다! 플젝은 앱의 집합이라 보면 된다

### application

* 실제 요청을 처리하고 페이지를 보여주고 여튼 얘가 열심히 굴러굴러
* 앱 하나는 보통 역할 / 기능 단위로 작성



아 근데 플젝은 앱이 ㅋㅋㅋ 생성된 걸 몰라서 앱을 등록해줘야 해 생각해보니 그렇네... 폴더 구조 자체가 걍 독립적 병렬인디

* 오 그래서 플젝에 settings.py 에 조금 내리면 `INSTALLED_APPS` 적혀있네 거기 제일 위에 `'articles',` 넣어서 등록 완,

> 반드시 앱 생성하고 등록해라 등록 먼저하면 앱이 생성되지 않음

* 제일 위에 적는 이유는... 오류 나고 그런 건 아니고 약간 장고가 권장하는 작성법임

  1. 제일 위에 우리가 작성한 로컬 앱들
  2. 그다음 우리가 가져와서 쓸 서드파티 어플들
  3. 그 다음 기본 앱들

  요 순서대로 씁니다



**가상환경~앱등록 까지가 기본 중 기본! 자다 깨서도 할 수 있어야 함**



## 요청과 응답

urls.py 가보자

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls), 
]
```

`admin/` 이게 url 주소 오
지금 우리가 실행한 url 보니까 admin이네? 근데 그 이름에 맞는 `path()` 함수가 있네? 거기 보니까 `admin.site.urls`가 있네? 이거 실행시켜



이제 views.py로 가서 하나 만들어봅시다

```python
# views.py

from django.shortcuts import render

# Create your views here.
def index(request):  # 필수 인자 request: 요청 받은... 명세서? 모든 것들
    return render(request, "index.html")  # 첫 인자가 request여야 함 걍 그렇게 생겨먹음
    # index.html 자리에 원래 템플릿을 넣어야 함 지금은 없어서 임시로 일케 적어둘게
```

 urls 다음에 가야 할 view를 이어보자

```python
from django.contrib import admin
from django.urls import path
from articles import views  # 오 이렇게 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index)
]
```



그 다음 **그 폴더 내 templates 이란 폴더 만들고 안에** 템플릿 만들어준다. 여기서 작성된 게 주소/index 치고 들어가면 보이는 것!



## Template

### Django Template Language (DTL)

* 빌트인 템플릿 시스템

* 조건, 반복, 변수 치환, 필터 등의 기능을 제공한다
* if문 for문 이런 거 있지만 파이썬으로 실행되는 코드가 절 대 아 님



#### DTL syntax 1: variable

`{{ variable }}`

render()를 사용해서 views.py에서 정의한 변수를 template 파일로 넘겨주는 것

```python
def greeting(request):
    foods = ["apple", "banana", "coconut",]
    info = {
        "name": "Alice",
    }
    context = {
        'foods': foods,
        'info': info,
    }
    return render(request, "greeting.html", context)
```



#### DTL syntax 2: filter

`{{ variagle|filter }}`

표시할 변수를 수정할 때 사용



#### DTL syntax 3: tags

`{% tag %}`

반복 또는 논리를 수행해서 제어 흐름을 만드는? 오



#### DTL syntax 4: comments

주석ㅇㅇ 한 줄 주석은 `{# #}`, 여러줄 주석은 `{% comment %} blarblar {% endcomment %}`



## Template Inheritance

`{% extends "부모템플릿이름" %}` 자식 템플릿이 부모 템플릿을 확장한다고... 템플릿 최상단에 적혀야 함

부모에 이렇게 적어두면

```html
<body>
    <p>
        parents template
    </p>
    {% block content %}
      {% comment %} 이 안을 자식 템플릿들이 가져가서 채울 거임 {% endcomment %}
    {% endblock content %}
</body>
```

자식을 바로 이렇게 적으면 된다 head 필요없음

```html
{% extends 'base.html' %}

{% block content %}
    <h1>Hello I'm {{ info.name|lower }}.</h1>
    <p>what I have are {{ foods }}.</p>
    <p>my favorite is {{ foods.2 }}.</p>
{% endblock content %}
```

그러면 자식 페이지 띄우면 parents template 밑에 저 hello~ 나옴



## urls.py

### urlpatterns

app 내에 urls.py를 만들고 아예 거기서 url과 함수를 조정하는 게 일반적
: 그 때 쓰는 게 include()

name은 나중에 templates에서 url 적을 때마다 주소 적기 귀찮아서 이름을 붙여준다

```python
from django.urls import path, include

urlpatterns: [
    path("example/", views.example, name = "exmaple")
]
```



## Namespace

다른 앱 내의 같은 이름을 가진 url name을 구분하기 위해 이름공간을 설정하는 것



### templates

왜냐하면 templates 같은 경우는 앱 내 폴더가 따로 있더라도 읽을 때 templates들을 다 모아서 하나의 경로(폴더라 생각하면 쉽다)에서 보기 때문에 이름이 같으면 무조건 settings.py 에서 INSTALLED_APPS 에 적힌 순서가 더 앞인 이름에서 슥삭 가져감

=> 그래서 templates 폴더 안에 다시 해당 앱 이름을 가진 폴더를 또 만들어주면 해결이 가능

대신 view에서 함수 render에 "example/index.html" 하고 경로를 붙여줘야겠지



### app name

urls.py에서 app_name도 붙여준다 그러면 html 어디 가서 적을 때 {% url "appname:pathname " %} 형태로 적어주면 됨 앱은 다른데 path가 이름이 같을 때 얘도 path 이름만 보고는 제일 처음 적힌 순서대로 걍 잡아가기 때문에 그걸 막아줌

```python
from django.urls import path, include

app_name = "example"  # 쨘
urlpatterns: [
    path("example/", views.example, name = "exmaple")
]
```



## Base Templates

### base.html

만약 앱은 달라도 헤더랑 푸터를 동일하게 만들고 싶다면? 헤더 푸터 html을 모든 앱에 넣어둬야 할까?
오,,, 누가 봐도 개발자가 싫어하게 생긴 방법이다

=> 루트 폴더에 templates를 만들어두고 거기에 정말 base html들을 넣어두면 된다! 대신 또 등록해줘야 함
: settings.py 내 TEMPLATES 보면 'DIRS'가 비어있다 거기에 [BASE_DIR / "templates",] 넣어주면 됨 뭔 말이냐면 너 templates 훑을 때 여기 폴더도 봐달라고 추가적으로 신청을 걸어두는 거