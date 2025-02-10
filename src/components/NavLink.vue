<template>
  <li class="w-full flex items-center">
    <template v-if="isExternal">
      <a :href="url" class="md:px-4 py-2 text-sm bg-transparent rounded-lg text-[#666666] hover:text-gray-900 focus:outline-none focus:shadow-outline" target="_blank" rel="noopener noreferrer">
        {{ name }}
      </a>
    </template>
    <template v-else>
      <RouterLink class="md:px-4 py-2 text-sm bg-transparent rounded-lg text-[#666666] hover:text-gray-900 focus:outline-none focus:shadow-outline" :to="url">
        {{ name }}
      </RouterLink>
    </template>
  </li>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { computed } from 'vue'

const props = defineProps({
  name: {
    type: String,
    required: true,
  },
  url: {
    type: String,
    required: true,
  },

})

const isExternal = computed(() => props.url.startsWith('http'))
</script>
