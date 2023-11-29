<template>
  <button
    class="btn btn-primary btn-lg fw-bolder rounded-0"
    :type="type"
    @click="$emit('onClick')"
  >
    <i class="me-2" :class="icon" v-if="icon"></i>{{ text }}
  </button>
</template>

<script>
export default {
  props: {
    text: { type: String, required: true },
    type: { type: String, default: "button" },
    icon: { type: String },
  },
};
</script>
