<template>
  <div class="w-full">
    <!-- Hero section -->
    <section id="hero" class="w-full pb-24">
      <BaseSection>
        <div class="col-span-12 lg:col-span-6 mt-12 xl:mt-10 space-y-4 sm:space-y-6 px-6 text-center sm:text-left">
          <span data-aos="fade-right" data-aos-once="true" class="text-base font-bold uppercase text-orange-400" 
          @click="router.push({ path: '/trophe-nsi' })">
            Trophe NSI 2025
          </span>
          <h1
            data-aos="fade-right"
            data-aos-once="true"
            class="text-[2.5rem] sm:text-5xl xl:text-6xl font-bold leading-tight sm:pr-8 xl:pr-10 text-blue-500">
            Bienvenue sur <span class="text-emerald-400">Elyon</span>
          </h1>
          <p data-aos="fade-down" data-aos-once="true" data-aos-delay="300" class="hidden sm:block text-gray-300 text-lg">
            Elyon est une plateforme de mini-jeux en multi-joueurs entièrement gratuit et open-source.
          </p>
          <div
            data-aos="fade-up"
            data-aos-once="true"
            data-aos-delay="700"
            class="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-4 mt-2">
            <BaseButton to="/download" class="max-w-full px-8 py-4 bg-gradient-to-r from-[#468ef9] to-[#0c66ee] border border-[#0c66ee] text-white text-center">
              Télécharger l'application
            </BaseButton>
            <BaseButton @click="router.push({ hash: '#presentation' })"
              class="max-w-full px-6 py-4 bg-inherit text-gradient border border-[#0c66ee] flex items-center justify-center"
            >
              <span>En savoir plus</span>
            </BaseButton>
          </div>
        </div>
        <div class="sm:block col-span-12 lg:col-span-6">
          <div class="w-full">
            <img
              data-aos="fade-up"
              data-aos-once="true"
              src="@/assets/img/hero.webp"
              class="mt-4 rounded-2xl"
              alt=""
            />
          </div>
        </div>
        <img
          data-aos="fade-up"
          data-aos-delay="300"
          src="@/assets/img/pattern/star.png"
          class="hidden sm:block absolute bottom-12 xl:bottom-16 left-4 xl:left-0 w-6"
        />
      </BaseSection>
    </section>

    <!-- Credit card section -->
    <section class="w-full my-36" id="presentation">
      <BaseSection data-aos="fade-down">
        <div class="col-span-12 lg:col-span-7">
          <div class="w-full">
            <img src="https://cdn.younity-mc.fr/fond" class="w-[95%] rounded-xl" alt="" />
          </div>
        </div>
        <div class="col-span-12 lg:col-span-5 space-y-6 px-4 sm:px-6 mt-20">
          <h2 class="text-4xl font-semibold text-emerald-400">
            Présentation
          </h2>
          <p class="text-gray-400">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ad consequuntur doloribus nisi animi minus perspiciatis neque voluptates, dolores maiores vero, autem rerum atque modi obcaecati repellendus itaque, adipisci id non.</p>
          <!-- <ul class="space-y-4 sm:space-y-2">
            <LandingListItem title="No annual fee" />
          </ul> -->
        </div>
      </BaseSection>
    </section>

    <!-- Advanced trading tools section -->
    <section class="bg-trading-tools relative max-w-full sm:mx-4 my-20 py-16 shadow rounded-2xl overflow-hidden">
      <div class="relative max-w-screen-xl px-4 sm:px-2 mx-auto grid grid-cols-12 gap-x-6">
        <div class="sm:hidden"></div>
          <div data-aos="fade-right" class="col-span-12 lg:col-span-6 space-y-8 sm:space-y-6 px-4 sm:px-6 mt-8">
            <h2 class="text-4xl font-semibold text-emerald-400">L'Histoire du projet</h2>
            <div class="space-y-2">
              <h4 class="text-lg font-medium text-gray-200">Lorem ipsum, dolor sit amet consectetur</h4>
              <p class="text-sm xl:text-base text-gray-300">
                Lorem ipsum, dolor sit amet consectetur adipisicing elit. Tenetur unde pariatur repellat autem itaque possimus impedit nulla? Suscipit cumque quia, amet a atque nostrum, repellat quo voluptatem nisi quod eaque.
              </p>
            </div>
          </div>
        <div data-aos="fade-left" class="hidden sm:block"></div>
      </div>
    </section>

    <!-- FAQ section -->
    <section class="w-full my-24">
      <BaseSection>
        <div data-aos="fade-right" data-aos-delay="150" class="col-span-12 lg:col-span-6">
          <div class="w-ful">
            <img src="@/assets/img/faq.png" class="w-full rounded-xl" alt="" />
          </div>
        </div>
        <div data-aos="fade-left" data-aos-delay="150" class="col-span-12 lg:col-span-6 px-4 sm:px-6 mt-8">
          <span class="text-base text-gradient font-semibold uppercase mb-4 sm:mb-2 text-blue-500">Support</span>
          <h2 class="text-3xl sm:text-4xl font-semibold mb-10 sm:mb-6 text-emerald-400">Questions Fréquemment Posées</h2>

          <ul class="shadow-box">
            <BaseAccordion v-for="(ask, index) in faq" :key="index" :accordion="ask" />
          </ul>
        </div>
      </BaseSection>
    </section>

    <div class="w-full my-10 flex justify-center">
      <a
        v-smooth-scroll
        data-aos="flip-down"
        data-aos-delay="150"
        href="#navbar"
        class="px-6 py-3 flex items-center space-x-2 bg-[#FAFAFA] hover:bg-gray-100 hover:shadow-md border border-[#DDDDDD] rounded-md text-gray-700"
      >
        <span>Revenir en haut</span>
        <ArrowUpIcon :size="20" />
      </a>
    </div>
  </div>
