<template>
  <form @submit.prevent="onSubmit" class="row">
    <div class="offset-1 col-10 row">
      <span class="border-bottom p-1 offset-3 col-6 mb-3 row">
        <input
          v-model="newArticle.title"
          type="text"
          placeholder="제목을 입력하세요"
          class="bg-transparent border-0 d-block col-12 form-control text-white"
        />
      </span>    
    </div>
    <div class="offset-1 col-10 row mb-3">
      <textarea
        v-model="newArticle.content"
        type="text"
        id="content"
        class="bg-transparent offset-3 col-6 form-control text-white"
        rows="10"
      >
      </textarea>
    </div>
    <div class="offset-1 col-10 row">
      <div class="text-right offset-3 col-6">
        <button class="btn btn-warning">{{ action }}</button>
      </div>
    </div>
  </form>
</template>

<script>
import { mapActions } from 'vuex'

  export default {
    name: 'ArticleForm',
    props: {
      article: Object,
      action: String,
    },
    data() {
      return {
        newArticle: {
          title: this.article.title,
          content: this.article.content,
        }
      }
    },

    methods: {
      ...mapActions(['createArticle', 'updateArticle']),
      onSubmit() {
        if (this.action === 'create') {
          this.createArticle(this.newArticle)
        } else if (this.action === 'update') {
          const payload = {
            pk: this.article.pk,
            ...this.newArticle,
          }
          this.updateArticle(payload)
        }
      },
    },
  }
</script>

<style></style>
