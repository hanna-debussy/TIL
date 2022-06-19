// import router from '@/router'
import drf from '@/api/drf'
import axios from 'axios'


export default {
  state:{
    movies: [],
    top_movies: [],
    movie: {},
    is_rated: {},
    recommended_movies: [],
  },
  getters: {
    movies: state => state.movies,
    top_movies: state => state.top_movies,
    movie: state => state.movie,
    score: state => state.movie.scores,
    is_rated: state => state.is_rated,
    recommended_movies: state => state.recommended_movies,
  },
  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_TOP_MOVIES: (state, top_movies) => state.top_movies = top_movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_MOVIE_RATE: (state, scores) => state.movie.scores = scores,
    SET_IS_RATED: (state, is_rated) => state.is_rated = is_rated,
    SET_RECOMMENDED_MOVIES: (state, recommended_movies) => state.recommended_movies = recommended_movies,
  },

  actions: {
    setMovies({ commit, getters }) {
      axios({
        url: drf.movies.movies(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then((res) => {
          commit('SET_MOVIES', res.data[0])
          commit('SET_TOP_MOVIES', res.data[1])
      })
        .catch(err => console.log(err))
    },
    fetchMovie({ commit, getters }, moviePk) {
      axios({
        url: drf.movies.movie(moviePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE', res.data)
        })
        .catch(err => {
          console.error(err.response)
          // if (err.response.status === 404) {
          //   router.push({ name: 'NotFound404' })
          // }
        })
    },

    fetchIsRated({ commit, getters }, moviePk) {
      axios({
        url: drf.movies.isMovieRated(moviePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_IS_RATED', res.data)
        })
        .catch(err => console.error(err.response))
    },

    fetchRecommendations({ commit, getters }, username) {
      axios({
        url: drf.movies.getRecommendation(username),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_RECOMMENDED_MOVIES', res.data)
        })
        .catch(err => console.error(err.response))
    },


    createScore({ commit, getters }, { moviePk, score }) {
      const newScore = { score }

      axios({
        url: drf.movies.movieRate(moviePk),
        method: 'post',
        data: newScore,
        headers: getters.authHeader,
      })
        .then(res => {

          commit('SET_MOVIE_RATE', res.data['score'])
        })
        .catch(err => console.error(err.response))
    },
    updateScore({ commit, getters }, { moviePk, username, score }) {
      const updatedScore = { score }

      axios({
        url: drf.movies.movieRateUpdate(moviePk, username),
        method: 'put',
        data: updatedScore,
        headers: getters.authHeader,
      })
        .then(res => { 
          commit('SET_MOVIE_RATE', res.data['score']) 
        })
        .catch(err => console.error(err.response))
    },
    deleteScore({ commit, getters }, { moviePk, username }) {
      if (confirm('평가를 삭제하시겠습니까?')) {
        axios({
          url: drf.articles.movieRateUpdate(moviePk, username),
          method: 'delete',
          headers: getters.authHeader,
        })
          .then(() => { commit('SET_MOVIE_RATE', {}) })
          .catch(err => console.error(err.response))
      }
    },

  }
}