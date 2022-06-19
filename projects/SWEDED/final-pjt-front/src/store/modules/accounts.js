import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'


export default {
  state: {
    token: localStorage.getItem('token') || '',
    currentUser: {},
    profile: {},
    authError: null,
  },
  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    profile: state => state.profile,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `Token ${state.token}`})
  },
  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_PROFILE: (state, profile) => state.profile = profile,
    SET_AUTH_ERROR:(state, error) => state.authError = error,
  },
  actions: {
    saveToken({ commit }, token) {

      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)
    },

    removeToken({ commit }) {

      commit('SET_TOKEN', '')
      localStorage.setItem('token', '')
    },

    signup({ commit, dispatch }, credentials) {

      axios({
        url: drf.accounts.signup(),
        method: 'post',
        data: credentials
      })
        .then((res) => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'home' })
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },

    login({ dispatch, commit }, credentials) {

      axios({
        url: drf.accounts.login(),
        method: 'post',
        data: credentials
      })
        .then((res) => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'home' })
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },

    logout({ dispatch, getters }) {
      if (confirm('로그아웃하시겠습니까?')){
        axios({
          url: drf.accounts.logout(),
          method: 'post',
          headers:getters.authHeader,
        })
         .then(() => {
           dispatch('removeToken')
           router.push({ name: 'login' })
         })
         .error(err => {
           console.error(err.response)
         })
      }
    },

    fetchProfile({ commit, getters }, { username }) {
      axios({
        url: drf.accounts.profile(username),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_PROFILE', res.data)
        })
    },

    fetchCurrentUser({ commit, getters }) {
      
      axios({
        url: drf.accounts.currentUserInfo(),
        method: 'get',
        headers: getters.authHeader
      })
        .then(res => {
          commit('SET_CURRENT_USER', res.data)
        })
    },

  },

}