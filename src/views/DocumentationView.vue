<template>
    <div class="flex flex-col space-y-6 mx-12 mt-8">
        <!-- Carte avec système interactif -->
        <UCard :ui="{'root': 'ring-emerald-500 ring-4 divide-cyan-500 divide-y-4'}">
            <template #header>
                <h1 class="text-center text-2xl text-cyan-500 font-black">Assistant Virtuel</h1>
            </template>
            <div class="p-4 flex flex-col space-y-4">
                <UInput v-model="question" placeholder="Posez votre question..." class="w-full" @keyup.enter="askQuestion" />
                <UButton label="Envoyer" @click="askQuestion" size="lg"/>
                <div v-if="answer" class="p-4 border rounded-xl bg-gray-800 text-gray-300">
                    <div v-html="answer"></div>
                </div>
            </div>
        </UCard>
        
        <!-- Liste des fichiers -->
        <UCard :ui="{'root': 'ring-emerald-500 ring-4 divide-cyan-500 divide-y-4'}">
            <template #header>
                <h1 class="text-center text-2xl text-cyan-500 font-black">Tous les Fichiers</h1>
            </template>
            <div class="flex flex-col space-y-4 p-4 text-center">
                <div v-for="file in files" :key="file" class="p-2 rounded-xl text-gray-300 text-lg font-bold ring-2 ring-emerald-500 w-fit">
                    <h2 class="text-xl text-cyan-500 font-bold uppercase">{{ file.name.replace(".md", "") }}</h2>
                    <UButton label="Voir" size="xl" @click="openModal(file.content)" class="w-32 mx-auto"/>
                </div>
            </div>
        </UCard>
    </div>

    <UModal v-model:open="isModalOpen" :ui="{'root': 'bg-gray-900 z-20'}">
        <template #content>
            <div class="h-48 m-4 overflow-auto text-gray-300" v-html="fileContent"></div>
        </template>
    </UModal>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { ofetch } from 'ofetch';
import { useStorage } from '@/stores/storage';
import { joinURL } from 'ufo';
import { useHead } from 'unhead';
import { marked } from 'marked';

const storage = useStorage();
useHead({ title: "Documentation" });

const files = ref([]);
const isModalOpen = ref(false);
const fileContent = ref('');
const question = ref('');
const answer = ref('');

onMounted(() => {
    ofetch(joinURL(storage.baseURL, "/api/docs/files")).then(res => {
        files.value = res;
    }).catch(err => console.error(err));
});

onUnmounted(() => {
    files.value = [];
});

const openModal = (content) => {
    fileContent.value = marked(content);
    isModalOpen.value = true;
};

const askQuestion = async () => {
    if (!question.value.trim()) return;
    try {
        const response = await fetch(joinURL(storage.baseURL, "/api/ai/ask"), {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question: question.value })
        });
        const data = await response.json();
        answer.value = marked(data.answer || "Aucune réponse reçue.");
    } catch (error) {
        console.error("Erreur API :", error);
        answer.value = "Erreur lors de la récupération de la réponse.";
    }
};
</script>
