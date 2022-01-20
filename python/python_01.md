# 01_01_파이썬기초

jupyter notebook 중 외우지 못한 것들 위주

## 1. 변수 Variables

* 수식으로 쓰여져있다고 해서 수학처럼 이해하지 말 것!!



## 2. 자료형 Data

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



## 3. 컨테이너 Container

컨테이너는 두 가지 기준으로 나눌 수 있다

* 순서
  * Sequence형: List, Tuple, Range - 순서가 있는ordered 데이터
  * Non-sequence형: Set, Dictionary - 순서가 없는unordered 데이터
* 변형 가능
  * Mutable: List, Set, Dictionary
  * Immutable: Tuple, Range



### List

### Tuple

```python
# 하나의 항목으로 구성된 튜플은 생성 시 값 뒤에 쉼표를 붙여야 한다
a = 1,
print(a)  # (1,)
```

### Range

```python
# range(n): 0부터 n-1

# range(start, end, step) start 부터 end 까지 step만큼 이동

list(range(0, -10, -1))  # n > m 인데 range(n, m) 이면 step으로 무조건 음수를 써줘야 한다 그래야 뒤로 가지
```



### cf) 패킹 / 언패킹

```python
# '*'가 패킹 언패킹 둘 다 뜻한다

# packing
x, *y = 1, 2, 3, 4
print(x)  # 1
print(y)  # [2, 3, 4]

a, b, *c = 5, 6, 7, 8, 9
print(a)  # 5
print(b)  # 6
print(c)  # [7, 8, 9] 이런 느낌

# unpacking
lst = [1, 2, 3, 4]
i, j, *k = lst
print(i, j, k)  # 1 2 [3, 4]
print(i, j, *k)  # 1 2 3 4
# wow...
```



### Set

* 세트는 중복된 값을 가질 수 없다
* 그리고 순서!!!! 순서가 없다 sequence container => set 할 때 순서 보장이 안 됨

```python
set_a = {1, 2, 3}
set_b = {3, 6, 9}
set_c = set()  # 빈 set는 {}로 쓸 수 없다 {}는 빈 dict

print(set_a - set_b)  # {1, 2}: 차집합, 그... 말 그대로 a - b 부분
print(set_a | set_b)  # 합집합
print(set_a & set_b)  # 교집합
```



### Dictionary

* 순서가 (필요)없다: key로 꺼내면 되는데 순서가 왜 필요해
* key는 **변경 불가능(immutable)한 데이터**만 가능
  * 보통은 string
* value는 list, dict를 포함한 모든 것이 가능

```python
# 중복 key 불가능
dict_a = {1: 1, "two": 2, 3: "three", 1: 4}  # 제일 마지막이 살아남는다
print(dict_a)  # {1: 4, 2: 2, 3: 3}

print(dict_a.keys())  # dict_keys([1, 'two', 3])
print(dict_a.values())  # dict_values([4, 2, 'three'])
print(dict_a.items())
# 오 위의 두 값은 그냥 type가 'dict_keys' 등등이네
```





## 4. 연산자 Operator

### 산술 연산자

### 비교 연산자

### 논리 연산자

* 단축평가

```python
print(True and False and True and True and False)  # False
# and는 false가 나오는 순간 value가 정해진다

print(True or False or True or True or False)  # True
# or는 true가 나오는 순간 value가 정해진다

# 단축평가: 하나로 확실해지면 그 뒤는 확인하지 않는다
# 속도가 향상된다는 포인트


print("a" and "b")  # "b"
# b까지 봤고 b까지 true야 (b != 0이므로 true라는 것)

print("a" and "b" and "c" and "" and "d" and "e")
# ""는 false니까 d와 e를 보지 않고 평가를 마침: 단축 평가
# 결과는 "", 즉 거짓임을 보여줌

print("a" or "b")  # "a"
# a 보자마자 전체가 True임을 결정 내림
```

### 복합 연산자

### 식별 연산자

### 멤버십 연산자

* 요소가 시퀀스(list, tuple, range, string)에 있는지 확인해줌
* `in`, `not in`

### 시퀀스형 연산자

### cf) Indexing / Slicing

```python
print([1, 2, 3, 4][1:4])  # [2, 3, 4]
# 1 이상 4 >>>미만<<<

print((1, 2, 3)[:2])  # (1, 2)
# 앞이 비어 있으면 앞 전체 ~ 2 >>>미만<<<

print(range(10)[5:8])  # range(5, 8) !! 잘린 range가 나옴 not list

print('abcd'[2:4])  # cd
# slice 마지막 인덱스가 더 크더라도 에러 x

print([1, 2, 3, 4][0:4:2])  # [1, 3]
# idx 0부터 3까지, 2 간격으로 => [0], [2]

s = "1234567890"

print(s[:3])  # 0부터 시작
print(s[5:])  # 뒤가 없다면 끝까지
print(s[::])  # :: = 앞뒤 전부 없으니 처음부터 끝까지
print(s[::-1])  # 처음부터 끝까지 인데 이제 대신 역순으로 나열하는,
```
