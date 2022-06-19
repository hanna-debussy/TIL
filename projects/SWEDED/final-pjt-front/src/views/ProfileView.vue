<template>
  <div class="text-light col-10 offset-1">
    <div class="m-3">
      <span class="h1 text-warning">{{ profile.username }} </span><span class="h5"> 님의 프로필</span>
    </div>
    <div class="m-5">
      총 게시물 <span class="text-warning">{{ profile.articles.length }}</span>개 | 
      본 영화들 <span class="text-warning">{{ profile.rated_movies.length }}</span>개
    </div>
    <div class="row">
      <div class="col-6">
        <h4 class="mb-5">내가 쓴 게시글</h4>
        <table class="table table-dark">
          <tbody>
            <tr v-for="article in profile.articles" :key="article.pk">
              <td class="text-left text-truncate">
                <router-link
                  :to="{ name: 'articleDetail', params: {articlePk: article.pk} }"
                  class="text-light d-block"
                >
                  {{ article.title }}
                </router-link>
              </td>
              <td>
                {{ article.created_at }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="col-6 row">
        <h4 class="mb-5 col-12">내가 평가한 영화</h4>
        <div class="col-4" v-for="movie in profile.rated_movies" :key="movie.pk">
          <div class="card">
            <router-link :to="{ name: 'movieDetail', params: {moviePk: movie.movie.movie_id} }">
              <img :src="`https://image.tmdb.org/t/p/w500${movie.movie.poster_path}`"  class="card-img" :alt="`${movie.movie.title}`">
            </router-link>
          </div>
        </div>
      </div>
    </div>
    
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters(['profile'])
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>

<style>

</style>