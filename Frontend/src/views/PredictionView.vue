<template>
    <div>
        <HeaderComponent />
    </div>
    <div class="fixed top-[100px] left-[50%] z-[100] translate-x-[-50%] w-[80%] max-w-[400px] flex flex-col">
        <div v-if="errorMessage" class="text-sm w-full rounded-[5px] shadow-4xl text-white bg-red-700 my-[10px] font-bold text-center p-[20px]">
            {{ errorMessage }}
        </div>
    </div>
    <section v-if="responseGetting" class="w-full flex items-start justify-center relative min-h-[calc(100vh-100px)]">
        <div class="w-full container lg:max-w-[1024px] px-[20px] mt-[50px] relative flex items-center justify-start flex-col">
            <div class="w-full relative flex items-start my-[15px] justify-end">
                <div class="max-w-[70%] w-auto md:max-w-[400px] p-[15px] rounded-[15px] bg-gray-100 text-gray-800">
                    {{ lastAvis }}
                </div>
            </div>
            <div class="w-full relative flex flex-col items-start my-[15px] justify-start">
                <h1 class="text-xs font-bold text-gray-500 hover:text-gray-700 flex items-center justify-start mb-[10px]">
                    <svg class="mr-[5px]" xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 20 20"><path fill="currentColor" d="M14.5 1c.276 0 .5.222.5.497c0 .463.073 1.219.472 1.846c.375.588 1.083 1.136 2.528 1.136c.276 0 .5.222.5.497a.5.5 0 0 1-.5.497c-.369 0-1.14.223-1.82.742c-.663.505-1.18 1.241-1.18 2.24a.5.5 0 0 1-.5.496a.5.5 0 0 1-.5-.497c0-.5-.155-1.261-.606-1.884c-.432-.596-1.157-1.097-2.394-1.097a.5.5 0 0 1-.5-.497c0-.275.224-.497.5-.497c.512 0 1.255-.01 1.873-.367C13.437 3.785 14 3.1 14 1.497c0-.275.224-.497.5-.497M6.145 12.166l-.932 3.396c-.17.62.077 1.345.74 1.64c1.638.727 4.65 1.351 7.97.009c.71-.288 1.021-1.064.814-1.75l-.975-3.229A6.5 6.5 0 0 1 10 13.424a6.5 6.5 0 0 1-3.855-1.258m6.78-9.833c-.046.218-.107.38-.168.499a.97.97 0 0 1-.388.421c-.354.205-.831.232-1.369.232c-.828 0-1.5.667-1.5 1.49c0 .824.672 1.491 1.5 1.491c.911 0 1.336.344 1.583.685c.302.417.417.962.417 1.303a1.495 1.495 0 0 0 1.613 1.487A5.5 5.5 0 0 1 10 12.43c-3.038 0-5.5-2.448-5.5-5.467S6.962 1.497 10 1.497c1.075 0 2.077.306 2.924.836"/></svg>
                    Sentiment prédit
                </h1>
                <div class="w-[100%] text-gray-800 text-xl font-bold" :class="{'text-green-600': sentiment == 'POSITIVE', 'text-red-600': sentiment == 'NEGATIVE'}">
                    {{ sentiment }}
                </div>
            </div>
        </div>
    </section>
    <section v-else class="w-full flex items-center justify-center relative min-h-[calc(100vh-100px)]">
        <div class="w-full container lg:max-w-[1024px] px-[20px] relative flex items-center justify-center flex-col">
            <h1 class="text-2xl md:text-3xl mb-[10px] font-bold text-gray-800">
                Donnez votre avis !
            </h1>
            <form @submit.prevent="predictSentiment()" class="w-full max-w-[800px] relative flex flex-col">
                <div class="w-full relative my-[15px]">
                    <textarea v-model="avis" class="h-[120px] w-full outline-none text-sm p-[10px] rounded-[20px] border border-gray-200 bg-gray-100 resize-none" placeholder="Votre avis !!"></textarea>
                    <button type="submit" class="w-[30px] h-[30px] rounded-[50px] bg-gray-800 text-white flex items-center justify-center absolute right-[10px] bottom-[15px]">
                        <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24"><path fill="currentColor" d="M11 5.825L6.4 10.4L5 9l7-7l7 7l-1.4 1.425l-4.6-4.6V13h-2zM11 18v-3h2v3zm0 4v-2h2v2z"/></svg>
                    </button>
                </div>
            </form>
        </div>
    </section>
    <div v-if="isLoading" class="w-full h-full bg-gray-800/80 fixed top-0 left-0 flex items-center justify-center z-30">
        <div class="loading-wave">
          <div class="loading-bar"></div>
          <div class="loading-bar"></div>
          <div class="loading-bar"></div>
          <div class="loading-bar"></div>
        </div>
    </div>
</template>
  
<script setup>
import HeaderComponent from "@/components/HeaderComponent.vue";
import { ref } from 'vue'
import axios from 'axios'

const sentiment = ref('')
const avis = ref('')
const errorMessage = ref('')
const isLoading = ref(false)
const lastAvis = ref('')
const responseGetting = ref(false)

const predictSentiment = async () => {
    try {
        isLoading.value = true
        lastAvis.value = avis.value
        const response = await axios.post("/predict", null, {
            params: { avis: avis.value },
        });
        sentiment.value = response.data;
        responseGetting.value = true
    } catch {
        errorMessage.value = "Erreur lors de la requête";
    } finally {
        isLoading.value = false
    }
}
</script>
  