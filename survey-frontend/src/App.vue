<!--<script setup>-->
<!--import Notifications from "@kyvg/vue3-notification";-->
<!--const components = [Notifications]-->
<!--</script>-->

<script>
import { defineComponent } from 'vue';
import Navbar from "@/components/navbar.vue";

window.addEventListener('scroll', () => {
  const divs = document.querySelectorAll('.product-card');
  divs.forEach((div) => {
    const rect = div.getBoundingClientRect();
    if (rect.top >= 0 && rect.bottom <= window.innerHeight) {
      window.scrollTo({
        top: div.offsetTop,
        behavior: 'smooth'
      });
    }
  });
});

export default defineComponent({
  name: 'app',
  components: {Navbar},
})
</script>

<template>
<!--  <navbar></navbar>-->
  <main class="" style="">
    <router-view />
  </main>
  <notifications position="bottom left" />
</template>

<style>
html, body {
  margin: 0;
  padding: 0;
  scroll-behavior: smooth;
}
</style>
