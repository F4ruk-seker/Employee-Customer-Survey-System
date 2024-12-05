<script>
import AuthService from "@/AuthService";
import {f} from "vue-knob-control/dist/vue-knob-control.common";

export default {
  name: "PasswordRestRequest",
  data: () => {return{
    email: '',
    on_sending: false
  }},
  methods: {
    async send_password_reset_request(){
      this.on_sending = true
      await AuthService.send_password_reset_token_request(this.email)
      this.on_sending = false
    }
  }
}
</script>

<template>
  <section class="d-block d-md-flex position-relative" @keyup="form_validate">
    <form @submit.prevent="send_password_reset_request" class="card col-12 col-md-6 col-lg-4 col-xl-3 rounded m-auto shadow border-light ">
      <div class="card-header fw-semibold text-center">
        Şifremi unuttum | Pars AUTH
      </div>
      <div class="card-body">
        <div class="mb-2">
          <label class="fw-semibold text-primary mb-1">Email <span class="text-danger">*</span></label>
          <input v-model="email" type="email" placeholder="e-mailiniz" class="form-control" required>
        </div>
      </div>
      <div class="card-footer text-end d-flex justify-content-between">
        <div class="w-100"></div>
        <button
            class="btn btn-success btn-sm fw-semibold d-inline-block"
            style="width: 100px;" type="submit" >
          <span v-if="!on_sending" class="my-auto fw-bold">Giriş</span>
          <div v-else class="spinner-grow spinner-grow-sm" role="status">
            <span class="sr-only">Loading...</span>
          </div>
        </button>

      </div>
    </form>
    <p class="mt-2 mt-md-0 rounded bg-light fw-semibold p-2 border border-secondary-subtle">
      E postanıza karşılık gelen bir üyelik var ise Şifre sıfırlama kodunuzu alırsınız, Spam kutunuzu kontrol etmeyi unutmayın
    </p>
  </section>
  <hr class="p-0 m-0">
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
