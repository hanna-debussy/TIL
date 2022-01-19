# 01_01_파이썬기초

jupyter notebook 중 외우지 못한 것들 위주

## 1. 변수 Variables

* 수식으로 쓰여져있다고 해서 수학처럼 이해하지 말 것!!



### 2. 자료형 data

* 부동소수점(float) 처리에서 뺄셈에 오류가 날 때가 있다

```python
# a와 b의 차이가 1e-10 값 이하이면 a 와 b 는 같다고 볼 수 있다
abs(a - b) <= 1e-10
# or epsilon: 부동소수점 연산에서 반올림을 함으로써 발생하는 오차 상환
abs(a - b) <= sys.float_info.epsilon
# or math.isclose() from python 3.5
import math
math.isclose(a, b)  # this is the BEST
```



* wow complex로 변환할 때 + 사이드에 띄어쓰기가 있으면 안 된다!

```python
complex("1+2j")
# => (1+2j)
complex("1 + 2j")  # ㅎㅓㄹ,,, 이것 또한 파싱이다
# ValueError: complex() arg is a malformed string
```



* string은 immutable

```python
a = 'my string?'
a[-1] = '!'
# TypeError: 'str' object does not support item assignment
```



* string은 iterable: 순회 가능하다

```python
a = "SSAFY"
for char in a:
    print(char)
    
"""
S
S
A
F
Y
"""
```



* escape sequence: \를 통해 특수문자 or 조작 가능

```python
print('철수야 \'안녕\'')
print('이 다음은 엔터. \n그리고 탭\t탭')
```



* string interpolation

```python
# print 할 때 지정된 변수를 불러오는 행위들
name = "김도영"
score = 4.15

print("%s의 학점은 %.2f입니다." %(name, score))  # 우우~~~~ bad

print("{}의 훌륭한 성적은 {}입니다.".format(name, score))  # 우와~~~~

print(f"{name}의 멋짱풍파 학점은 {score}입니다.") # f-strings: 간지 그 자체

print(f"""
Hello,
{name}
""") # 가능하다

# f-strings에서는 연산 / 출력형식 지정 가능!
pi = 3.141592
# .3 = 소수점 자리를 3개 '미만'으로
# {} 안에서 연산
print(f"원주율은 {pi:.3}, 반지름이 2일 때 원의 넓이는 {pi * 2 * 2}임다")
```



