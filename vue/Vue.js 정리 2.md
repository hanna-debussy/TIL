# Vue.js 정리 2

## Vue CLI

### Node.js

일단 Node.js를 설치해야 한다. 그게 뭔데요? JS를 브라우저가 아닌 환경에서도 구동할 수 있게 하는 환경입니다. `pip`가 아닌 `npm`으로 패키지를 관리한다.



### 가보자고

#### CLI 환경 만들기

CLI 설치

```bash
$ npm install -g @vue/cli
```



bash 말고 vscode terminal에서 해야 옵션 선택이 가능해서 여기서 하세요

```bash
$ vue create projectName
```

이러면 버전 선택하라 하는데 Vue 2를 선택하자. 얘가 레거시임
그리고 `cd projectName` `npm run serve`하라고 친절하게 가이드를 준다.



그렇게 깔고 나면 파일들이 막 깔리는데

* Babel
  : 컴파일러. 우리가 쓰기 쉽게 바뀐 신 JS 코드를 쓰면 컴퓨터가 알아먹게 구 JS로 변환해줌
* Webpack
  : module bundler. 모듈 간 의존성 문제를 해결하기 위한 도구래 약간 안 와닿네
* node_modules
  : 온갖 모듈 다 모여있다
* public/index.html
  : django로 치면 base.html
* src/App.vue
  : 최상위 컴포넌트
* src/components
  : 하위 컴포넌트들 작성하면 된다
* src/main.js
  : 약간... 약간 webpack이 빌드를 시작할 때 가장 먼저 불러오는 것들. Vue 전역에서 활용할 모듈들을 등록할 수 있다.



#### component 작성

##### props와 emit

컴포넌트들은 트리 모양이다. 그래서 부모-자식 관계가 당연히 생기고, 그들 간의 의사소통도 생기겠지? 그 의사소통을 props와 emit이라고 한다. **props**는 부모 &rarr; 자식에게 데이터 전달하는 거고, **emit**은 자식 &rarr; 부모에게 자신에게서 일어난 일(event)을 알리는 거다. 둘다 한쪽으로만 가능해서 단방향이다.



##### Component 작성

src/components 폴더에 vue 파일을 생성하고, `vue`를 치고 tab 키를 누르면 기본 컴포넌트 틀이 나온다.

```vue
<template>
  
</template>

<script>
export default {

}
</script>

<style>

</style>
```

여길 채우는 방법을 알아봅시다. 

★★: 컴포넌트 등록 방법
▲▲: props
♣♣: emit

```vue
<!-- App.vue (부모 컴포넌트) -->

<template>
  <!-- ※ vue CLI에서 template 안에는 단 하나만 들어갈 수 있어서 보통 <div> 하나 박고 시작한다 -->
  <div>
    <!-- ★★ 컴포넌트 등록 3단계: 템플릿에서 보여주기print 하면 끝! -->
    <!-- 템플릿에서 적을 때 통상적으로 케밥 케이스를 씁니다 -->
    <the-child></the-child>
      
    <!-- ▲▲ 2-1: 작성 컴포넌트 템플릿에서 prop-data-name="value" 형식으로 지정해준다 -->
    <!-- ▲▲ 2-2: 아님 v-bind로 부모의 data를 동적 바인딩(부모 data 업뎃되면 자식에게도 업뎃된 data 전달) -->
    <!-- 이렇게 하고 자식데이터로 가면 -->
    <the-child
      prop-data="자식에게 줄게"
      :parent-data="parentData"
    >
    </the-child>
      
    <p>childData: {{ fromChild }}</p>
    <!-- ♣♣ 5번: @1번의emitEventName="emit이들어있는methodName" 형식 해주면 끝!-->
    <!-- 이러면 이제 자식 컴포넌트에서 적은 ♣♣2번 @eventName이 발생하면 여기도 반응 -->
    <the-child @child-data="fromChild"></the-child>
      
    <!-- 그래서 최종적으로 부모에 적히는 the-child template은 emit과 prop가 합쳐진다-->
    <the-child
      prop-data="자식에게 줄게"
      :parent-data="parentData"
      @child-data="fromChild"
     >
    </the-child>
  </div>
</template>

<script>
// ★★ 컴포넌트 등록(이어주기) 1단계: 불러오기import
// py와 달리 import-from 순이다
import TheChild from "@/components/TheChild.vue"

export default {
  name: "TheParent",
    
  // ★★ 컴포넌트 등록 2단계: 등록하기register
  // 여기 components에 등록하면 된다
  components: {
    TheChild,
  },
    
  props: {
    // ▲▲ 1번: 수신할 데이터와 그 형식을 선언해준다
    propData: String,
  },
    
  // 부모의 데이터
  // 모든 컴포넌트에서 data는 함수 형태: data() { return {} } 로 써야 한다 
  data() {
    return {
      parentData: "안녕하세요 부모앱니다",
      // ♣♣ 3번: 자식에게서 받을 데이터 저장할 곳 data에 만들고
      fromChild: "",
    }
  },
  methods: {
	// ♣♣ 4번: 똑같이 methods에 이벤트 받는 행위 적어줌
    fromChild(함수라아무인자이름을써도되지만굳이그럴필요는없으므로childInput) {
      this.fromChild = childInput
      this.$emit("child-data", this.fromChild)
    }
  }
}
</script>

<style>

</style>
```

