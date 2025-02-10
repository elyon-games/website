<template>
  <UButton variant="link"
    class="text-sm text-center rounded-full hover:shadow-md hover:shadow-[#0c66ee]/50 transition duration-300"
    v-bind="$attrs"
    v-on="$listeners"
    :to="to"
  >
    <slot></slot>
  </UButton>
</template>
<script setup>
defineProps({
  to: {
    type: String,
    default: '/'
  }
})

</script>
