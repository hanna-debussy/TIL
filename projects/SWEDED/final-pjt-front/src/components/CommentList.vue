<template>
  <div>
    <ul class="list-group list-group-flush">
      <comment-list-item
        v-for="comment in comments"
        :key="comment.pk"
        :comment="comment"
      >
      </comment-list-item>
    </ul>
    <comment-form></comment-form>
  </div>
</template>

<script>
import CommentForm from '@/components/CommentForm.vue'
import CommentListItem from '@/components/CommentListItem.vue'

export default {
  name: 'CommentList',
  components: { CommentForm, CommentListItem, },
  props: { comments: Array },
}
</script>

<style>

</style>