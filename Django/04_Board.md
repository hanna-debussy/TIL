# Django

## Board

### 뭘 만들 거냐

우리는 게시판을 만들 겁니다

글을 쓰면 db에 적히고 수정을 하면 db에서 수정이 되고 삭제를 하면 db에서 삭제가 되는 간지템을...가보자고

1. 글 작성 버튼을 누르면(articles/new)
2. form 제공
3. form 제출 시 (articles/create)
4. 글 작성(db에 저장)
5. details 페이지로 이동



### first setting

```python
urlpatterns = [
    # 글 작성
    # create
    path("new/", views.new, name="new"),
    # and save
    path("create/", views.create, name="create"),
    
    # 글 수정
    #update
    path("<int:pk>/edit/", views.edit, name="edit"),
    # and save
    path("<int:pk>/update/", views.update, name="update"),
    
    #delete
    path("<int:pk>/delete/", views.delete, name="delete"),

    path("", views.list, name="list"),
    path("<int:pk>/", views.details, name="details"),
]
```

* 이게 글을 쓰면 글을 쓰는 그 form을 보여주는  path가 하나, 그걸 db에 보내주는 path가 하나 이렇게 두 개의 path가 필요함
* 마찬가지로 수정하는 것도 적는 form과 그걸 db에 날려주는 게 따로 필요하다



### 글 작성

```python
def new(request):
    return render(request, "articles/new.html")


def create(request):
    # 그 objects.create로 쓰면 나중에 밑에 pk를 잡을 수 없어서
    # article에 class 지정을 해줘야 함
    article = Article()
    article.title = request.GET["title"]
    article.content = request.GET["content"]
    article.save()
    """
    요청보낸 브라우저의 url을 이하로 바꿔주세요
    아하 원래 details/ 보내면 details.html만 응답해줬는데
    지금은 form과 함께 create/ 보내면 저 안으로 가세요 라고 응답을 해서
    그거 받자마자 거기로 가는 셈 그거시 redirect
    """
    return redirect("articles:details", article.pk)

```

인데 하나씩 뜯어봅시다

#### new

```python
def new(request):
    return render(request, "articles/new.html")
```

* 이건 그 제목을 적는 란, 내용을 적는 란, 글 작성 버튼 이렇게 있는 하나의 form만 보여주면 우리가 거기에 입력을 하면 되는 그 html만 보여주면 된다. 아직 작성을 안 했으니 오고 갈 정보가 없다고 생각하면 된다

#### create

```python
def create(request):
    # 그 objects.create로 쓰면 나중에 밑에 pk를 잡을 수 없어서
    # article에 class 지정을 해줘야 함
    article = Article()
    article.title = request.GET["title"]
    article.content = request.GET["content"]
    article.save()
    return redirect("articles:details", article.pk)
```

* 여기서 **redirect** 라는 개념이 나온다
  * 요청보낸 브라우저의 url을 이하로 바꿔주세요!
  * 아하 원래 details/ 보내면 details.html만 응답해줬는데 지금은 form과 함께 create/ 보내면 저 안으로 가세요 라고 응답을 해서 그거 받자마자 거기로 가는 셈 그거시 redirect
* 이걸 쓰려면 `from django.shortcuts import render, redirect`이라고 redirect를 추가해줘야 함
* 저 클래스를 할당 받는 인스턴스 이름으로 모든 걸 해야하는 건 알겠지

#### new.html

```html
<form action="{% url 'articles:create' %}", method="GET">
    <div>
        제목: <input type="text" name="title">
    </div>
    <div>
        내용: <textarea name="content" id="" cols="30" rows="10"></textarea>
    </div>
    <div>
        <button>글 작성</button>
    </div>    
</form>
```

* `{% url 'articles:create' %}`같은 url이 조금... 헷갈리는데 articles는 app 이름이고 create는 views에 함수 이름이 되겠다
* 그리고 **입력란에 `name`을 지정**해줘야 하는 게 필수!!!!!!
  왜냐하면 model에서 그 스키마 이름을 따라가야 한다 그래야 title에 제목란에 적은 게, content에 내용란에 적은 게 매칭이 되어 db에 저장될 수 있기 때문



### 글 수정

```python
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        "article": article,
    }
    return render(request, "articles/edit.html", context)


def update(request, pk):
    edited = Article.objects.get(pk=pk)
    edited.title = request.GET["title"]
    edited.content = request.GET["content"]
    edited.save()
    return redirect("articles:details", edited.pk)
```

인데 또 뜯어보자



#### edit

```python
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        "article": article,
    }
    return render(request, "articles/edit.html", context)
```

* '해당' 글을 가져와야 하기 때문에 get(pk=__)를 이용해 콕 찝어 가져와서 가져가야 한다



#### update

```python
def update(request, pk):
    edited = Article.objects.get(pk=pk)
    edited.title = request.GET["title"]
    edited.content = request.GET["content"]
    edited.save()
    return redirect("articles:details", edited.pk)
```

* 음 뭐... create와 매우 흡사하니 이해는 가능할 거라 본다
* 여기서도 redirect가 쓰인다 해당 형식을 잘 기억할 것



#### html

```html
<form action="{% url 'articles:update' article.pk %}", method="GET">
    <div>
        {% comment %} name 추가 {% endcomment %}
        제목: <input type="text" name="title" value="{{ article.title }}">
    </div>
    <div>
        내용: <textarea name="content" id="" cols="30" rows="10" >{{ article.content }}</textarea>
    </div>
    <div>
        <button>글 작성</button>
    </div>
</form>
```

* form 내 action에 update를 적어서 update가 form에 적혀진 정보를 가져가 함수에 맞게 처리할 수 있도록 걸어줘야 함!!
* 역시 name을 추가해서 연결해줘야 하고
* 딱 들어가면 우리 보통 이미 썼던 글이 그 안에 써져 있잖아 그러므로 value(기본 입력값)에 우리가 edit 함수에서 가져온 해당 이 글의 내용을 뽀려와야 함



### delete

```python
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect("articles:list", article.pk)
```

* 여기서도 redirect... 기릿
* 여기는 따로 html이 없다 당연함 그냥 처리하면 됨 그리고 일종의 얘의 html이 list.html이 되는 것