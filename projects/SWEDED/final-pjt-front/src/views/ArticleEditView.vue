<template>
  <div>
    <div class="offset-1 col-10 row">
      <div class="text-right offset-3 col-6">
        <button
          @click="goBack"
          class="btn btn-outline-light"
        >
          HOME
        </button>
      </div>
    </div>

    <article-form v-if="isArticle" :article="article" action="update">

    </article-form>
  </div>

</template>

<script>
import ArticleForm from '@/components/ArticleForm.vue'
import { mapGetters, mapActions } from 'vuex'

  export default {
    name: 'AritcleEditView',
    components: { ArticleForm },
    computed: {
      ...mapGetters(['article', 'isArticle',])
    },
    methods: {
      ...mapActions(['fetchArticle']),
      goBack() { 
        this.$router.go(-1)
      },
    },
    created() {
      this.fetchArticle(this.$route.params.articlePk)
    },
  }
</script>

<style></style>
