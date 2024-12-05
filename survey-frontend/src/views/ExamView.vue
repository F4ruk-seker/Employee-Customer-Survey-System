<script>
import Knob from 'primevue/knob';
import axios from "axios";
import {ref} from "vue";
import {f} from "vue-knob-control/dist/vue-knob-control.common";

const api_host = 'http://127.0.0.1:8000/api/'

const api_host_path = `${api_host}exam/`

export default {
  name: 'ExamView',
  components: {
    Knob
  },
  methods:{
    f,
     async get_exam() {
        try {
          var exam = await axios.get(`${api_host_path}${this.$route.params.slug}/`);
          this.exam = exam.data;
          this.exam.questions.forEach(e =>{
            e.answer = ref(0)
          })
        } catch (error) {
          console.log('login er')
          this.$router.push({
            name: 'login'
          })
          console.error(error);
        }
      },
      show_n (){
        this.$notify("Hello user!");

      },
     async answer_exam(){
       this.on_sending = true
       try {
         var response = await axios.post(`${api_host_path}${this.$route.params.slug}/answer/`,
             {
               exam:this.exam,
               email:this.email
             }
         )
         if (response.status === 201) {
           this.$notify({
             type: 'success',
             title: 'Kayıt Başarılı',
             text: 'Email Kutunuzu kontrol ediniz'
           })
         }
       }catch (e) {
         this.$notify({
           type: 'error',
           title: 'Kayıt edilemedi',
           text: 'Form Kabul edilebilir değil, lütfen formu kontrol ediniz'
         })
       }
       this.on_sending = false
     },
  },
  data() {
    return {
      exam: {},
      knob_size: 80,
      on_sending: false

    };
  },
  mounted() {
    this.get_exam();
  },
};

</script>

<template>
  <section class="container m-auto border p-3 rounded">
    <div class="d-flex justify-content-between">
      <strong class="my-auto">
        <i class="fa-solid fa-square-poll-horizontal "></i>
        <span class="ms-2">{{ exam.title }}</span>
      </strong>
      <span></span>
      <div class="d-block" style="text-align: right;justify-content: right">
        <button class="btn btn-light border ms-2" @click="this.knob_size = (this.knob_size + 10) <= 350 ? this.knob_size + 10 : 350 ">
          <i class="fa-solid fa-circle-plus text-success"></i>
        </button>
        <button class="btn btn-light border ms-2" @click="this.knob_size = (this.knob_size - 10) >= 50 ? this.knob_size - 10 : 50 ">
          <i class="fa-solid fa-circle-minus"></i>
        </button>
      </div>
    </div>
    <hr>
    <ul class="list-unstyled">
      <li v-for="(question, index) in exam.questions" >
        <div class="d-flex">
          <strong>{{ index+1 }}. </strong>
          <p class="d-inline-block">{{ question.text }}</p>
        </div>
        <Knob :size="knob_size" v-model="question.answer" value-color="gray" :show-value="false" />
      </li>
    </ul>
    <hr>
      <button class="btn btn-primary fw-semibold" @click="answer_exam" :disabled="on_sending" v-if="!on_sending">Gönder</button>
      <button class="btn btn-primary" type="button" disabled v-else>
        <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
        <span role="status">Gönderiliyor...</span>
      </button>
  </section>
</template>

<style>

</style>