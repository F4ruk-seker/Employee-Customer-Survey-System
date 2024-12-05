<script>
import AuthService from "@/AuthService"

export default {
  name: "email_confirmation_view",
  mounted() {
    this.token = this.$route.params.token
    this.census_token = this.$route.query.census_token
    this.check_email_confirmation_token()
  },
  data: ()=>{return{
    message: '',
    can_action: false,
    token: null,
    census_token: null

  }},
  methods: {
    go_login_page(){
      this.$router.push({name: 'login'})
    },

    async check_email_confirmation_token(){

      const status = await AuthService.email_confirmation_token_control(this.token, this.census_token)
      if (status === 200){
        this.message = "Anahtar Doğrulandı: E-posta Adresinizi Onaylayabilirsiniz"
        this.can_action = true
      }
      else if (status === 208){
        this.message = "Anahtar Süresi Dolmuş veya Kullanılmış"
        this.can_action = false
      }
      else if (status === 226){
        this.message = "Bu anahtar, üyeliği reddetti. Tekrar kullanım için 48 saat sonra yeniden üye olabilirsiniz."
        this.can_action = false
      }
      else {
        this.$router.push({name:'login'})
      }
    },
    async accept_email_confirmation(){
      const status = await AuthService.email_confirmation_accept(this.token, this.census_token)
      if (status === 201 ){this.go_login_page()}

    },
    async reject_email_confirmation(){
      const status = await AuthService.remove_disapproved_user(this.token, this.census_token)
      if ( status === 226 ){
        this.message = "Üyelik Onaylama Red Edildi! En Erken 48 Saat Sonra Tekrar Üye Olabilirsiniz. Eğer Bir Hata Olduğunu Düşünüyorsanız," +
            " lütfen help@survey.darken.gen.tr adresine e-posta atınız."
        this.can_action = false
      }
    }
  }
}
</script>

<template>
  <section class="d-block d-md-flex position-relative" @keyup="form_validate">
    <article class="card col-12 col-md-6 col-lg-4 col-xl-3 rounded m-auto shadow border-light ">
      <div class="card-header fw-semibold text-center">
        E-Posta aktivasyonu | Pars AUTH
      </div>
      <div class="card-body">
        {{ message }}
      </div>
      <div class="card-footer text-end d-flex justify-content-between">
        <div class="w-100"></div>
        <button :disabled="!can_action" @click="reject_email_confirmation"
            class="btn btn-danger btn-sm fw-semibold d-inline-block me-2"
            style="width: 100px;" type="submit" >
          <span class="my-auto fw-bold">Sil</span>
        </button>
        <button :disabled="!can_action" @click="accept_email_confirmation"
            class="btn btn-success btn-sm fw-semibold d-inline-block"
            style="width: 100px;" type="submit" >
          <span class="my-auto fw-bold">Onayla</span>
        </button>
      </div>
    </article>
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
