<script>
import AuthService from "@/AuthService";

export default {
  name: 'RegisterView',
  data(){return{
    verified:false,
    form_context:{
      first_name: null,
      last_name: null,
      email: null,
      password: null,
      repeat_password: null,
    }

  }},
  methods:{
    form_verify (){
      for (var formContextKey in this.form_context) {
        this.verified = this.form_context[formContextKey]
      }
    },
    async register(){
      if (await AuthService.register(
          this.form_context
      )){
        this.$router.push({name:'login'})
      }
    },
  }
}
</script>

<template>
<section class="d-block d-md-flex">
  <form @submit.prevent="register" class="card col-12 col-md-6 col-lg-4 col-xl-3 rounded m-auto shadow border-light">
    <div class="card-header fw-semibold text-center">
      Kayıt | Pars AUTH
    </div>
    <div class="card-body">
      <div class="d-flex mb-2">
        <div class="me-1 w-100">
          <label class="fw-semibold text-primary">Adınız <span class="text-danger">*</span> </label>
          <input v-model="form_context.first_name" type="text" placeholder="Adınız" class="form-control" required>
        </div>
        <div class="ms-1 w-100">
          <label class="fw-semibold text-primary">Soy Adınız </label>
          <input v-model="form_context.last_name" type="text" placeholder="Soy Adınız" class="form-control">
        </div>
      </div>
      <div class="mb-2">
        <label class="fw-semibold text-primary">Email Addresiniz <span class="text-danger">*</span></label>
        <input v-model="form_context.email" type="email" placeholder="e-mailiniz" class="form-control" required>
      </div>
      <div class="d-flex mb-2">
        <div class="me-1 w-100">
          <label class="fw-semibold text-primary">Şifreniz <span class="text-danger">*</span></label>
          <input autocomplete="false" v-model="form_context.password" type="password" placeholder="Şifreniz" class="form-control" required>
        </div>
      </div>
      <hr style="border-top: dotted 1px;" class="my-3">
      <router-link :to="{
          name: 'login'
        }">
        <strong class="fw-bold">Giriş Yapın</strong>
      </router-link>
    </div>
    <div class="card-footer text-end d-flex justify-content-between">
      <button class="border-0 px-2 py-1 rounded fw-semibold text-dark position-absolute z-3" style="width: 50px;" type="submit" @click="srm" disabled>
        <i class="fa-brands fa-google"></i>
      </button>
      <div class="w-100"></div>
      <button class="btn btn-success btn-sm fw-semibold d-inline-block" style="width: 140px;" type="submit"  :disabled="verified">
        <span class="my-auto fw-bold">Kayıt Ol</span>
      </button>
    </div>
  </form>
</section>
  <hr class="p-0 m-0 ">
<footer class="container mx-auto fw-semibold pt-1">
  <code>
    <i class="fa-solid fa-shield-cat"></i>
    Pars Border Services!
  </code>
</footer>
</template>

<style scoped>
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
</style>
