import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'
import ExamListView from '../views/ExamListView.vue'
import NotFound from "@/views/NotFoundView.vue";

const routes = [
  {
    path: '/',
    name: 'home',
    component: ExamListView
  },
  {
    path: '/auth',
    component: () => import(/* webpackChunkName: "about" */ '../views/auth/AuthView.vue'),
    children: [
      {
        path: 'login/',
        name: 'login',
        component: () => import(/* webpackChunkName: "login" */ '../views/auth/LoginView.vue')
      },
      {
        path: 'register/',
        name: 'register',
        component: () => import(/* webpackChunkName: "register" */ '../views/auth/RegisterView.vue')
      },
      {
        path: 'email/confirmation/:token/',
        name: 'confirmation',
        component: () => import(/* webpackChunkName: "confirmation" */ '../views/auth/email_confirmation_view.vue')
      },
      {
        path: 'forget-password/',
        name: 'forget-password',
        component: () => import(/* webpackChunkName: "forget-password" */ '../views/auth/PasswordRestRequest.vue')
      },
      {
        path: 'reset-password/',
        name: 'reset-password',
        component: () => import(/* webpackChunkName: "reset-password" */ '../views/auth/PasswordResetFormView.vue')
      },
    ]

  },

  {
    path: '/results/',
    name: 'results',
    component: () => import(/* webpackChunkName: "about" */ '../views/ResultsView.vue')
  },
  {
    path: '/exam',
    name: 'exam_list',
    component: ExamListView
  },
  {
    path: '/exam/:slug',
    name: 'exam',
    component: () => import(/* webpackChunkName: "about" */ '../views/ExamView.vue')
  },
  { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound }
]

// const router = createRouter({
//   history: createWebHashHistory(),
//   // routes
// })


const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
