<template>
  <li class="list-group-item bg-transparent text-white row d-flex">
    <p class="font-weight-bold text-left col-12 mb-1">{{ comment.user.username }}</p>
    <div v-if="!isEditing" class="text-left col-9">
        {{ payload.content }}
    </div>
    <div v-if="isEditing" class="col-12 row pr-0 pl-4">
      <input type="text" v-model="payload.content" class="border-0 col-10 d-block">
      <div class="col-2 text-right pr-0">
        <button @click="onUpdate" class="btn btn-sm btn-outline-light mr-2">수정</button>
        <button @click="switchIsEditing" class="btn btn-sm btn-outline-light">취소</button>
      </div>
    </div>
    <div v-if="currentUser.username === comment.user.username && !isEditing" class="col-3 text-right">
      <button @click="switchIsEditing" class="btn btn-sm btn-outline-light mr-2">수정</button>
      <button @click="deleteComment(payload)" class="btn btn-sm btn-outline-light">삭제</button>
    </div>

  </li>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        articlePk: this.comment.article,
        commentPk: this.comment.pk,
        content: this.comment.content,
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser', ]),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment', ]),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    },
  },
}
</script>

<style>

</style>