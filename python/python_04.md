# OOP: Object Oriented Programming

양심선언 난 이런 거 몰랐다!



## 객체 Object

모든 것은 객체다
모든 객체는 타입, 속성, 메서드를 가진다

약간... 관념이라 생각하면 됨
이런 타입, 이런 속성, 이런 메서드를 가진 애들은 모두 이렇게 부를 거야 라고 만들어둔 다음 그런 특정한 애(instance)들을 만드는 거지

`class ClassName:`: 클래스를 정의할게~!

`instanceName = ClassName()`: 인스턴스 만들기

속성은 `instanceName.itsAttribute`,
메서드는 `instanceName.itsMethod()`



```python
"""
class 정의에서는 원래 주석을 이렇게 달아야 한다
여기서는 간단하게 적는 이상 #로 잠깐만 할게
"""

class Person:
    def __init__(self, name, study):  # 생성자! 시작할 때 하는 거
        self.name = name  # 이렇게 속성을 정의할 수 있다
        self.name = study
        # 얘도 일종의 함수이므로 받은 인자(name, study)가 init을 벗어나면 소멸하게 되므로 self.sth에 저장/백업을 한다고 생각하면 쉽다        
    
    def __del__(self):  # 소멸자!
        print('나는 간다...')  # 해당 instance가 이 class와의 연결이 끊어지면 하는 행동이 여기 적힌다
    
    walk = "두 발로 걸어요"  # 요건 class 변수: 모든 인스턴스가 공유하는 class 내부의 정의다

    
    ## __(sth)__ 의 형태는 magic method라 한다
    def __str__(self):
        return f'나는 {self.name}'  # displayname
    
    def __repr__(self):  
        return f'I am {self.name}'  # username
        
        
    # 속성을 정의한다
    def talk(self):
        print('인간에게는 언어가 있습니다')
    
    def study(self, school):  # 변수를 넣을 수도 있다
        print(f'제 최종 학력은 {self.school}')
    
    
    # 함수의 인자와 동일하게 매개변수를 정의할 수 있다
    def eat(self, food="밀면", *args):
        print(f'{food}이 생각나네')
        if args:
            for arg in args:
                print(f"근데 {arg}도 먹고 싶긴 하다")
```



## 인스턴스 Instance

```python
p1 = Person("김도영", "university")

p1.walk  # 변수는 이렇게 접근
p1.walk = "변경 가능"
# p1의 walk가 바뀐 것이지 class 전체의 walk가 바뀐 건 아니다

p1 = 1  # class와 끊어지는 순간 == del p1, __del__가 실행된다
```



## 속성 Attribute

```python
# magic method: __sth__

class classMate:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __gt__(self, other):
        return self.age > other.age
    	# 아 비교연산 매직 메서드들은 여러 인자들 중 뭘 비교할지 정할 수 있다는 점에서 필요하구나
```



## Class Method & Static Method

* Class Method: 클래스 자체와 그 속성에 접근할 필요가 있을 때
* Static Method: 속성을 다루지 않고 단지 기능만 하는 메서드를 정의할 때

```python
class MyClass:
    
    def instance_mthd(self):
        return self
    
    @classmethod
    def class_mthd(cls):
        """
        classmethod는 첫번째 인자로 cls를 꼭 가져온다
        cls로 >현재 실행<된 class 속성을 가져오는 것
        (당연하지만) args 가져올 수도 있음
        """
        return cls
    
    @staticmethod
    def static_mthd(arg1, arg2):
        return arg1 + arg2  # 얘네들끼리만 노는 게 가능할 때


"""
일단 classmethod와 staticmethod 모두 인스턴스를 만들지 않아도 class의 메서드를 바로 실행할 수 있다
"""

MyClass.class_mthd()  # cls를 자동으로 전달했으므로 가능
MyClass.static_mthd()  # 자동으로 전달된 인자가 없어서 error
MyClass.static_mthd(1, 2)  # 3
```

```python
class Parents:
    who = 'parents'

    @classmethod
    def test(cls):
        return cls.who

class Child(Parents):
    who = 'child'

print(Child.test())  #child
# >현재 실행<된 class 속성 가져온댔잖아
```

**이렇게 만들면**

* 인스턴스는 인스턴스, 클래스, 정적 메서드 모두에 접근할 수 있지만 클래스 메서드와 스태틱 메서드는 호출하지 않는다(하지 마!)
  * => 인스턴스 거는 인스턴스 메서드로 설계할 것
