<template>
    <vue-particles class="z-[-1] fixed inset-0" id="tsparticles" :options="particule"/>
</template>
<script setup>
import { ref } from "vue";
import configs from "@tsparticles/configs";
const particule = ref({
    fpsLimit: 120,
    interactivity: {
        modes: {
            bubble: {
                distance: 400,
                duration: 2,
                opacity: 0.8,
                size: 40
            },
            push: {
                quantity: 4
            },
            repulse: {
                distance: 200,
                duration: 0.4
            }
        }
    },
    particles: {
        color: {
            value: '#ffffff'
        },
        links: {
            color: '#ffffff',
            distance: 150,
            enable: true,
            opacity: 0.5,
            width: 1
        },
        move: {
            direction: 'none',
            enable: true,
            outModes: 'bounce',
            random: false,
            speed: 6,
            straight: false
        },
        number: {
            density: {
                enable: true,
            },
            value: 150
        },
        opacity: {
            value: 0.5
        },
        shape: {
            type: 'polygon',
            polygon: {
                sides: 6
            }
        },
        size: {
            value: { min: 1, max: 5 }
        }
    },
    detectRetina: true
});
</script>