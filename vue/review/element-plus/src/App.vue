<template>
  <!-- <button type="success" @click="increase">default</button> -->
  <div>{{ numbers }}</div>
</template>

<script lang="ts">
import { defineComponent, ref } from "@vue/runtime-core";

export default defineComponent({
  name: "App",
  components: {},
  setup() {
    const numbers = ref(0);

    const increase = () => {
      numbers.value = numbers.value + 1
    }
    return {numbers, increase}
  }
})
</script>

<style>

</style>