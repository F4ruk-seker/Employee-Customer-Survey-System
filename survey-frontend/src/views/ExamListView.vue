<script>
import axios from "axios";
import { useStore } from 'vuex'
import Navbar from "@/components/navbar.vue";


// const api_host = process.env.VUE_APP_API_HOST
const api_host = 'http://127.0.0.1:8000/api/'


// const api_host =
const api_host_path = `${api_host}exam/`


export default{
  components: {Navbar},
  setup(){
    const store = useStore()
    return { store }
  },
  name: 'ExamListView',
  data(){return{
    exam_list:{},
  }},
  methods:{
    async get_exam_list(){
        const response = await axios.get(api_host_path)
        if (response.status === 200){
          this.exam_list = response.data
        }
    },
    go_exam(slug){
      this.$router.push({
        name:'exam',
        params:{
          'slug':slug
        }
      })
    },
  },
  async mounted() {
    await this.get_exam_list()
    await this.store.dispatch('check_auth_status', false)

  }
}
</script>

<template>
  <navbar />
  <section class="container" v-if="exam_list.length > 0">
    <div class="border rounded p-3 mb-3" v-for="exam in exam_list">
      <div class="d-flex justify-content-between">
        <strong class="d-block mb-3">
          <i class="fa-solid fa-square-poll-vertical me-1"></i>
          {{ exam.title }}
        </strong>
        <span></span>
        <span><i class="fa-solid fa-check"></i></span>
      </div>
      <button class="btn btn-primary fw-semibold" @click="go_exam(exam.slug)">Anket yap</button>
    </div>
  </section>
  <section v-else>
    <div class="alert alert-info container">
      Henüz Bir Anket Oluşturulmadı
    </div>
  </section>

  <section class="container" v-if="this.store.getters.get_user.is_staff">
    <hr>

    <div class="d-flex justify-content-between">
      <div class="d-flex">
        <button
            class="btn btn-sm btn-light d-inline-block rounded-end-0 fw-semibold"
            style="width: max-content"
            @click="$router.push({
              name: 'results'
            })"
        >Sonuçları Gör</button>
        <span class="vr"></span>
      </div>
      <div class="w-100 bg-light">
<!--        <hr class="text-danger mx-2">-->
      </div>
    </div>
  </section>
</template>

<style scoped>

</style>
