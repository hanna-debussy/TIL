<template>
  <div class="mb-5">
    <h2 class="mb-2">My Movie List</h2>
    <input type="text" v-model.trim="movieTitle" @keyup.enter="createMyMovie" class="me-1">
    <button @submit="createMyMovie" class="btn btn-primary btn-sm">Add</button>
  </div>
</template>

<script>
export default {
  name: 'WatchListForm',
  data() {
    return {
      movieTitle: "",
    }
  },
  methods: {
    createMyMovie() {
      const newMyMovie = {
        title: this.movieTitle,
        watched: false,
        date: new Date().getTime(),
      }
      this.$store.dispatch("createMyMovie", newMyMovie)
      this.movieTitle = ""
    }
  }
}
</script>

<style>
</style>