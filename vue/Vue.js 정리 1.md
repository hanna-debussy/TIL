# Vue.js 정리 1

* SPA(Single Page Application): 현재 페이지를 동적으로 운영하는 웹 어플리케이션
* CSR(Client Side Rendering): 서버가 아닌 클라이언트가 화면을 구성하는 것. 이렇게 하면서 트래픽이 감소하고 UX가 향상한다. 대신 전체 페이지 최종 렌더링 시점이 조금 느림. SPA가 동작 원리의 일부를 CSR 구조로 운영한다.
* SSR(Server Side Rendering): 서버가 클라이언트에게 보여줄 페이지를 모두 구성해서 전달하는 방식. 원래 전통적인 렌더링 방식이다. 검색 엔진 최적화에 적합하다. 하지만 모든 요청마다 새로운 페이지를 전달해서 트래픽이 많아진다.



Vue.js는 SPA를 완벽하게 지원



## Concept of Vue.js

### MVVM

Vue.js는 MVVM 디자인 패턴을 채택했다. Model, View, ViewModel이 그것이다.

* **Model**
  : JS Object(`{key: value}`)인데 한 마디로 데이터. 이 데이터가 바뀌면 View가 반응한다.
* **View**
  : DOM(HTML)을 뜻한다.
* **ViewModel**
  : 모든 Vue Instance를 뜻한다. View와 Model 사이에서 데이터를 얼마나 잘 처리해서 보여줄 것인지 고민해야 하는 부분이고 그 둘과 관련된 모든 일을 처리한다.



## 시작해보자고

Vue의 시작은 새 인스턴스를 만드는 것부터 시작된다.

``` vue
<div id="app">
  <!-- 이하 두 개는 똑같이 출력된다 -->
  {{ message }}
  <p v-text="message"></p>

  <!-- v- 접두사가 있는 속성값은 단일 JS 표현식이 가능 -->
  <input :checked="movie.watched? true : false">

  <!--
	v-show는 로딩이 다 된 상태임 걍 보이지 않을 뿐 (css로 따지면 hidden)
	렌더링 비용은 높지만 토글 비용이 적음 껐켰해도 한 번 로딩이 된 상태에서 가렸다 보였다만 하니까
	반면 v-if는 false일 때 렌더링되지 않음...
	그래서 렌더링 비용은 적지만 껐켰 때마다 로딩을 해서 토글 비용은 높다
  -->
  <p v-show="isTrue">v-show true</p>
  <p v-if="isTrue">v-if true</p>

  <!-- item in items 형식을 쓰고, 꼬옥 고유한 :key가 필요하다!! -->
  <div v-for="person in People" :key="person.name">
      {{ person.name }} {{ person.age }}
  </div>
  <!-- v-if랑 v-for가 같이 쓰이면 v-for가 우선순위가 높지만 걍 그렇게 동시에 쓰지 않는 걸 권장 -->

  <!-- v-on: 이벤트 발생 시 할 methods 적기 -->
  <div @click="greeting">클릭하면 인사합니다</div>

  <!-- v-bind: data와 단방향 연결 -->
  <img :src="imgSrc">

  <!-- v-model: data와 양방향 연결, .trim처럼 수식어 가넝한 -->
  <input v-model.trim="change">
  <p>
    input에 쓰인 게 여기 나타납니다: {{ change }}
    그리고 vue instance의 데이터에도 넣을 수 있고, 아님 data에서 고치면 여기서 그대로 출력된다
  </p>

  <!-- computed한 값이 double()의 형태가 아니라 double하면 나옴 당연함 함수가 아님 -->
  <p>{{ double }}</p>

  <!-- filter에서 지정한 함수는 이렇게 파이프로 추가하고, 뒤에 여러 개 더 추가 가능 -->
  <p>홀수만 나오시길: {{ numbers | getOddNums }}</p>
    
  <!-- created를 적용하면 blank가 아닌 구구절절이 나옴 -->
  <p>{{ createdNum }}</p>
</div>

<script>
  const appName = new Vue({
    // el: vue 인스턴스와 연결할 DOM 요소. new를 통해 인스턴스를 생성할 때만 필요
    el: "#app",

    // data: 이 인스턴스의 데이터 객체를 쓴다. this.로 접근, arrow func 불가
    data: {
	  message: "Hello world",
      isTrue: true,
      People: [
          { name: "Jay", age: 26, major: "Business"},
          { name: "Jay2", age: 26, major: "Business"},
      ],
      imgSrc: "어쩌구 이미지 주소",
      change: "",
      num: 12,
      numbers: [1, 2, 3, 4],
      createdNum: "blank",
    },

    // methods: 인스턴스에 추가할 메서드. this.로 접근, arrow func 불가
    methods: {
	  greeting() {
	    console.log("hi"),
      },
    },
    
    // computed: 함수처럼 보이지만 함수가 아니라 걍 함수처럼 보이는 것에 의해 계산된 '값'임
    // 값이기 때문에 캐싱이 돼서 관련 데이터가 변하지 않는 이상 여러번 불러도 또 계산하거나 그러지 X
    computed: {
      double() {
        return this.num * 2
      },
    },
      
    // watch: '데이터가 변경되었을 때' 할 함수를 지정 (변경되는지 아닌지 watch한다는 뜻)
    watch: {
      numChanged() {
        // 참고로 이렇게 데이터랑 연동시키려면 backtick 쓰고 ${}로 가넝한
        console.log(`${this.num} is changed.`)
      },
    },
    
    // filter: 음... 말 그대로 필터(??)
    filter: {
      getOddNums(nums) {
        // 시도때도 없이 this. 붙이는 거 아니고 data에 있는 거만...
        const oddNums = nums.filter(function (num) {
          return num % 2
        })
      },
    },
      
    // lifecycle hook이라고... 생애주기마다 이름이 있는데 그 주기(상황)에 동작시킬 함수 넣는 거
    // 근데 거의 created만 쓴다
    created() {
      // data도 넣을 수 있고, event도 넣을 수 있다
      this.createdNum = "데이터 입력은 blank지만 실행되자마자 지금 데이터로 바뀐다"
      console.log('createdNum will update, as this.createdNum is now reactive.')
    },
  })
</script>
```