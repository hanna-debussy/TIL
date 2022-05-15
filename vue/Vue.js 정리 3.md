# Vue.js 정리 3

## Vuex

Statement management pattern + Library for vue.js 상태 관리 패턴 + 라이브러리
: state(상태)를 전역 저장소로 관리할 수 있도록 지원하는 라이브러리

애플리케이션의 모든 컴포넌트에 대한 중앙 집중식 저장소라고 볼 수 있다. props는 부모 &rarr; 자식의 흐름에게만, emit은 데이터가 아닌 이벤트를 알리는 형식이었지만 만약 컴포넌트들 간에 중첩이 넘 많아지면 에바킹이 됨... 하지만 vuex에서는? 모든 데이터가 한 곳(store, 중앙 저장소)에 있어서 모두가 그 곳에서 바로 데이터를 가져올 수 있다. 그러면 우리는 state만 신경 쓰면 되니까 굿



## Core Concepts of Vuex

vuex는 네 가지로 이루어져있다: State, Mutations, Actions, Getters



### State

state는 곧 data다. 여러 컴포넌트 내부에 있는 데이터들을 중앙에서 관리하게 된다. 원본 소스가 되고 앱 하나에 하나의 저장소뿐이다. 또 state가 변하면 해당 state를 참조하고 있는 모든 컴포넌트들에게도 그게 전달되니까 굿



### Mutations

실제로 state를 변경하는 유일한 방법. 반드시 동기적이어야 한다... 추적할 수 없다나 뭐라나... 콜백함수 형태로 바로 부를 수 있는 게 아니라 actions에서 `commit()` 메서드에 의해서 호출된다.



### Actions

데이터 고치는 mutations역할 외의 모든 함수가 들어가있다 생각하면 된다. 이렇게 나눈 이유는 명확하게 나누면 서비스 규모가 커져도 state 관리가 용이하게 하기 위해서다. 비동기 작업도 쌉파서블. 컴포넌트에서 `dispatch()` 메서드에 의해 호출된다.



### Getters

computed와 비슷하다. state를 변경하지 않고 그를 활용해서 계산을 해주는 곳. computed와 비슷하다보니 얘도 캐싱이 되어있다가 state가 변경되면 그때만 계산을 다시 한다.



## 실제로 해보자

```bash
$ vue add vuex
```

하면 가끔 commit 여부를 물어본다. 앱이 이미 조금 만들어져있다가 깔면 까는 동시에 바뀔 수 있는 부분이 몇 있어서 그 전 상태를 commit 할 건지를 묻는 건데 보통 Yes라고 하지

그러면 src/store 폴더가 생기고 그 안에 index.js가 생긴다. 여기서 vuex core concept가 작성되는 것

```js
// src/store/index.js

export default new Vuex.Store({
  state: {
    // 여기에 하던대로 dictionary in list 형태로 데이터를 적으면 된다
    dataNames: [
      // 어쩌구
    ],
    [
      // 저쩌구
    ]
  },
  
  mutations: {
    // 보통 all capital로 쓰더라고
    CREATE_DATA(state, newItem) {	// mutations는 항상 state를 첫 번째 인자로 가진다
      state.dataNames.push(newItem)	// new data 생성은 push로
    },
    // 이렇게 만들고 나면 접근 가능해지게 actions에 함수 적어줘야 한다
    
    DELETE_DATA(state, oldItem) {
      const index = state.dataNames.indexOf(oldItem)
      // splice 자체가 어느 index에서 n개를 지우는 거라 그 아이템의 index가 필요해서 이렇게 쓴다
      state.dataNames.splice(index, 1)
    },
      
    UPDATE_DATA(state, nowItem) {
      state.dataNames = state.dataNames.map(dataName => {
        if (dataName == nowItem) {
          return {
            key1: nowItem.key1
			date: new Date().getTime()            
          }
        } else {
          return nowItem
        }
      }),
    }
  },
    
  actions: {
    createData(context, newItem) {				// actions는 항상 첫 번째 인자로 context
      context.commit("CREATE_DATA", newItem)	// commit으로 mutations 불러오기
      // context는 일종의... 맥가이버라고 보면 된다
      // 오 dispatch()로 다른 actions도 호출 가넝한
    },
      
    // 근데 context 내의 commit과 내가 부를 게 이름이 같다면 우리가 또 {}로 줄일 수 있으니까 보통
    createData({ commit }, newItem) {
      commit("CREATE_DATA", newItem)
    },
    // 형식으로 적는다
    deleteData({ commit }, oldItem) {
      commit("DELETE_DATA", oldItem)
    },
	updateData({ commit }, nowItem) {
      commit("UPDATE_DATA", nowItem)
    }
  },
      
  getter: {
	dataCount(state) {
      return state.daNamtes.length
    }
  },
})
```

그러고 나면 state는 다른 컴포넌트에서 `$store.state`로 접근 가능해지고, actions는 methods에서 `$store.dispatch()`로 가져올 수 있으며 mutations도 actions에서 불러오니까 같이 ㅇㅇ

```vue
// component.vue

<template>
  <div>
    {{ dataCount }}	<!-- computed 당연히 바로 이렇게 접근 가능 -->
    <another-component
      v-for="dataName in dataNames"
      :key="dataName.date"
    >
    </another-component>
  </div>
</template>

<script>

export default {
  // 어쩌구
    
  computed: {
    // 여기서 state 소환
    dataNames: function() {
      return this.$store.state.todos  // this.가 들어가야 한다
    },
    // 여기서 getters 소환
    dataCount() {
      return this.$store.getters.dataCount	// 계산된 '값'이니까 () 노필요
    }
  },
    
  methods: {
    // 여기서 actions 소환
    createData() {
      this.$store.dispatch("createData", this.dataName) // 부를 함수랑 그 함수에게 보낼 데이터
    }
    ... 등등
  },
    
  computed: {

  }
}
</script>
```



근데 또... 개발자들 귀찮은 거 싫어하죠? 바로 index.js에서 가져올 생각을 합니다
: `mapState`, `mapGetters`, `mapActions`, `mapMutations`



```vue
<script>
// 일단 이렇게 가져와주고
import { mapState, mapGetters, mapActions, mapMutations } from "vuex"
    
...
computed: {
  // mapState
  ...mapState(["dataNames", ]),
  // getters
  ...mapGetters(["dataCount", ])
  otherComputedData() {},
},
methods: {
  // actions
  ...mapActions(["createData", "deleteData", "updateData"])
}

</script>
```



### 로컬 스토리지 사용하기

이렇게 다 만들고 나서 데이터 입력하고 다 잘 움직이는데... 새로 고침을 하면? 그 데이터가 다 날아간다 이 말이에요. 그래서 이걸 로컬 스토리지에 담아서 그대로 남아있을 수 있도록 해보자



```bash
$ npm i vuex-persistedstate
```



```js
// src/store/index.js

import createPersistedState from "vuex-persistedstate"

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ] 
})

```