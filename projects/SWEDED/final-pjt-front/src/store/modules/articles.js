import axios from "axios";
import drf from "@/api/drf";
import router from "@/router";

import _ from "lodash";


export default {
  state: {
    articles: [],
    article: {},
  },

  getters: {
    articles: state => state.articles,
    article: state => state.article,
    isArticle: state => !_.isEmpty(state.article),
    isAuthor: (state, getters) => {
      return state.article.user?.username === getters.currentUser.username
    },
  },

  mutations: {
    SET_ARTICLES: (state, articles) => state.articles = articles,
    SET_ARTICLE: (state, article) => state.article = article,
    SET_ARTICLE_COMMENTS: (state, comments) => state.article.comments = comments,
    SET_ARTICLE_LIKE: (state, like_users) => state.article.like_users = like_users,
  },

  actions: {
    fetchArticles({ commit, getters }) {
      axios({
        url: drf.articles.articles(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_ARTICLES', res.data))
        .catch(err => {
          console.error(err.response)
          alert('로그인 해주세요')
        })
    },
    fetchArticle({ commit, getters }, articlePk) {
      axios({
        url: drf.articles.article(articlePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_ARTICLE', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },
    createArticle({ commit, getters }, article) {
      axios({
        url: drf.articles.articles(),
        method: 'post',
        data: article,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE', res.data)
          router.push({
            name: 'articleDetail',
            params: { articlePk: getters.article.pk }
          })
        })
    },

    updateArticle({ commit, getters }, { pk, title, content }) {
      axios({
        url: drf.articles.article(pk),
        method: 'put',
        data: { title, content },
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE', res.data)
          router.push({
            name: 'articleDetail',
            params: { articlePk: getters.article.pk }
          })
        })
    },
    deleteArticle({ commit, getters }, articlePk) {
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.articles.article(articlePk),
          method: 'delete',
          headers: getters.authHeader,
        })
          .then(() => {
            commit('SET_ARTICLE', {})
            router.push({ name: 'articleList' })
          })
          .catch(err => console.error(err.response))
      }
    },

    createComment({ commit, getters }, { articlePk, content }) {
      const comment = { content }

      axios({
        url: drf.articles.comments(articlePk),
        method: 'post',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => { commit('SET_ARTICLE_COMMENTS', res.data) })
        .catch(err => console.error(err.response))
    },
    updateComment({ commit, getters }, { articlePk, commentPk, content }) {
      const comment = { content }
      axios({
        url: drf.articles.comment(articlePk, commentPk),
        method: 'put',
        data: comment,
        headers: getters.authHeader
      })
        .then(res => { commit('SET_ARTICLE_COMMENTS', res.data) })
        .catch(err => console.error(err.response))
    },
    deleteComment({ commit, getters }, {articlePk, commentPk}) {
      if (confirm('댓글을 삭제하시겠습니까?')) {
        axios({
          url: drf.articles.comment(articlePk, commentPk),
          method: 'delete',
          data: {},
          headers: getters.authHeader,
        })
          .then(res => { commit('SET_ARTICLE_COMMENTS', res.data) })
          .catch(err => console.error(err.response))
      }
    },
    
    likeArticle({ commit, getters }, articlePk ) {
      axios({
        url: drf.articles.likeArticle(articlePk),
        method: 'post',
        // data: articlePk,
        headers: getters.authHeader,
      })
        .then(res => { commit('SET_ARTICLE_LIKE'), res.data })
        .catch(err => console.error(err.response))
    }
  },
}