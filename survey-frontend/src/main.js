import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'
import PrimeVue from 'primevue/config';

import store from './store'
import axios from "axios";
import AuthService from "@/AuthService";
// import VueSession from 'vue-session'
import Notifications from '@kyvg/vue3-notification'
// import LottieAnimation from 'lottie-web-vue'

const carrier_switch = 'Bearer'

// axios.defaults.baseURL = process.env.VUE_APP_API_HOST
axios.defaults.baseURL = 'http://127.0.0.1:8000/api/'
const API_URL = 'http://127.0.0.1:8000/api/'
axios.interceptors.request.use(
    ( config ) => {
        console.log('config')
        config.headers["Authorization"] = `${carrier_switch} ${AuthService.getAccessToken()}`;
        return config;
    });

axios.interceptors.response.use(
    (response) =>{
        return response
    }, error => {
        // console.error('Error in response:', error);
        const originalRequest = error.config;
        if (error.response.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;

            return  AuthService.refreshToken()
            .then((newAccessToken) => {
                originalRequest.headers['Authorization'] = `${carrier_switch} ${newAccessToken}` ;
                return axios(originalRequest);
            })
            .catch((refreshError) => {
                AuthService.logout()
                return Promise.reject(refreshError); // Reject the promise to propagate the error further

            })
        }
        return Promise.reject(error);
    }
)

// import './assets/main.css'

createApp(App)
    .use(router)
    .use(store)
    .use(Notifications)
    // .use(LottieAnimation)
    // .use(VueSession)
    .use(PrimeVue)
    .mount('#app')


import 'bootstrap/dist/js/bootstrap'

