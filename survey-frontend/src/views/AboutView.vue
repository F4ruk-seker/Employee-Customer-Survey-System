<template>
  <div class="knob" :style="{ transform: `rotate(${angle}deg)` }">
    <div class="knob-base"></div>
    <div class="knob-handle" @mousedown="startDrag"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      angle: 0,
      isDragging: false,
      startAngle: 0,
    };
  },
  methods: {
    startDrag(event) {
      this.isDragging = true;
      this.startAngle = this.angle - this.getMouseAngle(event);
      document.addEventListener("mousemove", this.drag);
      document.addEventListener("mouseup", this.stopDrag);
    },
    drag(event) {
      if (this.isDragging) {
        const newAngle = this.getMouseAngle(event) + this.startAngle;
        this.angle = newAngle;
        // You can emit an event or update a data property with the new value here.
      }
    },
    stopDrag() {
      this.isDragging = false;
      document.removeEventListener("mousemove", this.drag);
      document.removeEventListener("mouseup", this.stopDrag);
    },
    getMouseAngle(event) {
      const knob = this.$el;
      const knobRect = knob.getBoundingClientRect();
      const centerX = knobRect.left + knobRect.width / 2;
      const centerY = knobRect.top + knobRect.height / 2;
      const deltaX = event.clientX - centerX;
      const deltaY = event.clientY - centerY;
      return (Math.atan2(deltaY, deltaX) * 180) / Math.PI;
    },
  },
};
</script>

<style scoped>
.knob {
  position: relative;
  width: 100px;
  height: 100px;
}

.knob-base {
  background-color: #ccc;
  border-radius: 50%;
  width: 100%;
  height: 100%;
}

.knob-handle {
  position: absolute;
  background-color: #3498db;
  width: 50%;
  height: 10px;
  top: 50%;
  left: 50%;
  transform: translateX(-50%) translateY(-50%);
  cursor: pointer;
}
</style>
