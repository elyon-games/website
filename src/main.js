import './assets/css/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { useStorage } from './stores/storage'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { WatchPiniaPlugin } from 'pinia-plugin-watch';
import ui from '@nuxt/ui/vue-plugin'
import { createHead, useHead } from 'unhead'
import vueSmoothScroll from 'vue3-smooth-scroll'

import App from './App.vue'
import routerManger from './router'

import aosMixin from '@/mixins/aos'

import Particles from "@tsparticles/vue3";
import { loadFull } from "tsparticles";

import ChevronDownIcon from 'vue-material-design-icons/ChevronDown.vue'
import ChevronUpIcon from 'vue-material-design-icons/ChevronUp.vue'
import ChevronRightIcon from 'vue-material-design-icons/ChevronRight.vue'
import PlusThickIcon from 'vue-material-design-icons/PlusThick.vue'
import MinusThickIcon from 'vue-material-design-icons/MinusThick.vue'
import ArrowUpIcon from 'vue-material-design-icons/ArrowUp.vue'
import ArrowRightIcon from 'vue-material-design-icons/ArrowRight.vue'
import CheckCircleIcon from 'vue-material-design-icons/CheckCircle.vue'
import SegmentIcon from 'vue-material-design-icons/Segment.vue'
import CloseIcon from 'vue-material-design-icons/Close.vue'

const components = { ChevronDownIcon, ChevronUpIcon, ChevronRightIcon, PlusThickIcon, MinusThickIcon, ArrowUpIcon, ArrowRightIcon, CheckCircleIcon, SegmentIcon, CloseIcon }

const app = createApp(App)
const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)
pinia.use(WatchPiniaPlugin)
app.use(pinia)
app.use(routerManger)
app.use(ui)
app.use(vueSmoothScroll)

app.use(Particles, {
    init: async engine => {
        await loadFull(engine);
    },
});

Object.entries(components).forEach(([name, component]) => {
    app.component(name, component)
})

app.mixin(aosMixin)

createHead()
useHead({
    titleTemplate: (title) => {
        return title ? `Elyon Games | ${title}` : 'Elyon Games'
    }
})

let api_url
const element_api_url = document.getElementsByTagName("api_url")
if (import.meta.env.DEV) {
    api_url = "http://127.0.0.1:5400"
} else {
    api_url = element_api_url[0].textContent
}

const storage = useStorage()
storage.baseURL = api_url

app.mount('#app')