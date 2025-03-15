<template>
    <div class="container mx-auto">
        <UCard :ui="{'root': 'ring-emerald-500 ring-4 divide-cyan-500 divide-y-4'}">
            <template #header>
                <h1 class="text-center text-2xl text-cyan-500 font-black">Serveur Officiel</h1>
            </template>
            <div class="p-4 text-center text-lg text-gray-700">
                Nous proposons un serveur officiel qui est géré par nous.
            </div>
            <div class="p-4 text-center">
                <a href="https://play.elyon.younity-mc.fr" class="text-cyan-500 underline" target="_blank" rel="noopener noreferrer">
                    Aller voir la page des stats
                </a>
            </div>
        </UCard>
    </div>
</template>
<script setup>
import { useHead } from 'unhead';
useHead({
    title: "Serveur Officiel"
})
</script>