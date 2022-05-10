<template>
  <div class="border-solid-blue">
    <h1>The Parent</h1>
    <!-- parentInputData가 2번 -->
    <!-- emitApp 3번 -->
    <input type="text" v-model="parentInputData" @input="emitApp">
    <!-- appInputData가 1번 -->
    <p>appData: {{ appInputData }}</p>
    <p>childData: {{ childInputData }}</p>
    <!-- parent-input-data 5번 -->
    <!-- @child-data 6번...의 이벤트가 일어나면 ="fromChild" 함수가 발생 -->
    <the-child :app-input-data="appInputData" :parent-input-data="parentInputData" @child-data="fromChild"></the-child>
  </div>
</template>

<script>
import TheChild from "@/components/TheChild.vue"

export default {
  name: "TheParent",
  components: {
    TheChild,
  },
  props: {
    // 1번
    appInputData: String,
  },
  data() {
    return {
      // 얘 2번
      parentInputData: "",
      childInputData: "",
    }
  },
  methods: {
    // 3번
    emitApp() {
      // parent-data 4번... 이벤트 이름임ㅇㅇ
      // 넘겨줄 데이터 이름을 넣어준다(2번)
      this.$emit("parent-data", this.parentInputData)
    },
    fromChild(childInput) {
      this.childInputData = childInput
      // 얘는 7번... 인데 굳이 6번과 다를 필요는 없음 어차피 거쳐서 올리는 곳이라
      this.$emit("child-data", this.childInputData)
    }
  }
}
</script>

<style>
  .border-solid-blue {
    border: 1px solid blue;
    margin: 3px;
  }
</style>