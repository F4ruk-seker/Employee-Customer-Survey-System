<template>
  <section class="d-block d-md-flex position-relative" @keyup="form_validate">
    <form @submit.prevent="login()" class="card col-12 col-md-6 col-lg-4 col-xl-3 rounded m-auto shadow border-light ">
      <div class="card-header fw-semibold text-center">
        Giriş | Pars AUTH
      </div>
      <div class="card-body">
        <div class="mb-2">
          <label class="fw-semibold text-primary mb-1">Email <span class="text-danger">*</span></label>
          <input v-model="form_context.email" type="email" placeholder="e-mailiniz" class="form-control" required>
        </div>
        <div class="d-flex mb-2">
          <div class="me-1 w-100">
            <label class="fw-semibold text-primary mb-1">Şifreniz <span class="text-danger">*</span></label>
            <input autocomplete="false" v-model="form_context.password" type="password" placeholder="Şifreniz" class="form-control" required>
          </div>
        </div>
        <router-link :to="{
          name:'forget-password'
        }"
        class="fw-semibold text-decoration-none link-success"
        >
          Şifremi unuttum ?
        </router-link>
        <Transition>
          <code class="text-center fw-semibold p-0 m-0" v-show="login_error_status">
            <br>

            Giriş Başarısız!
          </code>
        </Transition>
        <hr style="border-top: dotted 1px;" class="my-3">
        <router-link :to="{
          name: 'register'
        }">
          <strong class="fw-bold">Kayıt olun</strong>
        </router-link>
      </div>
      <div class="card-footer text-end d-flex justify-content-between">
        <div class="d-flex">
          <button class="btn btn-light btn-sm border me-2" type="button">
            <i class="fa-brands fa-google"></i>
          </button>
          <button
              :class="'btn btn-sm btn-' + (email_verified ? 'primary' : 'secondary')"
              type="button"
              :disabled="!email_verified"
              @click="create_login_with_token">
            <div v-if="!on_sending_password_login_token">
              <span class="my-auto fw-bold">Şifresiz giriş</span>
            </div>
            <div v-else>
              <div class="spinner-grow spinner-grow-sm" role="status">
                <span class="sr-only">Loading...</span>
              </div>
              Gönderiliyor
            </div>
          </button>
        </div>
        <div class=""></div>
        <button
                :disabled="!form_verified"
            class="btn btn-success btn-sm fw-semibold d-inline-block"
                style="width: 100px;" type="submit" >
          <span class="my-auto fw-bold">Giriş</span>
        </button>
      </div>
    </form>
  </section>
  <hr class="p-0 m-0">
  <footer class="container mx-auto fw-semibold pt-1">
    <code>
      <i class="fa-solid fa-shield-cat"></i>
      Pars Border Services!
    </code>
  </footer>
</template>

<script>
import Navbar from "@/components/navbar.vue";

import AuthService from "@/AuthService";
import { useStore } from 'vuex'
import {f} from "vue-knob-control/dist/vue-knob-control.common";

export default {
  name:'LoginView',
  components: {Navbar},
  setup(){
    const store = useStore();
    return { store }
  },
  data(){return{
    form_context: {
      password: '',
      email: ''
    },
    login_status: false,
    login_error_status: false,
    email_verified: false,
    password_verified: false,
    form_verified: false,
    on_sending_password_login_token: false,
  }},
  methods:{
    async login(){
      console.log('inners')
      if (await AuthService.login({
        "email": this.form_context.email,
        "password": this.form_context.password
        })){
          this.store.commit('change_auth_status', { status : true })
          this.login_error_status = false
          this.show_success_message()
          this.route_to_home()
        }else {
          this.login_error_status = true
          this.show_login_error_message()
      }
    },
    async login_with_token(){
      const response = await AuthService.login_with_token(this.$route.query.login_token)
    },
    async create_login_with_token(){
      if (this.email_verified){
        this.email_verified = false
        this.on_sending_password_login_token = true
        await AuthService.create_login_with_token(this.form_context.email)
        this.email_verified = true
        this.on_sending_password_login_token = false
      }
    },
    show_login_error_message(){
      this.$notify({
        type: 'error',
        title: 'Giriş Başarısız',
        text: 'Lütfen giriş bilgilerinizi kontrol ediniz'
        })
    },
    show_success_message(){
      this.$notify({
        type: 'success',
        title: 'Giriş Doğrulandı!',
        text: 'Giriş Başarılı yönlendirliyorsunuz \nkonum; Ana Sayfa'
      })
    },
    route_to_home(){
      this.$router.push({
        name:'exam_list'
      })
    },
    validateEmailAddress(emailAddress) {
      const emailRegex = /^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$/;
      return emailRegex.test(emailAddress);
    },
    form_validate(){
      this.email_verified = this.validateEmailAddress(this.form_context.email)
      this.password_verified = this.form_context.password.length >= 8
      this.form_verified = this.email_verified && this.password_verified
      // this.verified = (this.validateEmailAddress(this.form_context.email)) && (this.form_context.password.length >= 8)
    },

  },

  mounted() {
    if (this.$route.query.login_token){
      this.login_with_token()
    }
  }
}

</script>


<style scoped>
.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}

section{
  flex-grow: 1;
  display: flex;
  width: 100%;
  height: 88vh;
  --d: 1px;
  background: radial-gradient( circle at var(--d) var(--d), #000 calc(var(--d) - 1px), #0000 var(--d) ) 0 0 / 20px 20px;
  flex-direction: column;
  align-items: center;
  align-self: stretch;
}

.kaydirilabilir-div {
  width: 200px;
  height: 200px;
  position: absolute;
}

</style>
