<template>
  <div class="d-flex align-items-center justify-content-center row">
    <div class="col-3 justify-content-center" style="margin: 25vh 0;">
      <div class="card text-center">
        <div class="card-header font-weight-bold h5">
          회원가입
        </div>
        <div class="card-body">
          <div class="mb-3">
            <form @submit.prevent="signup(credentials)">
              <div class="mb-3">
                <label for="username" class="text-left text-secondary d-block" style="font-size: 12px">아이디</label>
                <input  v-model="credentials.username" type="text" id="username" required class="form-control"/>
              </div>
              <div class="mb-3">
                <label for="password1" class="text-left text-secondary d-block" style="font-size: 12px">비밀번호</label>
                <input v-model="credentials.password1" type="password" id="password1" required class="form-control"/>
              </div>
              <div class="mb-3">
                <label for="password2" class="text-left text-secondary d-block" style="font-size: 12px">비밀번호 확인</label>
                <input v-model="credentials.password2" type="password" id="password2" required class="form-control"/>
              </div>
              <div>
                <button class="btn btn-warning font-weight-bold col-10">회원가입</button>
              </div>
            </form>
          </div>
          <div>
            <button @click="moveToLogIn" type="button" class="btn btn-light col-10">로그인</button>
          </div>
        </div>
      </div>      
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
  export default {
    name: 'SignupView',
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    methods: {
      ...mapActions(['login', 'signup']),
      moveToLogIn() { 
        this.$router.push({
          name: 'login',
        }) 
      },
    }
  }
</script>

<style>

</style>