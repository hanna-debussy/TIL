<template>
  <li class="list-group-item movielist">
    <label :for="`checkbox-${movie.date}`">
      <input
        type="checkbox"
        :id="`checkbox-${movie.date}`"
        @change="updateWatched(movie)"
        :checked="movie.watched? true : false"
        class="form-check-input me-1"
      >
      {{ movie.title }}
    </label>
    <button @click="deleteMyMovie(movie)" class="deletebtn btn btn-warning btn-sm">X</button>
  </li>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'WatchListItem',
  props: {
    movie: Object,
  },
  methods: {
    ...mapActions(["createMyMovie", "deleteMyMovie", "updateWatched"]),
  },
  computed() {
    
  }
}
</script>

<style>
  .movielist {
    /* display: flex; */
    width: 100%;
    margin: 0 auto;
  }
  .movielist:hover {
    background-color: #eee;
  }
  .deletebtn {
    position: absolute;
    right: 20px;
  }
</style>