</template>

<script setup>
import { ofetch } from 'ofetch'
import { useHead } from 'unhead'
import BaseSection from '@/components/base/Section.vue'
import BaseButton from '@/components/base/Button.vue'
import LandingListItem from '@/components/landing/ListItem.vue'
import BaseAccordion from '@/components/base/Accordion.vue'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

useHead({
  title: "Accueil"
})

const router = useRouter()
const faq = ref([
  {
    title: 'Why should I choose NEFA?',
    description:
      "We're industry pioneers, having been in the cryptocurrency industry since 2016. We've facilitated more than 21 billion USD worth of transactions on our exchange for customers in over 40 countries. Today, we're trusted by over 8 million customers around the world and have received praise for our easy-to-use app, secure wallet, and range of features.",
  }
]);
</script>

<style>
.cover-gradient {
  background: linear-gradient(
    169.4deg,
    rgba(57, 132, 244, 0.04) -6.01%,
    rgba(12, 211, 255, 0.04) 36.87%,
    rgba(47, 124, 240, 0.04) 78.04%,
    rgba(14, 101, 232, 0.04) 103.77%
  );
}
.cover-gradient-2 {
  background: linear-gradient(
    169.4deg,
    rgba(57, 132, 244, 0.1) -6.01%,
    rgba(12, 211, 255, 0.1) 36.87%,
    rgba(47, 124, 240, 0.1) 78.04%,
    rgba(14, 101, 232, 0.1) 103.77%
  );
}
.bg-blue-gradient,
.text-gradient {
  background: linear-gradient(136.91deg, #468ef9 -12.5%, #0c66ee 107.5%);
}
.text-gradient {
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.slide-enter-active {
  -moz-transition-duration: 0.3s;
  -webkit-transition-duration: 0.3s;
  -o-transition-duration: 0.3s;
  transition-duration: 0.3s;
  -moz-transition-timing-function: ease-in;
  -webkit-transition-timing-function: ease-in;
  -o-transition-timing-function: ease-in;
  transition-timing-function: ease-in;
}

.slide-leave-active {
  -moz-transition-duration: 0.3s;
  -webkit-transition-duration: 0.3s;
  -o-transition-duration: 0.3s;
  transition-duration: 0.3s;
  -moz-transition-timing-function: cubic-bezier(0, 1, 0.5, 1);
  -webkit-transition-timing-function: cubic-bezier(0, 1, 0.5, 1);
  -o-transition-timing-function: cubic-bezier(0, 1, 0.5, 1);
  transition-timing-function: cubic-bezier(0, 1, 0.5, 1);
}

.slide-enter-to,
.slide-leave {
  max-height: 100px;
  overflow: hidden;
}

.slide-enter,
.slide-leave-to {
  overflow: hidden;
  max-height: 0;
}
</style>
