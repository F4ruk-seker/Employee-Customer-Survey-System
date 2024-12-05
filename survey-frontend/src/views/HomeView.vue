<template>
<section class="bg-secondary d-flex z-2" style="height: 100vh; background: url('/pars.png') no-repeat center; background-size: cover">
  <div class="d-flex position-absolute justify-content-between w-100 fw-bold text-light p-3">
    <div>#LOGO</div>
    <div class="w-100"></div>
    <div>Sections</div>
  </div>
  <div class="container d-flex border border-dark py-2 rounded my-auto">
    <div class="w-50">
      <LottieAnimation
          ref="anim"
          :animation-data="WatermelonJSON"
          :loop="true"
          :auto-play="true"
          :speed="1"
      />
    </div>
    <div class="w-50 d-flex">
      <strong class="fw-bold text-light m-auto">
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Distinctio, fugit. <a href="#view">VIEW</a>
      </strong>
    </div>
  </div>
 </section>
<section>
  <article class="d-flex" style="height: 100vh; justify-content: center; align-items: center" id="view">
    <div class="row m-0 p-0 container">
      <div class="col-12 col-md-6 border-end">
        <div class="w-100 bg-secondary rounded text-center" style="height: 300px; background: url('/hirem.jpg') no-repeat center; background-size: cover">
        </div>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias, aliquid aspernatur culpa ducimus fugiat impedit ipsam laborum officia rem totam. Adipisci aspernatur dignissimos distinctio ipsum minus, neque nulla vero. Aliquam deleniti dignissimos dolorum eaque expedita illum, ipsam recusandae temporibus unde veritatis voluptate voluptatum. Accusamus aperiam at illo ipsam magni nam non sit voluptatum. Alias aliquid dolore, dolorum ea, id inventore ipsum iste reiciendis repudiandae rerum sapiente soluta tenetur vitae. Atque dignissimos id impedit inventore qui quisquam reiciendis ullam voluptas! Blanditiis dignissimos expedita illo ipsum nostrum quam reprehenderit temporibus. A, aut ex facere iste magnam maxime numquam quasi tempora temporibus unde.
        </p>
        <a href="#select-products" class="border rounded  py-2 px-3 text-info fw-semibold text-decoration-none">GO Start</a>
      </div>
      <div class="col-12 col-md-6 my-auto">
        <div class="d-flex mb-3">
          <div class="border border-primary-subtle rounded-circle d-flex" style="min-width: 100px; min-height: 100px; max-width: 100px; max-height: 100px; font-size: 40px">
            <i class="fa-solid fa-database m-auto text-primary-emphasis"></i>
          </div>
          <div class="ms-1 my-auto" style="width: max-content;">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque deleniti esse maiores modi molestias nulla obcaecati quis, quod similique vitae. Amet animi asperiores deserunt eum ex exercitationem inventore ipsa minima molestias nisi odio, quasi sapiente sequi suscipit veniam voluptas voluptatem.
          </div>
        </div>
        <div class="d-flex mb-3">
          <div class="border border-warning rounded-circle d-flex" style="min-width: 100px; min-height: 100px; max-width: 100px; max-height: 100px; font-size: 40px">
            <i class="fa-solid fa-magnifying-glass-chart text-warning m-auto ps-1"></i>
          </div>
          <div class="ms-1 my-auto" style="width: max-content;">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque deleniti esse maiores modi molestias nulla obcaecati quis, quod similique vitae. Amet animi asperiores deserunt eum ex exercitationem inventore ipsa minima molestias nisi odio, quasi sapiente sequi suscipit veniam voluptas voluptatem.
          </div>
        </div>


      </div>
    </div>
  </article>
  <article class="py-5 my-auto" style="height: 100vh" id="select-products">
    <div class="d-flex border-dark border-top border-bottom">
      <strong class="border-dark border-end pe-1 py-2 w-25 text-center">Brand</strong>
    </div>
    <div class="row m-0 p-0 text-center">
      <div class="col-6 col-md-3 py-3 border-dark border-end border-bottom">x</div>
      <div class="col-6 col-md-3 py-3 border-dark border-end border-bottom">x</div>
      <div class="col-6 col-md-3 py-3 border-dark border-end border-bottom">x</div>
      <div class="col-6 col-md-3 py-3 border-dark border-end border-bottom">x</div>
      <div class="col-6 col-md-3 py-3 border-secondary border-end border-bottom">x</div>
      <div class="col-6 col-md-3 py-3 border-danger border-end border-bottom">x</div>
    </div>
  </article>
</section>
</template>

<script setup>
import { LottieAnimation } from "lottie-web-vue"
import ZedNavbar from "@/components/ZedNavbar.vue";
import WatermelonJSON from "@/assets/anim/data_anim.json";
</script>
