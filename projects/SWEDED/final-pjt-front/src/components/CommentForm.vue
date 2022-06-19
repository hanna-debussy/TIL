<template>
  <div>
    <form @submit.prevent="onSubmit" class="row m-3 text-right">
      <input type="text" id="comment" v-model="content" required class="border-0 d-block col-10">
      <button class="btn btn-sm btn-outline-light col-1 offset-1">등록</button>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'CommentForm',
  data() {
    return {
      content: '',
    }
  },
  computed: {
    ...mapGetters(['article', ]),
  },
  methods: {
    ...mapActions(['createComment', ]),
    onSubmit() {
      this.createComment({ articlePk: this.article.pk, content: this.content, })
      this.content = ''
    },
  },
}
</script>

<style>

</style>