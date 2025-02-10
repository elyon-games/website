import { defineStore } from "pinia";
import { ref } from "vue";

export const useStorage = defineStore("storage", () => {
    const baseURL = ref("")
    return {
        baseURL
    }
})