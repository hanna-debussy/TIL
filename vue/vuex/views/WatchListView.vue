<template>
  <div class="watchlistcontainer">
    <watch-list-form></watch-list-form>
    <ul class="list-group">
      <watch-list-item
        v-for='movie in myMovies'
        :key='movie.id'
        :movie='movie'
      >
      </watch-list-item>
    </ul>
  </div>
</template>

<script>
import WatchListItem from '../components/WatchListItem.vue'
import { mapState } from 'vuex'
import WatchListForm from '../components/WatchListForm.vue'

export default {
  name: 'WatchList',
  components: {
    WatchListItem,
    WatchListForm,
  },
  computed: {
    ...mapState(['myMovies'])
  }
}
</script>

<style>
  .watchlistcontainer {
    width: 1000px;
    margin: 0 auto;
  }
</style>