# Django: Static Files

## Static file

* 정적 파일
  : 말 그대로 응답 시 별도의 처리 없이 그냥 내용 그대로 보여주기

* 근데? Django는 staticfiles 앱을 통해 정적 파일 관련 기능을 제공 오
  약간... 이미지 css JS 이런 바뀌지 않는 것들을 관리하는 거 같애

* `{% load static %}` 을 통해 데려오네

* 아하 static files도 namespace issue가 있기 때문에 templates이랑 똑같아 appname/templates/appname 구조인 것처럼 static files도 static 폴더 만들고 그 안에 앱 이름으로 폴더 만들어서 관리한다

* 또 templates랑 똑같아 base.html 위해서 루트 폴더에 templates 만들고 경로 추가적으로 적어둔 것처럼 앱들 전역에서 쓸 것들은 settings.py에서 `STATICFILES_DIRS = [BASE_DIR / "static",]` 추가해주고 거기서 관리하면 된다



### STATIC_ROOT

#### 배포 모드

우리가 코드 짜다가 에러 났을 때 노란 페이지가 뜨고 거기에 우리 코드가 다 드러나게 되는게 배포 단계에는 그걸 숨겨야 한다. 그러기 위해서는 `settings.py에서 DEBUG = True`를 `False`로 바꾸고 `ALLOWED_HOSTS = []`에 호스트를 추가하면 오 Not Found 만 덜렁 뜨네

#### STATIC_ROOT

배포모드를 왜 말했냐면 배포모드 때에는 이걸 설정해야 하기 때문
배포 환경에서 django의 모든 정적 파일을 다른 웹 서버가 직접 제공하기 위함

배포 직전에 settings.py에 `STATIC_ROOT = BASE_DIR / "staticfiles"` 추가해주면 댄다



### 띨뜹

```html
{% extends "base.html" %}  <!-- extends는 always 최상단 -->
{% load static %}

<!-- 꼭!!! static 내 파일 가져올 때면 {% static "" %} 으로 경로 설정 해줘야 한다!!! -->
<img src="{% static 'appname/sample.jpg' %}" alt="sample">
```



근데? 이걸 첨부하고 개발자모드에서 위치 추적해보면 host/static/sample.jpg이다. 앱 안이 아님... how?
`STATIC_URL = "/static/"`이라고 서버가 켜지면 이미지 자체가 아닌 이미지의 url이 만들어지는 거... 저 `/static`은 폴더...의 느낌이기도 하지만 주소의 path 쯤이라 이해해도 되려나?



