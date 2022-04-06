# Django Form Class

우리는 여태 html form이나 input을 통해 데이터를 받았는데 이렇게 받으면 데이터 유효성 검증한 결과를 다시 함께 표시해야 함(사용자가 입력한 데이터가 형식에 안 맞을 수 있잖아 always,,,) 근데 이걸 구현하는 게 너무 귀찮고 뭐 많이 해야하나 봐
&rarr; 이런 작업과 반복 코드를 줄여주는 게 **Django Form**



## 이게 뭐냐?

* 유효성 검사 도구 중 하나
  : 외부 공격 및 데이터 손상에 대한 중요한 방어 수단!
* 유효성 검사를 단순화 & 자동화 & more 안전 & speedy
* 그래서 뭘 해주느냐?
  1. 렌더링 위한 데이터 준비 및 재구성
  2. 데이터에 대한 HTML forms 생성
  3. 사용자로부터 받은 데이터 수신 및 처리



## Form Class

얘도 클래스처럼 하나 봐... 이게 form 관리 시스템의 핵심이래



### Form 선언하기

```python
# app/forms.py를 만들어조

from django import forms

class AppForm(forms.Form):
    # 구조가 모델과 상당히 유사
    title = forms.CharField(max_length=10)
    content = forms.Charfield()	# 어라 TextField가 없네
```

```python
# 그리고 views.py 간다
# 우리가 데이터를 받는 건 new와 edit인데 일단 new를 가보자고

from .forms import AppForm	# 추가


def new(request):
    form = AppForm()
    context = {
        "form": form,
    }
    return render(request, "app/new.html", context)
```

```html
<!-- new.html -->

<form action="blarblar" method = "blar">
    {{ form }}
    <!-- 만 일단 넣어보자 -->
</form>

<!--
form이 있는 이상 title에 정말 10자밖에 안 써진다 원래 form이 없으면 model에서 10자라고 해놔도 10자 이상으로 쓸 수 있었거든
그리고 block이던 요소들이 inline 요소가 된다 -> 이건 rendering options를 통해 바꿈
-->
```

#### form rendering options

* as_p(): `<p></p>` 태그로 감싸져서 렌더링 됨 - block으로 되겠지
  : `{{ form.as_p }}`
* as_ul(): `<ul></ul>` 태그로 ㅇㅇ
* 또 있는데... 교재 체크



#### HTML input 요소 표현 두 가지

1. forms.py에서 field 지정하기
   &rarr; 하지만 이건 지원하지 않는 field가 있음

2. **widgets**

   * GET/POST 딕셔너리에서 데이터 추출
   * 반드시 form fields에 할당된다 (단독 사용 불가)

   ```python
   # forms.py에서
   
   class AppForm(forms.Form):
       title = forms.CharField(max_length=10)
       content = forms.Charfield(widget=forms.Textarea)
   ```

   그러면 content가 textarea로 바뀐당

   * django widget 검색하면 공홈에 종류 뜨니까 다 외우진 말고
   * 유효성 검사와는 상관이 없고 그냥 input 표현방법을 처리할 뿐!



#### 위젯... 중요하군

```python
# select에 대해 알아보자

class AppForm(forms.Form):
    REGION_A = "sl"
    REGION_B = "dj"
    REGION_C = "bu"
    # 여기가 option 처리될 부분
    REGIONS_HOICES = [
        (REGION_A, "서울"),
        (REGION_B, "대전"),
        (REGION_C, "부산"),
    ]
    title = forms.CharField(max_length=10)
    content = forms.Charfield(widget=forms.Textarea)
    
    region = forms.ChoiceField(choices=REGION_CHOICES, widget=forms.Select)
```



## Model Form

* html에 {{ form }} 이라 적은 것만으로도 칸이 생겼잖아 결국 모델에서 적은 거랑 form에서 적는 거랑 행위가 중복된다는 말씀 그걸 좀 거들어주려고
* form과 DB는 밀접한 관련이 있다. form으로 받아서 DB에 저장하니까... 그래서 만약 우리가 쓰고픈 form의 구조가 DB와 비슷하다면 그걸 끌어와서 쓸 수 있겠지 그걸 장고는 해냅니다
  모델로 만들어진 테이블 필드 속성에 맞게 자동으로 html element를 만들어준다
* 그리고 이를 통해 받은 데이터를 view 함수에서 유효성검사도 가능하게 한다



### Meta

~~not facebook~~

