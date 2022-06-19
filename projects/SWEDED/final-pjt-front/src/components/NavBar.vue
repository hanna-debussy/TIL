<template>
  <nav>
    <div class="logo">
      <a href="http://localhost:8080/movies/">
        <img src="@/assets/sweded.png" alt="logo" class="logowidth">
      </a>
    </div>
    <router-link :to="{ name: 'home' }">Home | </router-link>   

    <router-link v-if="isLoggedIn" :to="{ name: 'profile', params: {username} }">Profile | </router-link> 
    
    <router-link :to="{ name: 'articleList' }">Community | </router-link>
    
    <router-link v-if="!isLoggedIn" :to="{ name: 'signup'}">Signup | </router-link> 

    <router-link v-if="!isLoggedIn" :to="{ name: 'login' }">Login | </router-link>

    <a v-if="isLoggedIn" @click="logout()" class="hovercursor">Logout</a>
  </nav>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'

  export default { 
    name: 'NavBar',
    methods: {
      ...mapActions(['logout'])
    },
    computed: {
      ...mapGetters(['currentUser', 'isLoggedIn']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    }
  }
</script>

<style>
.logo {
  position: absolute;
  top: 1rem;
  left: 2rem;
}
.logowidth {
  width: 50px;
}
.hovercursor:hover {
  cursor: pointer;
}
</style>