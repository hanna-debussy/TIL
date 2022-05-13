import Vue from 'vue'
import Vuex from 'vuex'

import _ from 'lodash'
import axios from 'axios'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)


// const API_KEY = process.env.VUE_TMDB_API_KEY
const API_KEY = 'apikey'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    myMovies: [],   // 보고싶은 영화 WatchList
  },
  getters: {
  },
  mutations: {
    CREATE_MY_MOVIE(state, newMovie) {
      state.myMovies.push(newMovie)
    },
    DELETE_MY_MOVIE(state, deleteMovie) {
      const index = state.myMovies.indexOf(deleteMovie)
      state.myMovies.splice(index, 1)
    },
    UPDATE_WATCHED(state, watchedMovie) {
      state.myMovies = state.myMovies.map(myMovie => {
        if (myMovie === watchedMovie) {
          myMovie.watched = !myMovie.watched
        }
        return myMovie
      })
    },
  },
  actions: {
    createMyMovie({ commit }, newMovie) {
      commit("CREATE_MY_MOVIE", newMovie)
    },
    deleteMyMovie({ commit }, deleteMovie) {
      commit("DELETE_MY_MOVIE", deleteMovie)
    },
    updateWatched({ commit }, watchedMovie) {
      commit("UPDATE_WATCHED", watchedMovie)
    },  },
  modules: {
  }
})