```python
# forms.py

from .models import ModelName	# 추가

class AppForm(forms.ModelForm):
    
    class Meta:
        model = ModelName
        # fields = ["title", "content",]로도 할 수 있지만
        fields = "__all__"		# 모든 필드를 가져올 수 이따
        exclude = ("region",)	# 출력에서 뺄 거... tuple도 되고 list도 된다
```

wow... model의 fields들을 해석해서 알아서 만들어주냄 위에처럼 구구절절 안 적어줘도 된다 바로 다 만들어짐



```python
# views.py에서 create가 어케 바뀌느냐

def create(request):
    form = AppForm(request.POST)	# request.POST.get("fieldname")들이 한 줄에
    if form.is_valid():				# 유효성 검사를 한 후
        a1 = form.save()
        return redirect("appName:detail(보낼 곳)", a1.pk)
    return redirect("유효성검사를실패하면보내지않을곳")
```



### 어메이징 new + create

아니 이게 된다고 ㄴㅇㄱ 이제는 따로 함수를 만들 필요가 없다

```python
def create(request):
    if request.method == "POST":
        # create 부분
        form = AppForm(request.POST)
    
        if form.is_valid():
            a1 = form.save()
            return redirect("appName:detail(보낼 곳)", a1.pk)
    else:
        # new
        form = AppForm()
    context = {
        "form": form,
    }
    return render(request, "create.html", context)
    # 하고 new.html도 create.html로 바꿔주자 이제 new는 놓아주자고
    # urls.py 에서도 new 없애주고
```

이렇게 하면 html form action을 비워둘 수 있다



### edit + update

```python
def update(request, pk):
    if request.method == "POST":
        # update
        article = ModelName.objects.get(pk=pk)
        form = AppForm(request.POST, instance=article)	# instance 까먹지 뫄    
        if form.is_valid():
            a1 = form.save()
            return redirect("article:detail", article.pk)
        
    else:
        # edit 부분
        article = ModelName.objects.get(pk=pk)
        form = AppForm(instance=article)	# instance=는 정해진 부분
    context = {
        "article": article,
        "form": form,
    }
    return render(request, "articles/update.html", context)
	# 마찬가지로 html 이름 바꾸고 html에 {{ form.as_p}} 해주고(submit은 남김) urls.py에 edit도 바이바이
```



POST...가 아니면 뭐라고라



### 위젯 활용하기

```python
# forms.py
class AppForm(forms.ModelForm):
    
    class Meta:
        model = ModelName
        title = forms.CharField(			# 위젯 사용하려면 __all__ 못 쓴다
        	widget = forms.TextInput(
                attrs={
                    "class": "my-class",	# html에서 class 지정하능 고
                    "placeholder": "제목을 입력하세요",
                }
            ),
            error_messages={
                "required": "님 제목 입력 안 하셨어요"
            }
        )
```



## Rendering Fields Manually

### 수동으로 form 완성하기

#### form을 해체 슉. 슈슉.

```html
<form>
    <div>
        {{ form.title.label_tag }}
        {{ form.title.errors }}
        {{ form.title }}
    </div>
    <div>
        {{ form.content.label_tag }}
        {{ form.content.errors }}
        {{ form.content }}
    </div>
</form>
```

저... rendering field manually는 그대로 찾아보면 공식 문서가 있슴다



#### 반복으로 더 간단하게 해체 슉. 슈슉. 슉.

```html
<form>
    {% for field in form %}
    	{{ field.label_tag }}
    	{{ field.errors }}
    	{{ field }}
    {% endfor %}
</form>
```



### with Bootstrap

#### 위젯 힘 빌리기

```python
class AppForm(forms.ModelForm):
    
    class Meta:
        model = ModelName
        title = forms.CharField(
        	widget = forms.TextInput(
                attrs={
                    "class": "my-class form-control",  # bootstrap class 여기에
                    "placeholder": "제목을 입력하세요",
                }
            ),
            error_messages={
                "required": "님 제목 입력 안 하셨어요"
            }
        )
```

```html
<form>
    {% for field in form %}
    	{{ field.label_tag }}
    	{% if field.errors %}
    		{% for error in fields.errors %}
    			<div class="alert alert-danger">{{ error }}</div>
    		{% endfor %}
    	{% endif %}
    	{{ field }}
    {% endfor %}
</form>
```



#### 서드파티 힘 빌리기

```bash
$ pip install django-boogstrap-v5
$ pip install -e .
```

```python
# settings.py
INSTALLED_APPS = {
    'bootstrap5',
}
```

```html
<form>
    {% bootstrap_form form %}
    <input type="submit">
</form>
```

