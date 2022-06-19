import Vue from 'vue'
import Vuex from 'vuex'
import articles from './modules/articles'
import accounts from './modules/accounts'
import movies from './modules/movies'
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex)

export default new Vuex.Store({
  
  plugins: [createPersistedState({
    paths: ["accounts"]
  })],

  modules: {
    accounts,
    articles,
    movies,
  }
})
