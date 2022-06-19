<template>
  <div class="col-10 offset-1 text-white row mt-3">
    <div class="col-12 text-left mb-5">
      <router-link :to="{ name: 'home'}">
        <button class="btn btn-light btn-sm">BACK</button>
      </router-link>
    </div>
    <div class="border-bottom col-12 row pb-5">
      <div class="col-4">
        <h1 class="m-4 font-weight-bold text-warning mb-5">{{ movie.title }}</h1>
        <div>
          <p class="h4">{{ currentUser.username }}님은 <span class="text-warning">{{ newScore }}</span> 점을 남기셨습니다</p>
          <movie-rate-form action="update" @rated="rated"></movie-rate-form>
        </div>
        <div class="mt-3 text-left">
          <p>개봉일: {{ movie.release_date }}</p>
          <p>평점: {{ movie.vote_average }}</p>
          
          <p class="mb-5 text-warning">장르: 
            <span v-for="genre in movie.genres" :key="genre.pk">{{ genre.name }} </span>
          </p>
          <p>{{ movie.overview }}</p>
        </div>
      </div>
      <div class="col-4 offset-4">
        <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" class="w-75" :alt="`${movie.title}`">
      </div>
    </div>

    <div class="col-12 text-left mt-5">
      <h2 class="col-12">이런 영화는 어떠세요?</h2>
      <div class="row row-cols-6">
        <div class="col mb-4" v-for="movie in recommended_movies" :key="movie.pk">
          <div class="card bg-dark hover-shadow">
            <a :href="`http://localhost:8080/movies/${movie.movie_id}`">
              <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" class="card-img" :alt="`${movie.title}`">
            </a>
          </div>        
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MovieRateForm from '@/components/MovieRateForm.vue'

export default {
  name: 'movieDetail',
  components: { MovieRateForm },
  data() {
    return {
      moviePk: this.$route.params.moviePk,
      imRated: false,
      isEditing: false,
      newScore: 0,
      oldScore: 0,
    }
  },
  computed: {
    ...mapGetters(['movie', 'is_rated', 'currentUser', 'recommended_movies', 'score']),
    isRated() {
      return this.is_rated[0]['is_rated'] | this.newScore != this.oldScore
    },
  },
  methods: {
    ...mapActions(['fetchMovie', 'createScore', 'updateScore', 'fetchIsRated', 'fetchRecommendations']),
    rated(score) {
      this.newScore = score
    },
    firstSetting() {
      this.oldScore = this.is_rated[1][0]['score']
      this.newScore = this.is_rated[1][0]['score']
    }
  },
  created() {
    this.fetchMovie(this.moviePk)
    this.fetchIsRated(this.moviePk)
    this.fetchRecommendations(this.currentUser.username)
    this.firstSetting()
  },
}
</script>

<style>

</style>
