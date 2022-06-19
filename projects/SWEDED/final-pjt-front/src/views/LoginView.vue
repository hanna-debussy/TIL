<template>
  <div class="d-flex align-items-center justify-content-center row">
    <div class="col-3 justify-content-center" style="margin: 25vh 0;">
      <div class="card text-center">
        <div class="card-header font-weight-bold h5">
          로그인
        </div>
        <div class="card-body">
          <div class="mb-3">
            <form @submit.prevent="login(credentials)">
              <div class="mb-3">
                <label for="username" class="text-left text-secondary d-block" style="font-size: 12px">아이디</label>
                <input type="text" id="username" required v-model="credentials.username" class="form-control"/>
              </div>
              <div class="mb-3">
                <label for="password" class="text-left text-secondary d-block" style="font-size: 12px">비밀번호</label>
                <input type="password" id="password" required v-model="credentials.password" class="form-control"/>
              </div>
              <button class="btn btn-warning font-weight-bold col-10">로그인</button>
            </form>
          </div>
          <div>
            <button @click="moveToSignUp" type="button" class="btn btn-light col-10">회원가입</button>
          </div>
        </div>
      </div>      
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'LoginView',
  data() {
    return {
      credentials: {
        username: '',
        password: '',  
      }
    }
  },
  computed: {
      // ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login']),
      moveToSignUp() { 
        this.$router.push({
          name: 'signup',
        }) 
      },
    },

}
</script>

<style>

</style>