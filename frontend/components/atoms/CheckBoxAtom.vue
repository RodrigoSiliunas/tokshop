<script>
export default {
  props: {
    label: { type: String, required: true },
  },
};
</script>

<template>
  <div class="form-check">
    <input
      class="form-check-input"
      type="checkbox"
      value=""
    />
    <label class="form-check-label">{{ label }}</label>
  </div>
</template>
