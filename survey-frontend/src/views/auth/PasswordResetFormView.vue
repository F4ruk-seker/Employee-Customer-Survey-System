<script>
import {f} from "vue-knob-control/dist/vue-knob-control.common";
import AuthService from "@/AuthService";

export default {
  name: "PasswordResetFormView",
  data: () => {return{
    password: '',
    password_is_valid: false,
    repeat_password: '',
    repeat_password_is_valid: false,
    passwords_is_equal: false,
    token_is_usable: false,
    token_usable_message: ''

  }},
  methods:{
    form_validator(){
      this.password_is_valid = this.password.length >= 8
      this.repeat_password_is_valid = this.repeat_password.length >= 8
      if (this.password_is_valid){
        this.passwords_is_equal = this.password === this.repeat_password
      }
    },
    async reset_password(){
      const status =  await AuthService.reset_password_with_credentials({
        reset_token: this.$route.query.reset_token,
        census_token: this.$route.query.census_token,
        password: this.password,
        repeat_password: this.repeat_password
      })
    },
    async token_validator(){
      const status =  await AuthService.reset_password_token_validate({
        reset_token:this.$route.query.reset_token,
        census_token:this.$route.query.census_token
      }
      )
      // return status === 200
      this.token_is_usable = status === 200
      console.log(this.token_is_usable)
      if (status === 200) {
        this.token_usable_message = ""
      } else if ( status === 208 ) {
        this.token_usable_message = "Anahtar daha önce kullanıldı"
      } else if ( status === 406 ) {
        this.token_usable_message = "Hatalı form biçimi bilgileri doğru girdiğinizden emin olunuz"
      } else {
        this.token_usable_message = "bilinmeyen bir hata oluştu"
      }
    }
  },
  mounted() {
    this.token_validator()

    // if (this.$route.query.confirmation_token && this.$route.query.census_token){
    // }
  }
}
</script>

<template>
  <section class="d-block d-md-flex" @keyup="form_validator">
    <form @submit.prevent="reset_password" class="card col-12 col-md-6 col-lg-4 col-xl-3 rounded m-auto shadow border-light">
      <div class="card-header fw-semibold text-center">
        Şifre sıfırla | Pars AUTH
      </div>
      <div class="card-body">
        <div class="d-flex mb-3">
          <span :class="'btn btn-light rounded-0 rounded-start disabled ' + (password_is_valid ? 'text-success': '') + ' ' + (passwords_is_equal ? 'border-success' : 'border-danger') " disabled>
            <i class="fa-solid fa-lock"></i>
          </span>
          <input :disabled="!token_is_usable" v-model="password" type="password" name="password" autocomplete="on" placeholder="şifreniz" class="form-control rounded-0 rounded-end" >
<!--          <button class="btn btn-light border rounded-0"><i class="fa-solid fa-eye"></i></button>-->
        </div>
        <div class="d-flex mb-2">
          <span :class="'btn btn-light rounded-0 rounded-start disabled '  + (repeat_password_is_valid ? 'text-success': '') + ' ' + (passwords_is_equal ? 'border-success' : 'border-danger')" disabled><i class="fa-solid fa-lock"></i></span>
          <input :disabled="!token_is_usable" v-model="repeat_password" type="password" name="password" autocomplete="on" placeholder="şifreniz" class="form-control rounded-0 rounded-end" >
<!--          <button class="btn btn-light border rounded-0"><i class="fa-solid fa-eye"></i></button>-->
        </div>
      </div>
      <div class="card-footer text-end d-flex justify-content-between">
        <div class="w-100">
        </div>
        <button class="btn btn-sm btn-success" type="submit" :disabled="!(password_is_valid && repeat_password_is_valid && passwords_is_equal)">
          <strong>Sıfırla</strong>
        </button>
      </div>
    </form>
    <p v-if="!token_is_usable" class="mt-2 mt-md-0 rounded bg-light fw-semibold p-2 border border-secondary-subtle">
      {{ token_usable_message }}
    </p>
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