```vue
<!-- TheChild.vue -->

<template>
  <div class=border-solid-purple>
    <h1>The Child</h1>
    <!-- ♣♣ 2번: @내가 알릴 이벤트="methods에서 emit이 있는 함수 이름" 형식으로 적음 -->
    <!-- 참고: v-model로 data와 바인딩 해두면 여기서 바뀌면 emit도 바뀐 게 올라감 -->
    <!-- 이러고 부모한테 가면 -->
    <input type="text" v-model="childData" @input="childData">
    
    <!-- ▲▲ 4번: 이렇게 받을 수 있다 끝! -->
    <!-- 동적으로 바인딩이 되어있어서 부모에서 데이터가 업뎃되면 여기도 업뎃된단다 -->
    <p>parent data: {{ parentData }}</p>  <!-- 자식에게 줄게 -->
    <p>prop data: {{ propData }}</p>  <!-- 안녕하세요 부모앱니다 -->
  </div>
</template>

<script>
export default {
  name: "TheChild",
    
  // ▲▲ 3번: props에서 부모에서 받아올 데이터와 형식들을 props:에서 선언하고(data 아님!)
  props: {
    propData: String,
    parentData: String,
  },
  data() {
    return {
      childData: "",
    }
  },
  methods: {
    // ♣♣ 1번: methods에서 this.$emit("올릴 때 데이터 이름", 올릴 데이터)으로 올릴 준비를 한다
    childData() {
      // 근데 보통 이렇게 두 데이터 이름을 달리하지는 않지 굳이..?
      this.$emit("child-data", this.childData)
    }
  },
}
</script>

<style>
  .border-solid-purple {
    border: 1px solid purple;
    margin: 3px;
  }
</style>
```



## Vue Router

vue.js에서 페이지 간 이동을 위한 라이브러리!!!!!



설치 가보자고

```bash
$ vue add router
```

하면 history mode 묻는데 Y 하면 된다 history mode가 뭐냐면 HTML History API를 통해 구현하는 거라서 페이지를 다시 로드하지 않고 URL을 옮겨다닐 수 있음 배앰



그러면 생기는 게 router 폴더랑 views 폴더다. router 폴더 안에는 index.js가 들어있고 views폴더에는 예시용 HomeView.vue랑 AboutViews.vue가 있는데 갑자기 vetur가 뭐 물어보면서 App.vue에 `nav>router-link`랑 `<router-view>`를 만들어줌... 똑똑해;



router/index.js에는 라우트 관련 정보와 설정이 들어간다.

```js
// router/index.js

// 여긴 기본적으로 적힘
import Vue from 'vue'
import VueRouter from 'vue-router'

// 일단 여기다가 여기저기 이동할 view 모두 import
import HomeView from '../views/HomeView.vue'
import AboutView from '@/views.AboutView.vue'
import LottoView from '@/views/LottoView.vue'
// ../는 상위로 올라가는 거니까 여기서 src가 됨.
// 근데 vue에서 @ 자체가 src 폴더를 의미하는 거라 어떻게 적든 상관이 없다.
// 다만 @가 절대 경로니까 좀 더 나을... 듯? 

Vue.use(VueRouter)

const routes = [
  // 여기다가 등록을 해주면 된다
  {
    path: '/',				// URL
    name: 'home',			// 이름
    component: HomeView,	// URL과 이을 component
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView,
  },
  {
    path: "/lotto/:count",	// params는 :로 매핑
    name: "lotto",
    component: LottoView,
  }
]

// 여기도 생성 시 적혀있는 거
const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
```



아아 src/views 폴더에는 router로 이어진 애들을 넣는 거고 components에는 router로 이어진 vue 안에서 그 component와 매핑된 부품들이라든가... 



```vue
<!-- App.vue -->
<template>
  <div id="app">
    <!-- 바로 여기를 vetur가 해줌 -->
    <nav>
      <!-- 하지만 형식은 알아둬야겠죠 -->
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <!-- 그... url에서 다른 param는 저렇게 데려오고 기본값을 정해둘 수 있음 -->
      <!-- 쿼리(url에서 ?뒤에 오는 거)도 key:value 형식으로 가져올 수 있다 -->
      <router-link :to="{ name: 'lotto', params: { count: 6 }, query: { queryName: "something"} }">Lotto</router-link>
    </nav>
    <router-view/>
  </div>
</template>
```

 

App에서는 저렇게 하는데 다른 Vue 인스턴스 내부에서는 `$router`로 접근해야 한다.

```vue
<!-- 자식 컴포넌트 -->

<template>
  <div>
    <p>
        만약 url의 params 등을 template에 가져오고 싶다면
        {{ $route.params.count }}
    </p>  
    <h2>LottoView.vue로 가보자고</h2>
    <button @click="moveToLotto">GOGO</button>
  </div>
</template>


<script>
export default {
  // 어쩌구저쩌구...
    
  // methods에서 쓴다
  methods: {
    moveToLotto() { 
      this.$router.push({
        name: 'lotto',
        params: { count: 6 },
        query: {"queryName": "something"}
      }) 
    },
  },
}
   
</script>
```