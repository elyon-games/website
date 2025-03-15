<template>
    <UCard :ui="{'root': 'ring-emerald-500 ring-4 divide-cyan-500 divide-y-4 mx-12'}">
        <template #header>
            <h1 class="text-center text-2xl text-cyan-500 font-black">Dernière Version</h1>
            <div class="flex flex-col items-center" v-if="latestVersion !== null">
                <UButton :label="`Télécharger la version ${latestVersion.name}`" class="mt-2" external block size="xl" target="_blank" :href="latestVersion.url"/>
            </div>
        </template>
        <template #footer>
            <h1 class="text-center text-2xl text-cyan-500 font-black pb-4">Tout Nos Versions</h1>
            <div class="flex flex-col">
                <UAccordion :items="versions.map((value) => {
                    return {
                        label: value.name,
                        ...value
                    }
                })" :ui="{
                    'item': 'border-emerald-500 border-b-4',
                }">
                    <template #default="{ item }">
                        <h1 class="text-xl text-cyan-500 font-bold uppercase">Version {{ item.label }}</h1>
                    </template>
                    <template #body="{ item }">
                        <div class="flex flex-col space-y-1.5 text-center justify-center text-gray-300 text-lg font-bold">
                            <h2 class="flex-1">Taille : <span class="text-emerald-500">{{ formatSize(item.size) }}</span></h2>
                            <h2 class="flex-1">MD5 : <span class="text-emerald-500">{{ item.md5 }}</span></h2>
                            <UButton label="Télécharger" external target="_blank" size="xl" :href="item.url" class="flex-1 mx-auto w-96 content-center justify-center"/>
                        </div>
                    </template>
                </UAccordion>
            </div>
        </template>
    </UCard>
</template>

<script setup>
import { useStorage } from '@/stores/storage';
import { ofetch } from 'ofetch';
import { joinURL } from 'ufo';
import { useHead } from 'unhead';
import { onMounted, onUnmounted, ref } from 'vue';
const storage = useStorage();
useHead({
    title: "Télécharger"
})
const versions = ref([]);
const latestVersion = ref(null);


onMounted(() => {
    ofetch(joinURL(storage.baseURL, "/api/versions"), {
        baseURL: storage.baseURL
    }).then((res) => {
        versions.value = res.sort(compareVersions).reverse();
        latestVersion.value = versions.value[0];
    }).catch((err) => {
        console.error(err);
        useToast().add({
            title: "Erreur",
            message: "Impossible de récupérer les versions",
            color: "red"
        })
    });
})

onUnmounted(() => {
    versions.value = [];
    latestVersion.value = null;
})

function compareVersions(v1, v2) {
    const v1Parts = v1.name.split('.').map(Number);
    const v2Parts = v2.name.split('.').map(Number);
    for (let i = 0; i < v1Parts.length; i++) {
        if (v1Parts[i] > v2Parts[i]) return 1;
        if (v1Parts[i] < v2Parts[i]) return -1;
    }
    return 0;
}

function formatSize(size) {
    const i = Math.floor(Math.log(size) / Math.log(1024));
    return (size / Math.pow(1024, i)).toFixed(2) * 1 + ' ' + ['B', 'kB', 'MB', 'GB', 'TB'][i];
}
</script>
