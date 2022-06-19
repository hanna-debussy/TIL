<template>
  <div>
    <div class="offset-1 col-10 row">
      <div class="text-right offset-3 col-6">
        <button
          @click="moveToArticleList"
          class="btn btn-outline-light"
        >
          HOME
        </button>
      </div>
    </div>

    <article-form :article="article" action="create"></article-form>
  </div>
</template>

<script>
  import ArticleForm from '@/components/ArticleForm.vue'
  export default {
    name: 'ArticleCreate',
    components: { ArticleForm },
    data() {
      return {
        article: {
          pk: null,
          title: '',
          content: '',
        }
      }
    },
    methods: {
      moveToArticleList() { 
        this.$router.push({
          name: 'articleList',
        }) 
      },
    }
  }
</script>

<style></style>
