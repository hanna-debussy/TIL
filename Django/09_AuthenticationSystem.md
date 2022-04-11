# Authentication System

## 인증 시스템이요?

인증이라고 하지만 두 기능이 어느 정도 결합되어 있기 때문에 인증과 권한 부여를 함께 제공/처리한다.

인증: 신원 확인
권한: 권한 부여(이 사용자가 무슨 작업이 가능한지를 결정)



`INSTALLED_APPS`에 있는 `django.contrib.auth`랑 `django.contrib.contenttypes` 가 이 일을 한다. 이미 필수 구성요소는 깔려있다는 말씀. 전자는 인증 프레임워크의 핵심과 기본 모델을 가지고 있고 후자는 모델과 권한을 연결시키는 일을 해준다.



## 쿡희? 세션?

### HTTP

Hyper Text Transfer Protocol, 리소스를 가져올 수 있도록 해주는 프로토콜(규칙)

얘들은 두 가지 특징이 있는데

* 비연결지향: 늘 연결되어 있는 게 아니라 요청에 대한 응답 시에만 연결됨
* 무상태: 연결이 끊기면 상태 정보가 유지되지 않음(ex. 로그인 상태). 그리고 클라이언트와 서버가 주고 받는 메시지들은 완전히 독립적이다.

이러한 특징들 때문에 클라이언트-서버 간 지속적인 관계를 유지하기 위해 쿠키와 세션이 존재한다.



### Cookie

서버가 사용자의 웹 브라우저에 전송하는 쟈근 데이터 조각. 사용자의 컴퓨터에 KEY-VALUE 형식의 데이터로 저장되는 기록 정보 파일이다. 이걸 서버가 응답과 함께 주면 그걸 로컬에 저장해뒀다가 동일한 서버에 재 요청 시 이 쿠키 파일을 함께 전송하게 된다. 한 마디로 쿠키는 '상태가 있는' 세션을 만들어주는 셈.



#### 쿠키가 하는 일

* 세션 관리: 로그인, 공지 일주일 간 보지 않기, 팝업 체크, 장바구니 등
* 개인화: 사용자 선호, 테마 설정 등
* 트래킹: 사용자 행동 기록 및 분석



### 세션

쿠키 중에서도 '상태'를 유지키는 것. 세션을 구별하기 위해 id가 필요하고 쿠키에는 id만 적혀있다. 당연함 내 정보가 쿠키에 적혀있으면 안 됨 저쪽 DB에만 적혀있어야지

헐 그렇다면? 로그아웃은? 세션을 삭제하는 행위라고 볼 수 있다



### their lifetime...

쿠키의 수명은 두 가지로 정의가 가능한데

1. session cookies

   : 현재 세션이 종료되면 같이 삭제

2. persistent cookies

   지정된 기간이 지나면 삭제



### Session in Django

* 장고의 세션은 미들웨어를 통해 구현된다.
  cf) 미들웨어: http 요청과 응답 처리 중간에서 작동한다. 미들웨어를 거쳐서 URL에 도달, 응답도 미들웨어를 거쳐서 내보냄
* database-backed sessions 저장 방식을 기본값으로 사용(변경 가능)
* 세션 정보는 django DB의 django_session 테이블에 저장된다





## 로그인

세션을 만드는 로직과 같다. 장고는 인증에 관한 빌트인 form을 제공한다.



### 만들어보자고

1. auth와 관련한 앱을 만든다. 보통 `accounts`라는 이름을 암묵적으로 사용한다.

2. 당연히 세팅 앱에 등록하고 url에 include하고 앱으로서의 세팅을 전부 잘 해줍시다

3. url.py

   ```python
   urlpatterns = [
       path('signin/', views.signin, name='signin'),
   ]
   ```

4. views.py

   ```python
   from django.contrib.auth import login as auth_login
   from django.contrib.auth.forms import AuthenticationForm
   
   
   @require_http_mthods(["GET", "POST"])
   def signin(request):
       if request.method == "POST":
           form = AuthenticationForm(request, request.POST)
           if form.is_valid():
               # 이 login 함수는 from django.contrib.auth import login에 있는
               login(request, form.get_user())  # aka auth_login
               # user: 저 Authen웅앵Form에 있음
               return redirect("articles:index")
       else:
           form = AuthenticationForm()
           
       context = {
           "form": form,
       }
       
       return render(request, "accounts/signin.html", context)
   ```

5. signin.html

   ```html
   <form action="{% url 'accounts:signin' %}" mthod="POST">
       {% scrf_token %}
       {{ form.as_p}}
   </form>
   ```

6. index.html

   ```html
   <h3>
       Hello, {{ user }}
   </h3>
   <a href="{% url 'accounts:signin' %}">LogIn</a>
   ```

   auth 모델에 User라는 class가 있어서 가능하다. 로그인하지 않은 경우에는 AnonymousUser가 뜸



## 로그아웃

당연히 세션을 delete시키는 로직과 같다

1. url.py

   ```python
   urlpatterns = [
       path('signin/', views.signin, name='signin'),
       path('logout/', views.logout, name='logout'),
   ]
   ```

