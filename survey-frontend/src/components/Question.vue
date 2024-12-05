<template>
  <div>
    <p>{{ text }}</p>
    <div>
    </div>
  </div>
</template>

<script setup>
import Knob from 'primevue/knob';
import { ref, onMounted, getCurrentInstance } from 'vue';

const props = defineProps({
  text: String
});

const value = ref(0);

onMounted(() => {
  const instance = getCurrentInstance(); // Component instance'ını al

  if (instance) {
    instance.emit('ref', value); // Ref'i parent component'e emit et
  }
});
</script>
