<script setup>
import { onMounted, ref } from "vue"
import { LottieAnimation } from "lottie-web-vue"
import WatermelonJSON from "../assets/anim/error_anim.json"

let anim = ref()

onMounted(() => {
  setTimeout(() => {
    anim.value.goToAndPlay(150, true)
    anim.value
  }, 500)
})

// called after each loop
// const loopComplete = () => {
//   console.log('Loop complete')
// }
//
// // called after first loop
// const complete = () => {
//   console.log('First loop complete')
// }
//
// // called after first frame entered
// const enterFrame = () => {
//   console.log('Entered first frame')
// }

// called after segment started
// const segmentStart = () => {
//   console.log('Segment started')
// }
//
// // called after animation stopped
// const stopped = () => {
//   console.log('Stopped')
// }
</script>
<template>
  <div class="container h-50 w-50">
    <LottieAnimation
        ref="anim"
        :animation-data="WatermelonJSON"
        :loop="true"
        :auto-play="true"
        :speed="1"
    />
  </div>
</template>


<!--      @loopComplete="loopComplete"-->
<!--      @complete="complete"-->
<!--      @enterFrame="enterFrame"-->

<!--@segmentStart="segmentStart"-->
<!--@stopped="stopped"/>-->