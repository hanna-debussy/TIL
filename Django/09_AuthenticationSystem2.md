# Authentication System

## 회원 가입

```python
# accounts의 urls.py
path('signup/', views.signup, name='signup')
```



```python
# accounts의 views.py
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# article의 create와 유사하다. 그냥... form이 다르다는 것뿐
@require_http_methods(["GET", "POST"])
def signup(request):
    # 로그인 한 사람이 들어올 필요 x
    if request.user.is_authenticated:
        return redirect("articles:index")
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 회원가입 후 자동 로그인 시키기
            return redirect("article:index")
    else:
        form = UserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html")
```



```html
<!-- base.html -->

{% if request.user.is_authenticated %} 

{% else %}
	<a href="{% url 'accounts:signin' %}">LogIn</a>
	<a href="{% url 'accounts:signup' %}">SignUp</a>
{% endif %}
```



```html
<form action="{% url 'accounts:signup' %}" mthod="POST">
    {% scrf_token %}
    {{ form.as_p}}
</form>
```



## 회원 탈퇴

```python
# accounts의 urls.py
path('delete/', views.delete, name='delete')
```



```python
# accounts의 views.py

@require_POST
def delete(request):
    is request.user.is_authenticated:
	    request.user.delete()
        auth_logout(request)
        # 탈태시키고 로그아웃 시켜야 함 로그아웃 시키느 순간 횐정을 안 들고 있게 됨
    return redirect("articles:index")
```



```html
<!-- base.html -->

{% if request.user.is_authenticated %} 
	<!-- 로그인 되었다면 -->
	<h3>
    	Hello, {{ user }}
	</h3>
	<form action="{% url 'accounts:logout' %}" method="POST">
    	{% csrf_token %}
    	<input type="submit" value="logout">
	</form>
	<form action="{% url 'accounts:delete' %}" method="POST">
        {% csrf_token %}
    	<input type="submit" value="회원탈퇴">
    </form>
{% else %}
	
{% endif %}
```



## 횐정 수정

`UserChangeForm`

```python
# accounts의 urls.py
path('update/', views.update, name='update')
```



```python
# accounts의 views.py
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm,
    UserChangeForm
)

def update(request):
    if request.method == "POST":
        pass
    
    else:
        form = UserChangeForm(instance=request.user)
    
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)
```



근데? 저 `UserChangeForm`을 쓰면 내가 admin에서 보는 모든 변경가능사항을 전부 띄워주기 때문에 우리가 form을 비로소 만들어야 한다.

```python
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        # get_user_model... 다음시간에 더 자세히 배워볼게요
        model = get_user_model()  # User
        # 찾아보면 field 이름이 다 나와있음 외우는 거 아니고 찾아서 필요한 것만 보이게 넣기
        fields = ("email", "first_name", "last_name")
        
```

```python
# views.py
from .forms import CustomUserChangeForm
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm,
    UserChangeForm  # 안 쓰이니까 지우면 됨
)


@login_required
@require_http_method(["GET", "POST"])
def update(request):
    if request.method == "POST":
        # form을 우리가 만든 걸로 써주면 된다
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("articles:index")
    
    else:
        form = CustomUserChangeForm(instance=request.user)
     
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)
```

```html
<!-- base.html -->

{% if request.user.is_authenticated %} 
<a href="{% url 'accounts:update' %}">회원 정보 수정</a>
{% else %}
	

{% endif %}
```



## 비밀번호 변경

`PasswordChangeForm`...! 와! 이 폼 형식을 전부 지원해준다니!



```python
# accounts의 urls.py
path('password/', views.change_password, name='change_password')
```



```python
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm,
    PasswordChangeForm,
) 

@login_required
@require_http_method(["GET", "POST"])
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect("article:index")
    else:
        form = PasswordChangeForm(request.user)
    
    context = {
        "form": form,
    }
    
    return render(request, "accounts/change_password.html", context)
```

```html
<!-- change_password.html -->

<form action="{% url 'accounts:change_password' %}" method="POST">
    {% csrf_token %}
    <input type="submit">
</form>
```



아 근데 비번 변경을 하고 나면 이제 이전의 나와 지금의 나를 다르게 인식하기 때문에 세션이 바뀌어서 로그인이 풀리게 된다. 그걸 막기 위해 `update_session_auth_hash(request, user)`라고 한다.

```python
#views.py

from django.contrib.auth import update_session_auth_hash


@login_required
@require_http_method(["GET", "POST"])
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()  # 해주고
            update_session_auth_hash(reqest user) # 인자에 넣어주기
            return redirect("article:index")

```

