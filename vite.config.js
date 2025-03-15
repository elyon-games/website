import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import ui from '@nuxt/ui/vite'

export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
    ui({
      colorMode: false
    })
  ],
  css: ['aos/dist/aos.css'],
  build: {
    emptyOutDir: true,
    outDir: './build/web',
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})