* 클래스 또한 인스턴스, 클래스, 정적 메서드 모두에 접근할 수 있지만 클래스에서 인스턴스 메서드는 호출하지  못한다
  * => class 입장에서는 instance가 수십수백수천 개일 수 있으니까 뭘 넣어야 할지 몰라 오류가 난다





## OOP의 특징

### 상속 Inheritance

```python
class Prof:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
        
    def greeting(self):
        print(f'안녕, {self.name}')
      
    
class Student(Prof):  # 상속받을 class 이름을 넣는다
    def __init__(self, name, age, major, student_id):
        # super()로 간단히 재사용 가능
        super().__init__(name, age, major)
        self.student_id = student_id
        
p1 = Person('홍 교수', 50, 'Business')
s1 = Student('학생', 20, 'sociology','12345678')

s1.greeting()  # 부모 메서드를 상속받아 쓴다
```





### 다형성 Polymorphism

- 동일한 메서드가 클래스에 따라 다르게 행동할 수 있다고
- 서로 다른 클래스에 속해있는 객체들이 동일한 메시지에 대해 각기 다른 방식으로 작동

```python
# Method Overriding
# 자식 클래스에서 부모 클래스의 메서드를 덮어쓰는 것

class Animal:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print("grrrrrrrrr")

class Person(Animal):
    # 자식 클래스의 init도 일종의 메서드 오버라이딩임
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
    
    # 덮어쓰기!
    def talk(self):
        print("안녕")
```





### 캡슐화 Encapsulation

파이썬에서는 암묵적으로 존재...

#### Public Access Modifier

* 그냥 언더바 없이 적히는 모든 메서드나 속성들



#### Protected Access Modifier

```python
# 언더바 1개로 시작하는 메서드나 속성

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self._age = age  # 부모랑 자식에서만 호출 가능하다는 뜻 (밖에서 호출하지 말라고 표시하는 것)
    
    # 그래서 보통 get_으로 해서 밖에서 부를 수 있게 한다
    def get_age(self):
        return self._age
        
        
p1 = Person("Colin", 20)

p1._age  # 하지만 암묵적인 거라 되긴 해
p1._age = 30  # 마찬가지로 되긴 함
# '암묵적' 규칙이니까 우리 그냥 하지 말자~ 하는 거지 안 되는 건 아님 
# 하지만!!!!!!! 늘 그렇듯 하지 말자면 하지 말자

p1.get_age()  # 이게 맞쥐
```





#### Private Access Modifier

이건 암묵적인 게 아니라 강제적이다

```python
"""
started with 언더바 2개

본 클래스 내부에서만 사용할 수 있고
하위 클래스 상속 및 호출 / 외부 호출은 불가
"""

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # not 암묵적 정말 강제한 것
    
    def get_age(self):  # 얘도 보통 'get_'으로 불러내게 한다
        return self.__age
    
    def __eat(self):  # method도 이렇게 강제할 수 있다
        print("yummy")
        
        
        
p1 = Person('김도영', 27)
p1.get_age()

# __age에 직접 접근 못 함

p1.__age  # 실행 불가
p1.__eat()  # 실행 불가
```





### getter & setter

* 위에서 `get_age()`로 했던 게 getter(`@property`)라고 생각하면 되네
* 대신 getter로 가져오면 ()인 메서드가 아니라 **변수**처럼 가져오게 된다. 그만큼 메서드에 바로 값 할당/변경이 가능하고 값을 가져올 때에도 sth.name로 가져오면 된다

```python
class Person:
    def __init__(self, age):
        self.__age = age
 
    @property  # getter 설정은 @property
    def age(self):
        return self.__age
 
    @age.setter  # 변경 가능하게 만들고 싶을 때 setter
    def age(self, new_age):
        if new_age <= 19:  # 이렇게 조건 설정도 가능
            raise ValueError('법적 성인이 아닙니다')
            return
        self._age = new_age  # 갈아끼우기
 

Haley = Person(38)
print(Haley.age)  # Haley.age() XXXX
Haley.age = 17  # 이렇게 변수처럼 접근해서 변경
print(Haley.age)  # setter에 의해 변경됨
```





### 다중 상속

```python
class Dad:
    
    gene = "dad's"
    
    def walk(self):
        print("dad's walk")
        

class Mom:
    
    gene = "mom's"
    
    def walk(self):
        print("mom's walk")

        
class Child(Dad, Mom):  # Dad first
    
    def cry(self):
        print("갓기응애")

       
    
b1 = Child("Lani")
b1.gene  # 엄빠 둘다 gene이란 속성값을 가지고 있다면 앞에 가져온 dad의 gene을 가져오게 된다
b1.walk()  # 마찬가지: dad's
b1.cry()  # child's
```
