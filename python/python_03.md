# 데이터 구조 (Data Structure)

양심선언 나는 이것을 모른다!



## String

`.find(x)`

x의 첫 번재 위치(index)를 반환
x가 없으면 `-1`를 반환

`.index(x)`

.find(x)와 비슷하지만 x가 없으면 `error`를 반환한다!!!



`.startswith(x)` 

문자열이 x로 시작하면 True를 반환, 아니면 False를 반환
`endswith(x)` 

문자열이 x로 끝나면 True를 반환, 아니면 False를 반환

>  x는 char뿐만 아니라 단어 등도 가능



`.replace(old, new[, count])`

말 그대로 old를 new로, count는 앞에서부터 old를 몇 번 new로 바꿀지 정하기



`.strip([chars])`

wow 아무것도 안 적으면 양 옆 공백 제거, char 적으면 그거 전부 제거
근데 ★ strip을 써도 해당 str은 변하지 않는다!!!!!!!!!!!!!!!!!!!!!!! 그냥 출력만 해주는 거

`.split([chars])`

쭉 이어진 str이 있으면 그걸 chars를 구분자로 하여 자르고 list로 반환

`'separator'.join(iterable)`

iterable의 문자열을 separator를 연결자로 하여 이어 붙임
중요한 건 iterable문자열이 아닌 separtor가 메서드를 제공한다!!!



> 문자열 메서드 모두 확인하기
>
> ```python
> dir('string') # dir(str)
> ```





## List

`.append()`는 그냥... 입력된 거 바로 갖다박음

`.extend()`는 []로 넣으면 안에 있는 거 빼서 넣어줌

둘 다 return이 없는 채로 원본을 변경만 시켜줌!! 별도의 결과 없이 넌 이미 변경되어있다

`.insert(i, x)` 

index i 에 x를 넣어준다요



`.pop([i])`

index i에 있는 값을 삭제 + 그 항목을 반환!
i가 지정되지 않으면 가장 마지막 항목을 삭제 + 되돌려준다



`.count(x)`

원하는 값의 개수를 반환



`.sort()`

리스트를 정렬해줌
**`sorted()`와는 다르게 원본 자체를 변형 but `None`을 반환함!!!!!!!!!!**
`.sort(reverse=True)` 하면 역순 쌉가능 = `.reverse()`



> 역시나 list method 모두 확인하는 방법
>
> ```python
> dir(list)  # dir([])
> ```





## Set

`.add(elem)`

elem을 set에 추가 **not .append()**

`.update(*others)`

여러 개를 추가



`.remove(elem)`은 elem을 삭제하고, set에 elem이 존재하지 않으면 KeyError

`.discard(elem)`도 elem을 삭제하지만 set에 elem에 존재하지 않아도 에러가 발생 X



> ```python
> dir(set)
> ```





## Dictionary



























