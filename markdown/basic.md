# '#' is same as h1

## '##' is same as h2

### h1-h6 = '#'-'######'

#### or ctrl+1-6


## list

순서가 있는 목록(ordered list)과 순서가 없는 목록(unordered list)가 있다.

### 1) 순서 있는 목록 ordered list

1. `1.` 하고 쓰면 자연스럽게 넘버링이 된다
2. 가보자고

### 2) 순서 없는 목록 unordered list

- `-` 혹은 `*`를 붙이면 글머리 기호가 붙는다
- 이렇게



## 하지만 Typora는 쓰는 대로 보인다

이게 바로 WYSIWYG (What You See is What You Get) 위씌윅

근데 참고로 한 md 안에 h1가 두 개가 있으면 안 된다 한 파일에 제목이 2개인 거랑 같은 거임 말이 안 된다는 거


## 강조(Emphasis)

#### 글자의 스타일링 지정

1. 기울임: `*`로 감싼 글자들은 *기울어집니다.*
2. 굵게: `**`로 감싼 글자들은 **굵어집니다.**
3. 취소: `~~`로 감싼 글자들은 ~~취소선이 생깁니다~~
4. 인라인 코드: 백틱(`)으로 감싼 글자들은 코드처럼 표시됩니다.



## 코드 블럭 설정하기

백틱 3개로 감싼 블럭은 코드 출력 용입니다.

``` python
def my_func():
	print('hello world')
```

백틱 3개 뒤에 띄어쓰기 없이 쓰고 싶은 언어를 적고 엔터를 치면 언어 설정을 따로 하지 않아도 설정이 된다. 



## 표,,, table

|를 파이프라 하는데 이걸 구분자로 해서 적으면 첫 머리행이 생긴다

ex) `|이름|전공|나이|`

| 이름        | 전공          | 나이        |
| ----------- | ------------- | ----------- |
| 와          | 쩐다          | 대박        |
| 다음 행으로 | 가려면        | ctrl+enter  |
| 행 안에서   | 엔터를 하려면 | shift+enter |



## 가로선

`---`를 입력하면 가로선이 생긴다

---



## 링크 & 이미지

`[링크할 이름](링크할 사이트)`

이미지는 바로 클립보드에 있는 걸 붙여넣으면 된다. 다만 그 이미지는 이 파일 자체에 포함된 게 아니고 .assets 폴더에 들어간 것이므로 .asset 폴더 지우면 이 이미지도 날아간다. 이 md랑 같이 다녀야 함.



## 수식(Latex)

> ! 원래 마크다운은 지원하지 않으나, Typora가 추가적으로 지원하는 기능 (참고로 이건 '>' 하면 이렇게 강조 처리 됨)

근데 이거는 배워야 해서 걍 찾아봐 지금 필요한 건 전혀 아님 그리고 깃헙 이런 데에 올리면 멋진 수식으로는 안 나옴