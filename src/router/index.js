import { createRouter, createWebHistory, useRouter } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import NotFound from "../views/NotFound.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: "/download",
      name: "download",
      component: () => import("@/views/DownloadView.vue")
    },
    {
      path: "/server",
      name: "server",
      component: () => import("@/views/ServerView.vue")
    },
    {
      path: "/team",
      name: "team",
      component: () => import("@/views/TeamView.vue")
    },
    {
      path: "/documentation",
      name: "documentation",
      component: () => import("@/views/DocumentationView.vue")
    },
    {
      path: "/github",
      name: "github",
      beforeEnter() {
        window.open("https://github.com/elyon-games", "_blank")
        useRouter().push('/')
      }
    },
    {
      path: "/trophe-nsi",
      name: "trophe-nsi",
      beforeEnter(){
        window.open("https://trophees-nsi.fr/", "_blank")
        useRouter().push("/")
      }
    },
    {
      path: "/younity",
      name: "younity",
      beforeEnter(){
        window.open("https://www.younity-mc.fr", "_blank")
        useRouter().push("/")
      }
    },
    { path: '/:pathMatch(.*)*', component: NotFound }
  ],
})

export default router
