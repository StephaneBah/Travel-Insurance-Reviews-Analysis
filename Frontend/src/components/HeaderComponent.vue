<template>
    <header class="w-full flex items-center z-50 justify-center relative p-[20px]">
        <div class="w-full relative flex items-center justify-center p-[10px] text-gray-200 bg-gray-800 max-w-[400px] rounded-[20px]">
            <div @click="gotodashboardpage()" class="w-[50%] text-center text-xs font-bold hover:bg-gray-700 p-[10px] rounded-[10px] cursor-pointer" :class="{'bg-gray-200 text-gray-800 hover:bg-gray-200': $route.path == '/'}">Tableau de bord</div>
            <div @click="gotopredictionpage()" class="w-[50%] text-center text-xs font-bold hover:bg-gray-700 p-[10px] rounded-[10px] cursor-pointer" :class="{'bg-gray-200 text-gray-800 hover:bg-gray-200': $route.path == '/prediction'}">Prédiction</div>
        </div>
    </header>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router';

const router = useRouter()

function gotodashboardpage() {
    router.push("/")
}
function gotopredictionpage() {
    router.push("/prediction")
}
</script>

<style>

</style>