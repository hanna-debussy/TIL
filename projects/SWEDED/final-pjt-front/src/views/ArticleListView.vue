<template>
  <div class="col-10 offset-1">
    <!-- text-white -->
    <h1 class="font-weight-bold m-5 text-light">영화 게시판</h1>
    <div class="row mb-3">
      <div class="offset-10 col-1">
        <button
          @click="moveToArticleCreate"
          type="button"
          class="btn btn-light font-weight-bold"
        >
          글쓰기
        </button>
      </div>
      <div class="col-1">
        <button
          @click="moveToHome"
          type="button"
          class="btn btn-light font-weight-bold"
        >
          HOME
        </button>
      </div>
    </div>
    <table class="table table-hover table-dark">
      <thead>
        <tr>
          <th scope="col" class="col-7">제목</th>
          <th scope="col" class="col-2">글쓴이</th>
          <th scope="col" class="col-2">작성일</th>
          <th scope="col" class="col-1">좋아요</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="article in articles" :key="article.pk">
          <td class="text-left pl-4">
            <router-link
              :to="{ name: 'articleDetail', params: {articlePk: article.pk} }"
              class="text-white d-block"
            >
              {{ article.title }}
              <span class="border border-warning rounded-pill ml-2">&nbsp;&nbsp;{{ article.comment_count }}&nbsp;&nbsp;</span>
            </router-link>
          </td>
          <td>
            <router-link
              :to="{ name: 'profile', params: {username: article.user.username } }"
              class="text-white"
            >
              {{ article.user.username }}
            </router-link>
          </td>
          <td>{{ article.created_at | time_stamp }}</td>
          <td>{{ article.like_count }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'ArticleListView',
  computed: {
    ...mapGetters(['articles', ]),
  },
  methods: {
    ...mapActions(['fetchArticles', ]),
    moveToArticleCreate() { 
      this.$router.push({
        name: 'articleCreate',
      }) 
    },
    moveToHome() { 
      this.$router.push({
        name: 'movieList',
      }) 
    },
  },
  filters: {
    time_stamp(dateTime) {
      return dateTime.toString().slice(2, 10)
    },
  },
  created() {
    this.fetchArticles()
  },
}
</script>

<style>

</style>