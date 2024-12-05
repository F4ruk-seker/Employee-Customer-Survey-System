<script>
import AuthService from "@/AuthService";
import { useStore } from 'vuex'


export default {

  setup(){
    const store = useStore()
    return { store }
  },

  data(){return{
    username: ''
  }},
  methods:{
    async logout(){
      // this.store
      await AuthService.logout()
      await this.store.commit('change_auth_status', { status:false })
      this.$router.push({name:'login'})
    },
    say_hello_user(){
      console.log('this.store.getters.get_user')
      console.log(this.store.getters.get_user)
      if (this.store.getters.get_user){
        this.username =  this.store.getters.get_user.email
      }
    }
  },
  async mounted() {
    await this.store.dispatch('check_auth_status', false)
    await this.say_hello_user()
  }
}
</script>

<template>
  <nav class="navbar bg-light navbar-default border-bottom p-0 m-0 position-sticky top-0 z-3" style="height: 6vh">
    <div class="container-fluid my-auto">
      <a class="navbar-brand" href="/">
        <i class="fa-solid fa-signal"></i>
        <strong>
          Anket
        </strong>
      </a>
      <div>
        <strong >
          <i class="fa-solid fa-user"></i> {{ this.store.getters.get_user_name }}
        </strong>
        <!--        <router-link to="/about">About</router-link>-->
      </div>

      <div v-if="!this.store.getters.get_auth_status" class="d-flex">

        <router-link :to="{
          name: 'login'
        }" class="btn btn-primary fw-semibold ms-2">
          <i class="fa-solid fa-user"></i> Giriş Yap
        </router-link>
        <router-link :to="{
          name: 'register'
        }" class="btn btn-success fw-semibold ms-2">
          <i class="fa-solid fa-user-plus disabled" disabled></i> Kayıt Ol
        </router-link>
      </div>
      <div v-else>
        <button class="btn btn-danger fw-semibold ms-2" @click="logout">
          <i class="fa-solid fa-arrow-right-from-bracket"></i>
          Çıkış yap
        </button>
      </div>
    </div>
  </nav>
</template>

<style scoped>

</style>
