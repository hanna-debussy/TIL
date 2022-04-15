# 1:N

## Accounts

```python
# BASE_DIR/settings.py

AUTH_USER_MODEL = "accounts.User"
# 제공하는 것 말고 우리가 만든 Uer를 쓸 것
```



```python
# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    age = models.PositiveIntegerField(default=0)
```

* 장고가 제공하는 User는 AbstractUser의 하위 클래스라서 속성을 물려받는다. 그래서 우리도 우리만의 User를 만들 때 AbstractUser를 가져와서 만드는 것
  물려받으면 기본적으로 Username, First name, Last name, Password, Password confirmation이 들어있다. 우리가 만약 age를 정의했다면 여기에 age가 추가되는 것



```python
# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    
    age = forms.IntegerField(min_value=12, max_value=150, required=False)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "age")
        """
        same as:
        fields = ("username", "first_name", "last_name", "age")
        """
        

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = User
        # 찾아보면 field 이름이 다 나와있음 외우는 거 아니고 찾아서 필요한 것만 보이게 넣기
        fields = ("email", "first_name", "last_name")
```

form도 입맛대로 항목 넣어주고

나중에 알겠지만 회원수정 란도 그냥 쓰면 모든 항목이 다 뜨기 때문에 form을 수정해주어야 한다



```python
# accounts/urls.py

from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path('delete/', views.delete, name='delete'),						# 탈퇴
    path('update/', views.update, name='update'),						# 회원정보 수정
    path('password/', views.change_password, name='change_password'),	# 비번 변경
    path("<str:username>/", views.profile, name="profile"),
]
```

기획을 한 다음



```python
# accounts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import (
    login as auth_login, 
    logout as auth_logout,
    get_user_model,
)
from .forms import CustomUserCreationForm, CustomUserChangeForm


@require_http_methods(["GET", "POST"])
def signup(request):
    if not request.user.is_authenticated:				# 로그인한 사람은 들어올 필요 X
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)				# 회원가입 후 바로 로그인 시켜주기
                return redirect("articles:articles_index")
        else:
            form = CustomUserCreationForm()
        context = {
            "form": form,
        }
        return render(request, "accounts/signup.html", context)
    else:
        return redirect("articles:articles_index")		# 로그인한 사람은 index로


@require_http_mthods(["GET", "POST"])
def login(request):
    if not request.user.is_authenticated:				# 로그인한 사람이 다시 로그인할 수 X
        if request.method == "POST":
            form = AuthenticationForm(request, request.POST)	# 얘는 request 필요
            if form.is_valid():
                user = form.get_user()
                auth_login(request, user)
                # or가 첫 번째 인자가 0(False)이 아니라면 바로 그걸 반환하니까 그걸 이용한 것
                return redirect(request.GET.get("next") or "articles:articles_index")
        else:
            form = AuthenticationForm()
        context = {
            "form": form,
        }
        return render(request, "accounts/login.html", context)
    else:
        return redirect("articles:articles_index")		# 로그인한 사람은 index로


@login_required
@require_POST
def logout(request):
    auth_logout(request)
    return redirect("articles:articles_index")


@require_POST
def delete(request):
    is request.user.is_authenticated:
	    request.user.delete()			# 탈퇴시키고 로그아웃 시켜야 함 
        auth_logout(request)			# 로그아웃 먼저 하면 횐정을 안 들고 있게 됨
    return redirect("articles:index")


@login_required
@require_http_method(["GET", "POST"])
def update(request):
    if request.method == "POST":
        # form을 우리가 만든 걸로 써주면 된다
        form = CustomUserChangeForm(request.POST, instance=request.user)	# instance 
        if form.is_valid():
            form.save()
            return redirect("articles:articles_index")
    else:
        form = CustomUserChangeForm(instance=request.user)
     
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)


@login_required
@require_http_method(["GET", "POST"])
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(reqest user) # 비번 변경 후 로그인 유지
            return redirect("article:index")
    else:
        form = PasswordChangeForm(request.user)
    
    context = {
        "form": form,
    }
    
    return render(request, "accounts/change_password.html", context)


def profile(request, username):
    # 알아서... 다만 인자를 username 가져오는 거 잊지 말고
    pass


```

* 비번 변경을 하고 나면 이제 이전의 나와 지금의 나를 다르게 인식하기 때문에 세션이 바뀌어서 로그인이 풀리게 된다. 그걸 막기 위해 `update_session_auth_hash(request, user)`라고 한다.



```html
<!-- 기본 형식 -->
<form action="{% url 'accounts:해당하는 url' 필요한 인자 %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <button>submit</button>
</form>
```



## Articles

```python
# articles/models.py

from django.conf import settings

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.id}> {self.content}"
```

* User를 여기 있는 User model로 쓰기로 한 이상 다른 곳에서는
  `from django.contrib.auth import get_user_model
  User = get_user_model()`
  로 해야 하지만 모델에서는 이렇게 하는 걸 권장하지 않는다. 대신 `from django.conf import settings`해서 `settings.AUTH_USER_MODEL`로 넣으면 settings.py에 적힌 `accounts.User`가 입력된다
