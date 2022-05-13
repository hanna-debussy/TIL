# Vuex

## 뷱스요? (아닙니다)

애플리케이션의 모든 컴포넌트에 대한 중앙 집중식 저장소 역할!

원래는 컴포넌트들이 독립적으로 데이터를 관리하고 부모&rarr;자식 으로 전달만 가능하고 거꾸로 하려면 똑똑 이벤트 일어났습니다 햄 했어야 했음 이건 넘모... 후지잖아 우우

**그래서!**

중앙 저장소에 state(data)를 모아놓고 관리하자는 것
컴포넌트 중첩이 깊은 프로젝트에 매우 효율적이다. 왜냐면 각 컴포넌트에서는 중앙 저장소만 보면 되니까. 그리고 동일한 state를 공유한다면 중앙 저장소에서 한 번만 바꿔도 모든 다른 컴포넌트들이 동기화되기 때문에 체고



## 핵심 컨셉

![Uni-directional data flow with Vuex | by Colin Fallon | Medium](https://miro.medium.com/proxy/1*tGpsJzS-qp80-Z6JVrOoCA.jpeg)

1. State
   : 데이터라 생각하면 된다. mutations을 거치면 데이터가 변경되겠지
2. Mutations
   : 데이터를 변경하는 유일한 방법. actions 중에서 `commit()`으로 실행된다.
3. Actions
   : 함수. 모든 건 함수로 움직이니까 걍 모든 행동이라 생각하면 된다(만능 but state 직접 변경은 불가(이걸 mutation이 하능고)). **context**인자를 받는다. 
4. Getters
   : state에서 컴포넌트를 통해 화면에 보낼 때 계산해주는 거. 약간 computed와 비슷하다. data를 변경하지 않고 계산해주는 거임... 



## 실제로 가보자고

vuex는 내장된 게 아니다

```bash
$ vue add vuex
```

그러면 store 폴더와 그 안에 index.js가 생긴다. 

일단 각종 삼대 vue를 만들어보자 그리고 밑에 index.js 보면서 맞춰봅시다

```vue
<!-- GrandParent.vue -->

<template>
  <div>
    Grandpa Grandma
    <p>
      <!-- mapGetters로 가져오면 getters 이름 그대로 가져올 수 있다 -->
      getters에서 계산된 걸 가져오면: {{ completedDataCount }}
    </p> 
    <component-name></component-name>
    <child-vue></child-vue>
  </div>
</template>

<script>
import ComponentName from '@/components/ComponentName.vue'
import ChildVue from '@/components/ChildVue.vue'

// map 붙이면 다 가져올 수 있구먼
import { mapGetters } from "vuex"

export default {
  name: "Grand",
  components: {
    ComponentName,
    ChildVue,
  },
  computed: {
    ...mapGetters([
      "completedDataCount",
      "uncompletedDataCount",
      "totalDataCount",
  	])
  },
}
</script>

<style>

</style>
```

```vue
<!-- ComponentName.vue -->

<template>
  <div>
    <!-- computed 안 쓰고 $store로 바로 접근이 가능하기도 함 당연함... -->
    <!-- key도 겹치지 않는 걸로 꼭 필요 -->
    <child-vue
      v-for="data in computedDataName"
      :key="data.date"
      :propsName="propsName"
    ></child-vue>
  </div>
</template>

<script>
import ChildVue from '@/components/ChildVue.vue'   
 
export default {
  name: "ComponentName",
  components: {
    ChildVue,
  },
  computed: {
    computedDataName() {
      return this.$store.state.dataName
    },
    // 아니면 import { mapState } from 'vuex' 적고 ...mapState(["todos"]),
  }
}
</script>

<style>

</style>
```

```vue
<!-- ChildVue.vue-->

<template>
  <div>
    <!-- 제목을 누르면 isCompleted를 갱신하고 싶어 그리구 했다면 취소선 그을래 -->
    <span
      @click="updateData(propsnName)"
      :class="{'is-completed': propsName.isCompleted}"
    >{{ propsName.title }}</span>
    <!-- deleteData 해주시고 propsName 데이터도 넘겨주세요 -->
    <button @click="deleteData(propsName)">
        삭제빵
    </button>
  </div>
</template>

<script>
export default {
  name: "ChildVue",
  props: {
    propsName: Object,
  },
  methods: {
    deleteData() {
      // store에서 두 번째 인자를 삭제해달라고 action에 부탁하기 (직접 삭제 아님)
      this.$store.dispatch("deleteData", this.propsName)
        
      // 근데 이거 인셉션 아니에요? 그냥 바로 index.js actions에 있는 거 꺼내면 않되요?
      vuex.mapActions(["deleteData", 등등]).deleteData
      // 아니면 methods 안에 deleteData: vuex. ... .deleteData 해놓고 모든 함수가 접근 가능하게 써도 됨
        
      // ...아니면! mapActions에 vuex. 를 일일이 붙이고 다니는 게 귀찮다면 script 제일 상단에 import { mapActions } from 'vuex'라고 해도 된다... 필요한가?
    },
  },
    
  // 아니면 더 킹받게 확 줄이려면
  methods: {
    // ... 쓰는 이유는 다른 내가 만든 methods들 가져오기 위해... args 들고오는 거 ㅇㅇ
    // import { mapActions } from 'vuex' 하고
    ...mapActions(["createDataMethod", "deleteData", "updateData"]),
    myMethods() {
      // 내가 만든 어쩌구저쩌구
    },
  },
}
</script>

<style>
  .is_completed {
    text-decoration: line-through;
  }
  div {
    border: 2px solid blue;
  }  
</style>
```

여기에는 추가하는 vue도 만들어보자

```vue
<!-- CreateForm.vue -->

<template>
  추가 맨
  <!-- .trim을 저기 넣는 것처럼 js를 여기서 걸 수도 있다 -->
  <input type="text" v-model.trim="inputTitle" @keyup.enter="createData">
</template>

<script>
export default {
  name: "CreateForm",
  data() {
    return {
      inputTitle: "",
    }
  },
  methods: {
    createData() {
      // 우리가 넘겨줄 데이터 정의해주고
      const newData = {
        title: this.inputTitle,
        isCompleted: false,
        date: new Date().getTime(),
      }
      // vuex index.js에 actions에 있는 함수를 가져오는 게 바로 'dispatch'
      // this. 넣어주시고요
      // 두번째 인자로 우리가 넘길 데이터 넣어주긔
      this.$store.dispatch("createDataMethod", newData)
      // 넘기고 나서도 input에 남아있는 newData를 걍 빈칸으로 해서 없애줍시다
      this.inputTitle = ""
    }
  }
}
</script>

<style>

</style>
```



그리고 여기가 그 store/index.js

```js
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {		// data
    // 여기에 우리 database를 만드는 셈
    dataName: [
      // 당빠 비워둬도 되지
      { title: "one", isCompleted: true, date: new Date().getTime() },
      { title: "two", isCompleted: false, date: new Date().getTime() },
    ],
  },
  getters: {		// computed
    completedDataCount(state) {
      return state.dataName.filter(oneData => {
        return oneData.isCompleted
      }).length
    },
  },
  mutations: {	// change
    // 오 강조의 의미로 보통 생성 함수를 대문자로 쓴다나봐
    // newData는 actions에서 우리가 createDataMethod를 통해 넘어온 데이터
    CREATE_DATA(state, newData) {
      // push가 data 추가하는 유일한 방법...인데! this.는 쓰지 않는다
      // 항상 state 자체를 첫번째 인자로 가져오기 때문(그러니까 인자에 state 늘 쓰시길,,,)
      state.dataName.push(newData)
    },
      
    // ㅇㅇ삭제해줄게
    DELETE_DATA(state, deleteItem) {
      const index = state.dataName.indexOf(deleteItem)  // 여기는 js 부분
      // splice라고 첫 번째 인자 index에서부터 (두 번째 인자)개를 지우는 게 있어
      state.dataName.splice(index, 1)
    },
      
    // ㅇㅇ업뎃해줄게
    UPDATE_DATA(state, oldData) {
      state.dataName = state.dataName.map(oneData => {
        // 데이터들 중에 해당하는(일치하는) 데이터라면
        if (oneData === oldData) {
          // 박궈 박궈
          oneData.isCompleted = !todo.isCompleted
        }
        return oneData
      })
    }
  },
  actions: {		// methods
      
    // context 꼬옥 넣어주면 되,
    createDataMethod(context) {
      // context가 모든 곳에 접근이 가능한 만능맨이기 때문에 context.로 실행한다
      context.commit("CREATE_DATA")
      // ...로 쓰거나 1
        
      const { commit } = context
      commit("CREATE_DATA")
      // ...로 쓰거나 2
    },
        
    // 이렇게 초간지로 쓸 수도 있다 3
    createDataMethod({ commit }, newData) {
      // 여기에 나머지 필기할게
      // data를 CREATE_DATA에 같이 넘겨주기 위해 두 번째 인자로 쏘옥
      commit("CREATE_DATA", newData)
    },
    
    // 삭제빵
    deleteData({ commit }, deleteItem) {
      // mutation아 함만 해조
      commit("DELETE_DATA", deleteItem)
    },
      
    // 업뎃
    updateData({ commit }, oldData) {
      commit("UPDATE_DATA", oldData)
    },
    
    
  },
})
```



## 새고를 해도 남아있는 견고함

지금까지 만든 건 새로고침을 하면 여태 만들었던 데이터가 날아간다. 어데갔으묘? 그래서 해야 하는 게 `localStorage`를 써야 한다.

```js
// 데이터를 새고해도 날아가지 않게 스토리지에 저장을 하자고
  
  mutations: {
    LOAD_DATA(state) {
      // 진짜 로드하기 위해 파싱 해주기
      const dataString = localStorage.getItem("dataName")
      state.dataName = JSON.parse(dataString)
    }
  }

  actions: {
	saveData({ state }) {
      const jsonData = JSON.stringfy(state.dataName)
      localStorage.setItem("dataName" jsonData)
    },
        
    createDataMethod({ commit, dispatch}, 어쩌구) {
      // 저쩌구
      dispatch("saveData")
    }
    // delete에도, update에도, ...
  }
```

```vue
<!-- App.vue -->

<script>
import { mapMutations } from "vuex"
    
// ...어쩌구
  methods: {
	...mapMutations(["LOAD_DATA"]),
  },
  created() {
    this.LOAD_DATA()
  }
</script>


```



근데 항상 라이브러리가 해내죠?

```bash
$ npm i vuex-persistedstate
```

```js
<!-- store/index.js -->

import createPersistedState from 'vuex-persistendstate'

// Store 넣고
export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  // 나머지 원래 것들 붙여넣기
})
```

이러면 vue들에서 저 위에 했던 짓들 다 안 해도 됨 cool~
