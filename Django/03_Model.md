# Django

## Model

* about Database
* 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함
* 일반적으로 각각의 보델은 하나의 데이터베이스 테이블에 매핑됨



## 하지만 그 전에 Database...?

체계화된 데이터...겠지 그렇지 그런데



### 기본구조

* 테이블
  : 행과 열로 조직된 테이터 집합
* 스키마 schema
  :자료의 구조, 표현 방법, 관계를 정의해둔 구조... 그러니까 테이블에서 제일 머리행, 그리고 그 속성들(int, str...) 각각 열들이 무슨 필드를 가지는지 그 명세를 적어둔 것
* 레코드
  : 한 행을 의미
* 기본키 Prime Key, PK
  : 각 행의 고유값...! 동명이인이 있으면 어떻헤? 약간 id 느낌으로 db 관리 및 관계 설정 시 중요하다



### Query

* 데이터를 조회 및 조작하기 위한 명령어
* 보통 DB를 조작한다는 말을 쿼리를 날린다고 한대 오,,,



## ORM

* object - relational - mapping
  객체-관계웅앵데이터(RDBMS)-연결해서 db를 조작해주는 프로그램(???)
* 엄 그러니까 객체지향언어를 SQL로 변환하는 프로그램
* 왜냐면 DB를 조작할 수 있는 언어는 오직 SQL 뿐인데 우리는 객지언(; 파이썬 같은)을 다룰 수 있으니까 번역을 중간에서 해줘야 하는 거임 그게 ORM의 역할
* 장점이라 함은... SQL 몰라도? DB 조작 쌉가능 객체 지향적 접근이 가능하니까 생산성도 높아져
  근데? 그래도 ORM만으로는 완전한 서비스를 구현하기 어려운 경우가 있긴 혀
* 그래도 우리의 요점은 웹 개발을 빨리하기 위함이니까 생산성을 더 따지는 것



## Model로 돌아오자면

우리는 모델을 클래스로 만들 겁니다 왜냐면 행동까지 지정해둘 수 있기 때문

```bash
# 쭉... 보통 프로젝트 만들 듯 하고 나서
$ pip install django_extensions ipython
# 확장 프로그램이랑 저... ipython이란 걸 더 깔아준다
```

그 다음 그 다음 그 모냐 settings.py에 `INSTALLED_APPS`에 `django_extensions` 를 등록해준다



```python
from django.db import models

# Create your models here.

# models.Model을 통해 DB와 통신할 수 있는 모든 기능을 상속받는 거
class Student(models.Model):
    # 그냥 단순히 int, str 하고 지정해줄 수는 없다 models에서 가져와야 함
    # 왜냐면? 우리는 지금 장고(파이썬)을 하고 있는 게 아니니까
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    # CharField는 max_length 인자가 필수
    major = models.CharField(max_length=100)
```

그 다음 지금 우리가 하는 말을 ORM으로 보내서 SQL에 반영해줘 라는 명령어

```bash
$ python manage.py makemigrations appName
# 이거는 commit push처럼 버전을 만드는 거
$ python manage.py migrate appName
# 실제로 SQL에 반영해줘
```

그리고 확장 프로그램에 sqlite viewer 깔아서 자료를 한번 봐보자고 저거 깔면 db.sqlite3 파일 볼 수 있음 깔끔한 테이블이쥬?

고러고? 데이터를 넣어보자고

```bash
$ python manage.py shell_plus
# 이게 django_extensions 기능
```

우와 그러고 Student 써서 class 들어가고 s1 = Student() 해서 객체 하나 만들어보자
그리고 또 구구절절하게 s1.name s1.age 머 일케 다 집어넣어
근데 그렇다고 db에 바로 반영되지는 않고 s1.save() 해줘야 한다

cf) 좀더 간지나는 건

```bash
$ python manage.py shell_plus --print-sql
# --print-sql 설정하면 입력하고 save할 때 그 데이터 보여줌
$ s3 = Student(name="Jay", age=26, major="business")
```



한편 class들에게는 비서가 딸려있는데 얘 이름이 manage 아니고 objects라고 한다
그래서 bash에 `Student.objects.create(name="Jay", age=26, major="business")` 하면 save 없이 바로 연결을 시켜줌 objects가
또 `$ s4 = Student.objects.get(pk=1)` 해두면? s4에 1번 객체가 저장되는 거임
이게 우리가 객체로 바로 슈슉 접근할 수 있는 간지 s4.name 하면 바로 내 이름 나옴

또 뭐 `$ Student.objects.filter(age__gt=26)` 뭐 이런 거로 필터링도 할 수 있는데 결론이 뭐냐면
**파이썬을 통해 우리가 SQL에 마음대로 접근할 수 있다는 거**



자 이제 col을 추가하려고 적기만 하면? not반영 yet 그래서 뭐 대충 `is_married = models.BooleanField` 을 적고 다시 추가하려고 `$ python manage.py makemigrations appName` 하면?
뭔가 구구절절하게 나와 umm 이상하다;
걍 바로 뚝딱 붙이면 그 전 데이터들의 값들이 없는 상태로 붙잖아 그래서 그거 물어보는 거
1 내가 디폴트 값 일단 임의로 설정하깨
2 지금은 이거 끌 테니까 너 직접 디폴트 값 적고 다시 와
오 이거는 데이터 없는 상태로 추가하려 해도 뜬대 일단 테이블이 만들어진 이상 뜨는 경고문

```python
is_married = models.BooleanField (default=False)
# 해서 default값을 우리가 저장해주자
```





