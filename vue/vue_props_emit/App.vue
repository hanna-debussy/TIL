<template>
  <div id="app" class="border-solid-lightskyblue">
    <h1>App</h1>
    <input type="text" v-model="appInputData">

    <p>parentData: {{ parentInputData }}</p>
    <p>childData: {{ childInputData }}</p>
    <!-- app-input-data가 TheParent의 1번 -->
    <!-- @parent-data가 TheParent의 4번 이벤트...가 일어나면 fromParent발생 -->
    <!-- child-data는 7번 -->
    <the-parent :app-input-data="appInputData" @parent-data="fromParent" @child-data="fromChild"></the-parent>
  </div>
</template>

<script>
import TheParent from '@/components/TheParent.vue'

export default {
  name: 'App',
  components: {
    TheParent,
  },
  data() {
    return {
      // 여기 1번
      appInputData: "",
      parentInputData: "",
      childInputData: "",
    }
  },
  methods: {
    fromParent(parentInput) {
      this.parentInputData = parentInput
    },
    fromChild(childInput) {
      this.childInputData = childInput
    }
  },
}
</script>

<style>
.border-solid-lightskyblue {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  border: 1px solid lightskyblue;
}

</style>
