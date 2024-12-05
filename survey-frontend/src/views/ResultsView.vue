<script>
import axios from "axios";
import Navbar from "@/components/navbar.vue";


export default {
  name: "ResultsView",
  components: {Navbar},
  data:() => {return{
    results:[],
    api_host: 'http://127.0.0.1:8000/api/'
  }},
  methods:{
    async get_results(){
      try {
        const response = await axios.get(`${this.api_host}exam/answers/`)
        if (response.status === 200){
            this.results = await response.data
            this.results.forEach((e) => {
              e.created = this.get_date(e.created)
            })
        }
      }catch (e) {}
    },
    get_date(date){
      const rawDate = new Date(date);
      const options = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit', second: '2-digit', timeZoneName: 'short' };
      return rawDate.toLocaleDateString(undefined, options);
    }
  }, mounted() {
    this.get_results()
  }
}
</script>

<template>
  <navbar />
<section class="container overflow-y-auto" style="height: 92vh">
  <div class="card mb-3" v-for="result in results">
    <div class="card-header fw-semibold">
      Kullanıcı: {{ result.user }}
    </div>
    <div class="card-body">
      <span class="fw-semibold">{{ result.exam.title }}</span>
      <hr>
      <div>
        <div v-for="(answer_question, index) in result.answer_question_list">
          <p class="fw-semibold">{{ index }}.<span class="fw-normal">{{ answer_question.question }}</span></p>
          <input type="range" :value="answer_question.answer" disabled> {{ answer_question.answer }}%
        </div>
      </div>
    </div>
    <div class="card-footer d-flex justify-content-between">
      <div class="my-auto">
        Kayıt tarihi : {{ result.created }}
      </div>

      <div class="my-auto">
        <button class="btn btn-sm btn-danger me-1 fw-semibold" disabled>Sil</button>
      </div>
    </div>
  </div>
</section>
</template>

<style scoped>

</style>
