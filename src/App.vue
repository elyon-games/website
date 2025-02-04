<template>
  <UApp>
    <RouterView />
  </UApp>
</template>
<script setup>
import { useHead } from 'unhead'
import { RouterLink, RouterView } from 'vue-router'
useHead({
  titleTemplate: (title) => title ? `Elyon Games | ${title}` : 'Elyon Games',
})
</script>