* `CASCADE`: 글이 사라지면 그에 딸린 DB도 사라지게 만듦



```python
# articles/forms.py

from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ("title", "content",)  # __all__하면 user 선택란도 들어감
        """
        fields에 들어간다는 말은 
        1 유효성 검사를 하겠다 (is_valid()를 돌려보겠다)
            -> 그 말은 fields에 없다면 체크 안 한다는 말씀
        2 HTML에 출력될 것이다
        """
        # cf) exclude = ("user", )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ("content",)
```



```python
# articles/urls.py
from django.urls import path
from . import views


app_name = "articles"

urlpatterns = [
    path("create/", views.article_create, name="article_create"),
    path("", views.articles_index, name="articles_index"),
    path("<int:article_pk>/", views.article_detail, name="article_detail"),
    path("<int:article_pk>/update/", views.article_update, name="article_update"),
    path("<int:article_pk>/delete/", views.article_delete, name="article_delete"),
    path("<int:article_pk>/comments/create", views.comment_create, name="comment_create"),
    path("<int:article_pk>/comments/<int:comment_pk>/delete/", views.comment_delete, name="comment_delete"),
]
```

accounts나 그 외 app들과 헷갈릴 수 있으므로 이제 views이름에 표시를 해준다



```python
# articles/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.
@login_required
@require_http_methods(["GET", "POST"])
def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)   # 저장xx article 객체만 만들어두는 상태
            # 우리가 forms에서 user를 빼놔서 save()가 되지 않기 때문에 따로 넣어줘야 한다
            article.user = request.user         # 글쓴이는 요청보낸 바로 그 사람이다
            article.save()
            return redirect("articles:article_detail", article.pk)
    else:
        form = ArticleForm()

    context = {
        "form": form,
    }

    return render(request, "articles/article_form.html",context)


@require_safe
def articles_index(request):
    articles = Article.objects.order_by("-pk")	# 최근 글이 가장 위에
    context = {
        "articles": articles,
    }
    return render(request, "articles/articles_index.html", context)


@require_safe
@login_required
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm()
    context = {
        "article": article,
        "form": form,
    }
    return render(request, "articles/article_detail.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def article_update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        if request.method == "POST":
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                article.save()
                return redirect("articles:article_detail", article.pk)
        else:
            form = ArticleForm(instance=article)

        context = {
            "form": form,
        }

        return render(request, "articles/article_form.html",context)
    else:
        return redirect("articles:article.detail", article.pk)


@login_required
@require_safe
def article_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        article.delete()
    return redirect("articles:articles_index")


@login_required
@require_POST
def comment_create(request, article_pk):
    # article_pk가 올바른지 검증하려고 get_object_or_404에 넣어보는 거
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.article = article
        comment.save()
    
    return redirect("articles:article_detail", article.pk)


@login_required
@require_POST
def comment_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.user == comment.user:
        comment.delete()

    return redirect("articles:article_detail", article.pk)
```



```html
<!-- article_detail.html -->

<h1>{{ article.title }}</h1>			# 제목
<h3>{{ article.user.username }}</h3>	# 작성자

<div>
{% if request.user == article.user %}	# 오직 작성자만
  <div>
    <a href="{% url 'articles:article_update' article.pk %}">
      <button>UPDATE</button>
    </a>
  </div>
  <form action="{% url 'articles:article_delete' article.pk %}">
    {% csrf_token %}
    <button>DELETE</button>
  </form>
{% endif %}
</div>

<p>
  {{ article.content|linebreaksbr}}
</p>

<hr>

<!-- 댓글 작성 -->
<ul>
  {% for comment in article.comment_set.all %}
  <li>
    {{ comment.user.username }}: {{ comment.content }}

    {% if request.user == comment.user %}		# 댓글 당사자라면
    <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
      {% csrf_token %}
      <button>삭제</button>
    </form>
    {% endif %}

  </li>
  {% endfor %}
</ul>

{% comment %} 댓글 리스트 {% endcomment %}
<form action="{% url 'articles:comment_create' article.pk %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <button>등록</button>
</form>
```



## base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <nav>
    <ul>
      <li><a href="{% url 'articles:articles_index' %}">Home</a></li>

    {% if request.user.is_authenticated %}		# 로그인한 사람
      <li><a href="{% url 'articles:article_create' %}">New Article</a></li>
      <li><a href="{% url 'accounts:profile' user.username %}">{{ user.username }}'s Profile</a></li>
      <li><a href="{% url 'accounts:logout' %}">Logout</a></li>
    
    {% else %}									# 비로그인
      <li><a href="{% url 'accounts:login' %}">Login</a></li>
      <li><a href="{% url 'accounts:signup' %}">Signup</a></li>
    {% endif %}
    </ul>
  </nav>
  {% block content %}{% endblock content %}
</body>
</html>
```















