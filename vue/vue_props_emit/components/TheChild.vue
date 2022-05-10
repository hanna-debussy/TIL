<template>
  <div class=border-solid-purple>
    <h1>The Child</h1>
    <input type="text" v-model="childInputData" @input="childInputDataChange">
    <p>appData: {{ appInputData }}</p>
    <!-- 5번 -->
    <p>parentData: {{ parentInputData }}</p>
    <p>childData: {{ childInputData }}</p>
  </div>
</template>

<script>
export default {
  name: "TheChild",
  props: {
    // 5번
    parentInputData: String,
    appInputData: String,
  },
  data() {
    return {
      childInputData: "",
    }
  },
  methods: {
    childInputDataChange() {
      // child-data 6번
      this.$emit("child-data", this.childInputData)
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