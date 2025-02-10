<template>
  <nav id="navbar" class="relative z-10 w-full text-neutral-800">
    <div class="flex flex-col max-w-screen-xl px-8 mx-auto lg:items-center lg:justify-between lg:flex-row py-4">
      <div class="flex flex-col lg:flex-row items-center space-x-4 xl:space-x-8">
        <div class="w-full flex flex-row items-center justify-between py-6">
          <div>
            <img src="@/assets/img/logo/icon.png" class="w-14 xl:w-18" alt="Elyon Games Logo" @click="router.push({
              'path': '/'
            })" />
          </div>
          <button class="rounded-lg lg:hidden focus:outline-none focus:shadow-outline" @click="open = !open">
            <Icon name="ph:list" v-if="!open" class="text-white" :size="24" />
            <Icon name="ph:x" v-else class="text-white" :size="24" />
          </button>
        </div>
        <ul
            :class="[open ? 'flex' : 'hidden lg:flex']"
            class="w-full h-auto flex flex-col flex-grow lg:items-center pb-4 lg:pb-0 lg:justify-end lg:flex-row origin-top duration-300 xl:space-x-2 space-y-3 lg:space-y-0"
          >
          <UButton size="xl" label="Télécharger" variant="link" icon="oui:download" to="/download"/>
          <UButton size="xl" label="Serveur" variant="link" icon="mdi:server" to="/server"/>
          <UButton size="xl" label="Documentation" variant="link" icon="oui:documentation" to="/documentation"/>
          <UButton size="xl" label="Notre équipe" variant="link" icon="mdi:account-group" to="/team"/>
          <UButton size="xl" label="Github" variant="link" icon="mdi:github" to="/github"/>
        </ul>
      </div>
    </div>
  </nav>
</template>
<script setup>
import { useRouter } from 'vue-router'
import { ref } from 'vue'
const router = useRouter()
const dropdownNavbar = ref(false)
const open = ref(false)
const dropdownToggler = () => {
  dropdownNavbar.value = !dropdownNavbar.value
}
</script>