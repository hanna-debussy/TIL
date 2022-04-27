# Java Script

# DOM (Document Object Model)

### DOM?

문서 한 장(HTML)에 해당하고 이를 조작하는 것



### DOM 조작 순서

#### 선택(Select)

* `document.querySelector`

  제공한 선택자와 일치하는 첫 번째 element를 하나 픽한다. 없으면 null.

* `document.querySelector`

  제공한 선택자와 일치하는 여러 element를 선택. 지정된 셀렉터에 일치하는 node list를 리턴

* ...등등

window는 tab, document는 tab 안의 화면이라고 볼 수 있다. django로 치면 window는 root dir라고 할 수 있는데 매번 치기는 귀찮으니까 생략이 가능하다.
`document` == `window.document`



```html
<script>
const h1 = document.querySelector("h1")
const h2 = document.querySelector("h2")
// 하면 tag 선택이 가능하다. h1는 <h1></h1>, h2는 <h2></h2> 선택 중

const secondH2 = document.querySeletor("#idName")
// id로 부를 수 있다

const selectUlTag = document.querySelector("div > ul")
// div 안의 ul 태그 중 가장 첫 번째 픽해줌

const liTag = document.querySeletorAll("ul li")
// li tag들 저언부 불러준다.

const liTag2 = document.querySeletorAll(".className")
// li tag들 중에 class로 불러오기
</script>
```



#### 변경 (create)

```html
<script>
const ulTag = document.querySeletor("ul")
const newLiTag = document.createElement("li")
const markup = document.createElement("li")
// 화면엔 없는데 일단 존재는 한다
newLiTag.innerText = "태그 안의 내용을 바꿀 수 있는 innerText"
markup.innerHTML = "<strong>str을 html로 해석해줌</strong>"

// 붙여보자
ulTag.append(newLiTag)
newLiTag.append("이렇게도 문자열 추가 가능")
</script>
```

> 근데 `.innerHTML`은 사용을 권하지 않는다. 이유는 직접 악성 스크립트 삽입하는 XSS(Cross-site Scripting) 공격에 취약하기 때문이다.

```html
<script>
const newLiTag2 = document.createElement("li")
newLiTag2.innerText = "test2"
const newLiTag3 = document.createElement("li")
newLiTag3.innerText = "test3"

ulTag.append(newLiTag2, newLiTag3)
// 이렇게도 가넝한
</script>
```

```html
<script>
const newLiTag4 = document.createElement("li")
newLiTag3.innerText = "test4"
ulTag.appendChild(newLiTag4)
// appendChild는 노드만 1개씩 가능, 문자열 불가 (= 하나의 node 객체만 가넝한)
</script>
```



#### 삭제 (Delete)

```html
<script>
newLiTag4.remove()
// 바아로 슥삭

const removedChild = ulTag.removeChild("newLiTag3")
// 화면에서 지우고 그걸 removedChild에 담아둔다. 이러면 위치 변경이 가능함!
newUlTag.append(removedChild)
// 요렇게
</script>
```



#### 속성 (attribute)

```html
<script>
h1.setAttribute("class", "newClassName")
// 이렇게 새 속성을 추가할 수도, 이미 속성이 있다면 갱신이 가능
h1.classList = ["again", "again2"]
// 얘는 추가인 듯
    
h1.getAttribute("class")
// h1의 class를 가져와주세요

// cf)
h1.style.color = "red"
// 슥삭 바꾸기 가능
// but... 좋은 방법은 아니지 bootstrap처럼 className에 style 먹여둔 다음 class에 그거 먹이는 게 훨 낫다
    
const navDivs = document.querySelectorAll("nav div")
navDivs.forEach(function (div) {
    div.setAttribute("class", "className")
})
// 선택된 전부 각각에게 setAttribute	
</script>
```



#### 오 style 속성 

```html
<script>
const image = document.querySelector("img")
image.width = "450"
image.width = 450
// px 넣을 필요 xx
image.style.marginTop = '40px'
// 뭐임 얘는 px 먹힘... 이유는 없고 걍... 걍.
</script>
```



## Event Listener

### Event?

네트워크 활동이나 사용자와의 상호작용(마우스 클릭, 키보드 누르기 등) 등의 사건 발생을 알리기 위한 객체



### addEventListner

특정 이벤트가 발생하면 할 일을 등록한다.

`target.addEventLister(type, listener[])`

target: 이 객체에

type: 무슨 이벤트가 일어나면

listener: 이러이러한 사건을 발생시켜

