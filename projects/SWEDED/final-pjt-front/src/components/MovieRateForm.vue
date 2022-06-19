<template>
  <div>
    <form @submit.prevent="rateSubmit()">
      <input type="number" v-model="score">
      <button>{{ action }}</button>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'MovieRateForm',
  props: {
    action: String,
    newScore: Number,
  },
  data() {
    return {
      score: 0,
    }
  },
  computed: {
    ...mapGetters(['movie', 'currentUser' ]),
  },
  methods: {
    ...mapActions(['createScore', 'updateScore', 'fetchIsRated', ]),
    rateSubmit() {
      if (this.action === 'create') {
        this.createScore({ moviePk: this.movie.movie_id, score: this.score, })
      } else if (this.action === 'update') {
        this.$emit('rated', this.score)
        const payload = {
          moviePk: this.movie.movie_id,
          username: this.currentUser.username,
          score: this.score,
        }
        this.updateScore(payload)
        this.$emit('rated', this.score)
        this.fetchIsRated(this.movie.movie_id)
      }
    },
  },
}
</script>

<style>

</style>