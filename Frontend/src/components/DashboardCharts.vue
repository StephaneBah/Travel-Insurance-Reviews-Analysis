<template>
    <div class="fixed top-[100px] left-[50%] z-[100] translate-x-[-50%] w-[80%] max-w-[400px] flex flex-col">
        <div v-if="errorMessage" class="text-sm w-full rounded-[5px] shadow-4xl text-white bg-red-700 my-[10px] font-bold text-center p-[20px]">
            {{ errorMessage }}
        </div>
    </div>
    <div class="p-[20px] flex flex-wrap items-start justify-between w-full relative">
      <!-- Graphique 1: Évolution des notes moyennes -->
      <div class="bg-white p-[15px] rounded-xl shadow lg:w-[calc(50%-15px)] w-full my-[15px]">
        <h2 class="text-xl font-semibold mb-2">Évolution des notes moyennes</h2>
        <p v-if="!lineChartData.labels.length">Aucune donnée</p>
        <Line v-else :data="lineChartData" :options="chartOptions" />
      </div>
  
      <!-- Graphique 2: Répartition des sentiments -->
      <div class="bg-white p-[15px] rounded-xl shadow lg:w-[calc(50%-15px)] w-full my-[15px]">
        <h2 class="text-xl font-semibold mb-2">Répartition des sentiments</h2>
        <p v-if="!barChartData.labels.length">Aucune donnée</p>
        <Bar v-else :data="barChartData" :options="chartOptions" />
      </div>
  
      <!-- Graphique 3: Sentiments en 2024 -->
      <div class="bg-white p-[15px] rounded-xl shadow lg:w-[calc(50%-15px)] w-full my-[15px]">
        <h2 class="text-xl font-semibold mb-2">Sentiments en 2024</h2>
        <p v-if="!barChart2024Data.labels.length">Aucune donnée</p>
        <Bar v-else :data="barChart2024Data" :options="chartOptions" />
      </div>

      <!-- Graphique 5: Répartition des notes (Pie Chart) -->
      <div class="bg-white p-[15px] rounded-xl shadow lg:w-[calc(50%-15px)] w-full max-h-[350px] my-[15px]">
        <h2 class="text-xl font-semibold mb-[20px]">Répartition des notes (%)</h2>
        <p v-if="!pieChartData.labels.length">Aucune donnée</p>
        <Pie v-else :data="pieChartData" :options="pieChartOptions" class="max-h-[250px]" />
      </div>
  
      <!-- Graphique 4: Top 50 des mots les plus fréquents -->
      <div class="bg-white p-[15px] rounded-xl shadow w-[calc(100%)] my-[15px]">
        <h2 class="text-xl font-semibold mb-2">Top 50 des mots les plus fréquents</h2>
        <p v-if="!wordBarChartData.labels.length">Aucune donnée</p>
        <Bar v-else :data="wordBarChartData" :options="horizontalChartOptions" />
      </div>
  
    </div>
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
  import { ref, onMounted } from "vue";
  import axios from "axios";
  import { Chart, registerables } from "chart.js";
  import { Line, Bar, Pie } from "vue-chartjs";
  
  Chart.register(...registerables);
  
  const reviewsData = ref([]);
  const errorMessage = ref('')
  const isLoading = ref(false)
  
  // Options des graphiques
  const chartOptions = ref({
    responsive: true,
    maintainAspectRatio: true,
  });
  
  const horizontalChartOptions = ref({
    responsive: true,
    maintainAspectRatio: true,
    indexAxis: "y",
  });
  
  // Données des graphiques
  const lineChartData = ref({ labels: [], datasets: [] });
  const barChartData = ref({ labels: [], datasets: [] });
  const barChart2024Data = ref({ labels: [], datasets: [] });
  const wordBarChartData = ref({ labels: [], datasets: [] });
  const pieChartData = ref({ labels: [], datasets: [] });

  const pieChartOptions = ref({
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      position: "right", // Place la légende à droite
      labels: {
        font: {
          size: 14,
        },
      },
    },
  },
});

  
  const fetchTrends = async () => {
    try {
        isLoading.value = true
      const response = await axios.get("/trend");
      reviewsData.value = response.data;
      processData();
    } catch (error) {
      errorMessage.value = "Erreur lors de la récupération des données";
    } finally {
        isLoading.value = false
    }
  };
  
  const processData = () => {
    if (!reviewsData.value || reviewsData.value.length === 0) return;
  
    const ratingsByMonth = {};
    const sentimentsByMonth = {};
    const sentiments2024 = {};
    const wordFrequency = {};
    const ratingCounts = {};
  
    let totalReviews = reviewsData.value.length;
  
    reviewsData.value.forEach((review) => {
      const date = new Date(review.review_date);
      const yearMonth = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, "0")}`;
      const year = date.getFullYear();
      const sentiment = review.Sentiment;
      const rating = review.rate;
  
      // Graphique 1: Évolution des notes moyennes
      if (!ratingsByMonth[year]) {
        ratingsByMonth[year] = { total: 0, count: 0 };
      }
      ratingsByMonth[year].total += rating;
      ratingsByMonth[year].count++;
  
      // Graphique 2: Répartition des sentiments
      if (!sentimentsByMonth[yearMonth]) {
        sentimentsByMonth[yearMonth] = { POSITIVE: 0, NEGATIVE: 0 };
      }
      sentimentsByMonth[yearMonth][sentiment]++;
  
      // Graphique 3: Sentiments en 2024
      if (year === 2024) {
        if (!sentiments2024[yearMonth]) {
          sentiments2024[yearMonth] = { POSITIVE: 0, NEGATIVE: 0 };
        }
        sentiments2024[yearMonth][sentiment]++;
      }
  
      // Graphique 4: Top 50 des mots les plus fréquents
      if (review.tokenized_reviews) {
        JSON.parse(review.tokenized_reviews.replace(/'/g, '"')).forEach((word) => {
          word = word.toLowerCase();
          wordFrequency[word] = (wordFrequency[word] || 0) + 1;
        });
      }
  
      // Graphique 5: Répartition des notes (Pie Chart)
      ratingCounts[rating] = (ratingCounts[rating] || 0) + 1;
    });
  
    // Transformer les données pour Chart.js
    lineChartData.value = {
      labels: Object.keys(ratingsByMonth),
      datasets: [
        {
          label: "Moyenne des notes",
          data: Object.values(ratingsByMonth).map((d) => (d.total / d.count).toFixed(2)),
          borderColor: "blue",
          backgroundColor: "blue",
        },
      ],
    };
  
    barChartData.value = {
      labels: Object.keys(sentimentsByMonth),
      datasets: [
        {
          label: "Positifs",
          data: Object.values(sentimentsByMonth).map((d) => d.POSITIVE),
          backgroundColor: "green",
        },
        {
          label: "Négatifs",
          data: Object.values(sentimentsByMonth).map((d) => d.NEGATIVE),
          backgroundColor: "red",
        },
      ],
    };
  
    barChart2024Data.value = {
      labels: Object.keys(sentiments2024),
      datasets: [
        {
          label: "Positifs",
          data: Object.values(sentiments2024).map((d) => d.POSITIVE),
          backgroundColor: "green",
        },
        {
          label: "Négatifs",
          data: Object.values(sentiments2024).map((d) => d.NEGATIVE),
          backgroundColor: "red",
        },
      ],
    };
  
    wordBarChartData.value = {
      labels: Object.keys(wordFrequency)
        .sort((a, b) => wordFrequency[b] - wordFrequency[a])
        .slice(0, 50),
      datasets: [
        {
          label: "Fréquence",
          data: Object.values(wordFrequency)
            .sort((a, b) => b - a)
            .slice(0, 50),
          backgroundColor: "blue",
        },
      ],
    };
  
    // Graphique en disque (Pie Chart)
    pieChartData.value = {
      labels: Object.keys(ratingCounts),
      datasets: [
        {
          data: Object.values(ratingCounts).map((count) => ((count / totalReviews) * 100).toFixed(2)),
          backgroundColor: ["#4CAF50", "#FFC107", "#F44336", "#2196F3", "#9C27B0"],
        },
      ],
    };
  };
  
  onMounted(() => {
    fetchTrends();
  });
  </script>
  