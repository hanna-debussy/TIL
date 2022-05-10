# Vue CLI & Vue Louter

## Vue CLI

```bash
# 설치
$ npm install -g @vue/cli

# 프로젝트 생성
$ vue create project-name
# 하면 버전 선택이 나와 거기서 우리는 2 선택

$ cd project-name
$ npm run serve
```



Vetur라는 extensions를 깔았다면 `vue`하고 엔터 치면 기본 틀이 나온다

그래서 src/components에 새 vue를 만들었다면 해당 vue와 src의 App.vue에서 1 불러오기 2 등록하기 3 보여주기 를 해줘야 한다.

```vue
<!-- App.vue, 즉 부모 component -->


<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    
    <!-- 보여주기Print -->
    <ComponentName my-message="CamelCase"/> <!-- 한 번 쓰고 슬래시 필요 -->
    <!-- 위는 카멜 케이스, 아래는 케밥 케이스라고 한다. 둘다 똑같은 걸 가리킴 -->
    <component-name my-message="kebab-case"></component-name>
      
    <!-- bind해야 JS 표현식으로 해서 JS data로 보낼 수 있다 안하면 걍 str 취급 -->
    <the-about my-message="parentData"></the-about>
    <the-about :my-message="parentData"></the-about>
    <!-- 자식이 부르는 소리를 듣게 귀 뚫어주기 -->
    <the-about :my-message="parentData" v-on:signal-to-parent="onParent"></the-about>
  </div>
</template>

<script>
// 1. 불러오기Import
import 통상적으로ComponentName from './components/ComponentName'

export default {
  name: 'App',

  // 2. 등록하기Register
  components: {
      ComponentName,
      // 'template에서부를이름: 컴포넌트이름' 으로 써도 된다
  },
    
  // data는 반드시 function의 모양을 해야 한다
  data: function() {
    return {
      parentData: "This is parent data to child component",
    }
  },
    
  methods: {
    onParent: function() {
      // inputData가 자식이 보낸 '그' 데이터
      console.log("그래 자식아;", inputData)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

```

```vue
<!-- ComponentName.vue, 즉 자식 component -->


<template>
    <div>
    <h1>ComponentName.vue</h1>
    <h2>{{ myMessage }}</h2>
    <p>template 안에는 하나밖에 못 써서 div 안에 전부 넣어줘야 한다!</p>
    <input
      type="text"
      v-model="childInputData"
      @keyup.enter="childInputChange"
    >

  </div>

</template>

<script>
// 여기서는 camel case로만 적어야 한다 kebab하면 '-'를 minus 처리하기 때문
export default {
  // name: template에서 얘를 뭐라고 지칭할 건지 - <name></name>
  name: "ComponentName",
    
  // props: 수신할 데이터 선언하는 곳
  props: {
    // 형식 선언
    myMessage: String,
  }
    
  // 마찬가지로 data는 function의 모양
  data: function() {
    return {
      childInputData: "",
    }
  },

  // 부모를 불러보자고
  methods: {
    childInputChange: function() {
      console.log("이벤트(enter) 발생", this.childInputData)
      // 부모 부르는 이름이 첫번째 인자, 케밥 케이스로 써야 한다
      // 자식 데이터도 넘기기 쌉가넝 두 번째 인자로 넘기면 된다
      this.$emit("signal-to-parent", this.childInputData)
    },
  },

}
</script>

<style>

</style>
```



## Pass Props & Emit Events

Pass Props: 부모가 자식에게 데이터를 주는 것
Emit Evnets: 자식이 부모에게 데이터를 주는 것 (나에게 일어난 일을 메시지로 전달)

부모가 자식 이상의 손자(?)에게나, 자식이 부모 이상의 조상에게 데이터를 넘기는 건 불가능하다.



## Vue Router

라우트에서 컴포넌트를 매핑한 후, 어떤 주소에서 렌더링할 지 알려줌
...? 일단 가보자



```bash
# router라는 plugin을 설치해줘야 한다
$ vue add router

? Use history mode for router?
Y
```

하면 main.js의 new Vue에는 router가 등록되고 src 안에는 router라는 폴더가 생긴다. 쏘 스맕

component와 달리 views에는 router와 관련된 vue들이 들어가고, 보통 `ㅁㅁView.vue`의 이름을 가진다.



```js
// index.js
// 건들지 않는 기본틀 제외


// views가 index가 들어있는 router 폴더 상위 폴더인 src에 있으므로 ../로 갈 수 있다
import LunchView from '../views/LunchView.vue'
// 아니면 src 폴더 자체를 '@'라고 표현하기도 한다 오직 vue에서만! 다른 데서는 못 알아먹음
import LottoView from '@/views/LottoView.vue'


const routes = [
  {
    // URL
    path: "/url-name",
    
    // 별명
    name: "name",

    // 어떤 component와 매핑되는지
    component: NameView,
  },
  {
    // :ㅁㅁ해두면 ㅁㅁ란 이름으로 데이터가 연결이 된다 이말이야 
    path: "/lotto/:count",
    name: "lotto",
    component: LottoView,
  }
]

```

```vue
<!-- App.vue -->


<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <!--
		{% url %}의 역할을 하는 게 바로 router-link다.
		:to=로 갈 수 있고 데이터라는 걸 알려주기 위해 {}안에 넣는다
		주소의 다른 변수는 params에서 꺼내온다
	  -->
      <router-link :to="{ name: 'lunch' }">Lunch</router-link> |
      <router-link :to="{ name: 'lotto', params: { count: 6 } }">Lotto</router-link>
    </nav>
    <!-- div 안에 넣어주는 게 국룰 -->
    <div class="container">
      <router-view/>
    </div>
  </div>
</template>
```



```vue
<!-- ㅁㅁView.vue -->



<template>
  <div>
    <h1>{{ data 속 값들을 불러올 때 }}</h1>
    <div>
      <h2>{{ luckyNumbers }}</h2>
      <button @click="pickLotto">pick</button>
      <button @click="moveToAnotherPage">another page</button>
    </div>
  </div>
</template>

<script>
// lodash는 이렇게 불러온다
import _ from "lodash"

export default {
  name: "ㅁㅁView",
  data () {
    return {
      // url의 변수는 this.$route.params.로 가져올 수 있다
      count: this.$route.params.count,
      luckyNumbers: [],
    }
  },
  methods: {
    pickLotto() {
      // const count = this.$route.params.count 여기서 이렇게 불러줘도 가능
      const numbers = _.range(1, 46)
      this.luckyNumbers = _.sampleSize(numbers, this.count)
    },
    moveToAnotherPage() {
      // $route 아님 $router임...
      // $router.push({})를 통해 다른 View로 보낼 수 있다
      this.$router.push({ name: "lotto", params: { count: 6 }})
      // or template에서 louter-link로 하거나
    },
  },
  created() {
    this.pickLotto()
  }
}
</script>

<style>

</style>
```



