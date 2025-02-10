<template>
  <footer class="max-w-screen-xl px-8 mt-10 mx-auto w-[52rem] border-y-2 border-gray-200">
    <div class="py-8 sm:py-4 font-bold text-center text-sm text-gray-400">
      &copy; Copyright 2024-{{ dayjs().year() }} <span class="text-emerald-400">Elyon Games</span> 
      by <span class="text-orange-500">Younity MC</span>. All rights reserved
    </div>
  </footer>
</template>
<script setup>
import dayjs from 'dayjs';
import { useRouter } from 'vue-router';
const router = useRouter()
</script>
