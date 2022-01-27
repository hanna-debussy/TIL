# OOP: Object Oriented Programming

양심선언 난 이런 거 몰랐다!



## 객체 Object

모든 것은 객체다
모든 객체는 타입, 속성, 메서드를 가진다

약간... 관념이라 생각하면 됨
이런 타입, 이런 속성, 이런 메서드를 가진 애들은 모두 이렇게 부를 거야 라고 만들어둔 다음 그런 특정한 애(instance)들을 만드는 거지

`class ClassName:`: 클래스를 정의할게~!

`instanceName = ClassName()`: 인스턴스 만들기

속성은 `instanceName.itsAttribute`, 메서드는 `instanceName.itsMethod()`



```python
class Person:
    def __init__(self, name, study):  # 생성자!
        self.name = name  # 이렇게 속성을 정의할 수 있다
        self.name = study
        # 얘도 일종의 함수이므로 받은 인자(name, study)가 init을 벗어나면 소멸하게 되므로 저장/백업을 한다고 생각하면 쉽다
    
    def __del__(self):  # 소멸자!
        print('나는 간다...')  # 해당 instance가 이 class와의 연결이 끊어지면 하는 행동이 여기 적힌다
    
    walk = "두 발로 걸어요"  # 요건 class 변수
    
    def __str__(self):  ## __(sth)__ 의 형태는 magic method라 한다
        return f'나는 {self.name}'  # displayname
    
    def __repr__(self):  
        return f'I am {self.name}'  # username
        
    def talk(self):  # 속성을 정의한다
        print('인간에게는 언어가 있습니다')
    
    def study(self, school):  # 변수를 넣을 수도 있다
        print(f'제 최종 학력은 {self.school}')
```



## 인스턴스 Instance

```python
p1 = Person("김도영", "university")

p1.walk
```