2. views.py

   ```python
   from django.contrib.auth import logout as auth_logout  # 이름 겹치니까
   
   
   @require_POST
   def logout(request):
       auth_logout(request)
       return redirect("articles:index")
   ```

3. index.html

   ```html
   <h3>
       Hello, {{ user }}
   </h3>
   <form action="{% url 'accounts:logout' %}" method="POST">
       {% csrf_token %}
       <input type="submit" value="logout">
   </form>
   ```



## 로그인 사용자에 대한 접근 제한

접근을 제한하겠다는 거는 로그인한 사람과 안 한 사람을 구별하고 싶다는 건데... 거기에는 두 가지 방법이 있다

1. `is_authenticated` attribute: T/F

   user model의 속성중 하나로 모든 user 인스턴스에 대해 True를, 비로그인 anonymousUser에 대해서는 False를 항상 반환한다
   just 사용자가 인증되어있는지의 여부만을 알려줌... 권한과는 노 상관

   ```html
   <!-- base.html -->
   <!-- 
   settings.py에 templates 보면 context_processors에 auth와 request가 있다... 얘네는 탬플릿에서 바로 별도의 행동 없이 바로 쓰기 가능 -->
   {% if request.user.is_authenticated %} 
   	<!-- 로그인 되었다면 -->
   	<h3>
       	Hello, {{ user }}
   	</h3>
   	<form action="{% url 'accounts:logout' %}" method="POST">
       	{% csrf_token %}
       	<input type="submit" value="logout">
   	</form>
   {% else %}
   	<a href="{% url 'accounts:signin' %}">LogIn</a>
   {% endif %}
   ```

   근데 이렇게 하면 로그인을 했을 때에도 로그인 페이지로 갈 수 있는 상황이 된다 왜냐하면 저 속성만으로는 권한 제어가 되지 않기 때문에 views.py의 로그인 로그아웃에서 직접 또 해줘야 한다

   ```python
   # views.py
   
   @require_http_mthods(["GET", "POST"])
   def signin(request):
       # 로그인된 상태라면 들어가지 못 하고 index로 가게 추가
       if request.user.is_authenticated:
           return redirect("articles:index")
       
       if request.method == "POST":
           form = AuthenticationForm(request, request.POST)
           if form.is_valid():
               # 이 login 함수는 from django.contrib.auth import login에 있는
               login(request, form.get_user())
               # user: 저 Authen웅앵Form에 있음
               return redirect("articles:index")
       else:
           form = AuthenticationForm()
           
       context = {
           "form": form,
       }
       
       return render(request, "accounts/signin.html", context)
   
   
   @require_POST
   def logout(request):
       if reqeust.user.is_authenticated:
   	    auth_logout(request)
       return redirect("articles:index")
   ```


   그리고 로그인 못 하면 글쓰기도 못 하게 만들어버리자

   ```html
   {% if request.user.is_authenticated %}
   	<a href="{% url 'articles:create' %}">CREATE</a>
   {% else %}
   	<a href="{% url 'articles:login' %}">로그인하세요</a>
   {% endif %}
   ```

   근데 이러면? 그냥 비로그인 상태에서 articles/create 주소 직접 치고 들어가면 쓸 수 있음... 그래서 로그인이 필요한 페이지들에 대해 데코레이터가 필요하다

   

2. `login_requiered` decorator: 

   사용자가 로그인되어있지 않으면 'settings.LOGIN_URL'에 설정된 절대 경로로 redirect한다. 근데 이 절대경로 기본값이 `/accounts/login`이기 때문에... 앱 이름도 account로, 로그인 함수도 login으로 하면 편한 거지 물론 난 필기를 signin으로 해버렸지만

   ```python
   # articles의 views.py 와서
   
   from django.contrib.auth.decorators import login_required
   
   
   @login_required
   # decorator 여러 개 가능, 먼저 적힌 것들부터 확인을 한다
   def create(request):
       
       
   @login_required
   def update(request, pk):
       
       
   @login_required
   def delete(request, pk):
   ```



next parameter 쓰기

```python
def signin(request):
    if request.user.is_authenticated:
        return redirect("articles:index")
    
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # 로그인을 하고 글쓰기로
            return redirect(request.GET.get("next") or "articles:index")
    else:
        form = AuthenticationForm()
        
    context = {
        "form": form,
    }
    
    return render(request, "accounts/signin.html", context)
```

```html
<form action="" mthod="POST">  <!-- action을 지워야 함 -->
    {% scrf_token %}
    {{ form.as_p}}
</form>
```



cf) 데코레이터가 두 개일 때 구조적 문제

```python
@login_required
@require_POST
def delete(request, pk):
    return 
```

만약 비로그인 시에 글삭을 시도한다면? 먼저 나온 `@login_required`에 의해 로그인 홈페이지로 갔고, 리다이렉트 과정이 GET이라서(`return redirect(request.GET.get("next")...`) `@require_POST`에 의해 걸리게 됨

그래서 어떻게 바꿔야 하나

```python
def delete(request, pk):
    if request.user.is_authenticated:
        원래 코드
```