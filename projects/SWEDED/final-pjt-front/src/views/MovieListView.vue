<template>
  <div class="col-10 offset-1 text-white">
    <div class="m-5"><img src="@/assets/sweded.png" alt="logo" style="width: 150px;"></div>
    <p class="mb-3 h3 text-left">요즘 뜨는 신작들</p>
    <div class="row row-cols-6 mb-5">
      <div class="col mb-4" v-for="movie in movies" :key="movie.pk">
        <div class="card bg-dark hover-shadow">
          <router-link :to="{ name: 'movieDetail', params: {moviePk: movie.movie_id} }">
            <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" class="card-img" :alt="`${movie.title}`">
            <div class="card-img-overlay shadow d-flex align-items-end justify-content-center">
              <h5 class="card-title text-light shadow-text font-weight-bold text-truncate mb-3">{{ movie.title }}</h5>
            </div>
          </router-link>
        </div>        
      </div>
    </div>
    <p class="mb-3 h3 text-left">평점이 높은 작품들</p>
    <div class="row row-cols-6">
      <div class="col mb-4" v-for="movie in top_movies" :key="movie.pk">
        <div class="card bg-dark hover-shadow">
          <router-link :to="{ name: 'movieDetail', params: {moviePk: movie.movie_id} }">
            <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" class="card-img" :alt="`${movie.title}`">
            <div class="card-img-overlay shadow d-flex align-items-end justify-content-center">
              <h5 class="card-title text-light shadow-text font-weight-bold text-truncate mb-3">{{ movie.title }}</h5>
            </div>
          </router-link>
        </div>        
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'MovieListView',
  components: {},
  computed: {
    ...mapGetters(['movies', 'top_movies'])
  },
  methods: {
    ...mapActions(['setMovies',]),
    
  },
  created() {
    this.setMovies()
  }
}
</script>

<style>
  .hover-shadow {
    transition: all ease .5s;
  }

  .hover-shadow:hover {
    transform: scale(1.07);
  }

  .shadow {
    transition: all ease .5s;
    background: rgba(0, 0, 0, 0.5);
    opacity: 0;
  }

  .shadow:hover {
    opacity: 1;
  }

  .shadow-text {
    opacity: 0;
    transition: all ease .5s;
  }

  .shadow:hover .shadow-text {
    opacity: 1;
  }
</style>