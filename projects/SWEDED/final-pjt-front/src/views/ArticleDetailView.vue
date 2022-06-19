<template>
  <div class="row text-white bg-dark">
    <div class="offset-3 col-6 row mt-3">
      <div v-if="isAuthor" class="col-12 row">
        <div class="col-4 offset-8 text-right mb-2">
          <router-link :to="{ name: 'articleEdit', params: {articlePk} }">
            <button class="btn btn-light">수정</button>
          </router-link>
          <button @click="deleteArticle(articlePk)" class="btn btn-warning ml-3">삭제</button>
        </div>
      </div>
      <p class="text-secondary mb-0 mt-2">영화 게시판</p>
      <h3 class="col-12 text-left text-warning mt-2">{{ article.title }}</h3>
      <div class="col-12 row">
        <p class="col-1">{{ article.user.username }}</p>
        <p class="mr-3">작성 시각: {{ format_date(article.created_at) }}</p>
        <p>수정 시각: {{ format_date(article.updated_at) }}</p>
      </div>
      <p class="col-12 text-left border-top pt-3">{{ article.content }}</p>
      <div style="height: 150px;"></div>
      <div class="col-12 row mb-4">
        <span class="col-2 text-left">댓글 {{ article.comments.length }}</span>
        <div class="offset-8 col-2 text-right">
          <button @click="likeArticle(article.pk)" class="btn btn-sm btn-outline-light">좋아요 {{ article.like_users.length }}</button>
        </div>
      </div>
      <div class="bg-secondary col-12 ">
        <comment-list :comments="article.comments"></comment-list>
      </div>
      <div class="text-right offset-10 col-2 mt-3">
        <button
          @click="moveToArticleList"
          class="btn btn-outline-light"
        >
          BACK
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import CommentList from '@/components/CommentList.vue'
import moment from 'moment'

export default {
  name: 'ArticleDetail',
  components: { CommentList },
  data() {
    return {
      articlePk: this.$route.params.articlePk,
    }
  },
  computed: {
    ...mapGetters(['isAuthor', 'article', ]),
  },
  methods: {
    ...mapActions(['fetchArticle', 'deleteArticle', 'likeArticle' ]),
    moveToArticleList() { 
      this.$router.push({
        name: 'articleList',
      }) 
    },
    format_date(value){
      if (value) {
        return moment(String(value)).format('YYYY년 MM월 DD일 hh:mm')
      }
    },
  },
  created() {
    this.fetchArticle(this.articlePk)
  }
}
</script>

<style>

</style>