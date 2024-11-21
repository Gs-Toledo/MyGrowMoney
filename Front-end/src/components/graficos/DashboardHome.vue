<!-- Dashboard.vue -->
<template>
  <div class="p-6 space-y-6">
    <!-- Cards de Resumo -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div class="card">
        <div class="card-header flex items-center justify-between pb-2">
          <h3 class="text-sm font-medium">Receitas do Mês</h3>
          <i class="text-green-500">↑</i>
        </div>
        <div class="card-content">
          <div class="text-2xl font-bold text-green-600">
            R$ {{ formatValue(resumoMensal.receitas) }}
          </div>
          <p class="text-xs text-gray-500">+12% em relação ao mês anterior</p>
        </div>
      </div>

      <div class="card">
        <div class="card-header flex items-center justify-between pb-2">
          <h3 class="text-sm font-medium">Despesas do Mês</h3>
          <i class="text-red-500">↓</i>
        </div>
        <div class="card-content">
          <div class="text-2xl font-bold text-red-600">
            R$ {{ formatValue(resumoMensal.despesas) }}
          </div>
          <p class="text-xs text-gray-500">+5% em relação ao mês anterior</p>
        </div>
      </div>

      <div class="card">
        <div class="card-header flex items-center justify-between pb-2">
          <h3 class="text-sm font-medium">Saldo do Mês</h3>
          <i class="text-blue-500">↗</i>
        </div>
        <div class="card-content">
          <div class="text-2xl font-bold text-blue-600">
            R$ {{ formatValue(resumoMensal.saldo) }}
          </div>
          <p class="text-xs text-gray-500">
            Economia de {{ calcularPercentualEconomia }}% da receita
          </p>
        </div>
      </div>
    </div>

    <!-- Gráficos -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <!-- Gráfico de Pizza -->
      <div class="card">
        <div class="card-header">
          <h3 class="text-lg font-semibold">Despesas por Categoria</h3>
        </div>
        <div class="card-content h-[300px]">
          <PieChart :data="pieChartData" :options="pieChartOptions" />
        </div>
      </div>

      <!-- Gráfico de Linha -->
      <div class="card">
        <div class="card-header">
          <h3 class="text-lg font-semibold">Fluxo de Caixa</h3>
        </div>
        <div class="card-content h-[300px]">
          <LineChart :data="fluxoCaixaData" :options="lineChartOptions" />
        </div>
      </div>
    </div>

    <!-- Resumo Mensal -->
    <div class="card">
      <div class="card-header">
        <h3 class="text-lg font-semibold">Resumo Financeiro - {{ mesAtual }}</h3>
      </div>
      <div class="card-content">
        <!-- Grid de resumo -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
          <div class="p-4 bg-gray-50 rounded-lg">
            <p class="text-sm text-gray-500">Saldo Inicial</p>
            <p class="text-lg font-bold text-gray-900">
              R$ {{ formatValue(resumoMensal.saldoInicial) }}
            </p>
          </div>
          <div class="p-4 bg-gray-50 rounded-lg">
            <p class="text-sm text-gray-500">Total Receitas</p>
            <p class="text-lg font-bold text-green-600">
              + R$ {{ formatValue(resumoMensal.receitas) }}
            </p>
          </div>
          <div class="p-4 bg-gray-50 rounded-lg">
            <p class="text-sm text-gray-500">Total Despesas</p>
            <p class="text-lg font-bold text-red-600">
              - R$ {{ formatValue(resumoMensal.despesas) }}
            </p>
          </div>
          <div class="p-4 bg-gray-50 rounded-lg">
            <p class="text-sm text-gray-500">Saldo Final</p>
            <p class="text-lg font-bold text-blue-600">
              R$ {{ formatValue(resumoMensal.saldoFinal) }}
            </p>
          </div>
        </div>

        <!-- Gráfico de Barras -->
        <div>
          <h4 class="text-sm font-medium mb-4">Comparativo Mensal</h4>
          <div class="h-[300px]">
            <BarChart :data="comparativoMensalData" :options="barChartOptions" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  ArcElement,
  Tooltip,
  Legend
} from 'chart.js'
import { Pie as PieChart, Line as LineChart, Bar as BarChart } from 'vue-chartjs'
import { formatToLocaleBr } from '@/utils/formatUtils';

// Registrar os componentes necessários do Chart.js
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  ArcElement,
  Tooltip,
  Legend
)

const props = defineProps({
  despesasCategorias: {
    type: Array,
    required: true
  }
})

console.log('props',props.despesasCategorias)

// Estado
const resumoMensal = ref({
  saldoInicial: 3800,
  receitas: 5800,
  despesas: 4300,
  saldo: 1500,
  saldoFinal: 5300
})

const fluxoCaixa = ref([
  { mes: 'Jul', receitas: 5000, despesas: 4000, saldo: 1000 },
  { mes: 'Ago', receitas: 5500, despesas: 4200, saldo: 1300 },
  { mes: 'Set', receitas: 4800, despesas: 4500, saldo: 300 },
  { mes: 'Out', receitas: 6000, despesas: 4100, saldo: 1900 },
  { mes: 'Nov', receitas: 5800, despesas: 4300, saldo: 1500 }
])

// Computed Properties
const mesAtual = computed(() => {
  return 'Novembro 2024'
})

const calcularPercentualEconomia = computed(() => {
  return ((resumoMensal.value.saldo / resumoMensal.value.receitas) * 100).toFixed(1)
})

// Configurações comuns dos gráficos
const commonOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      position: 'top',
      align: 'center'
    }
  }
}

// Configurações específicas de cada gráfico
const pieChartOptions = {
  ...commonOptions,
  plugins: {
    ...commonOptions.plugins,
    legend: {
      position: 'bottom'
    }
  }
}

const lineChartOptions = {
  ...commonOptions,
  scales: {
    y: {
      beginAtZero: true,
      grid: {
        drawBorder: false
      }
    },
    x: {
      grid: {
        display: false
      }
    }
  }
}

const barChartOptions = {
  ...commonOptions,
  scales: {
    y: {
      beginAtZero: true,
      grid: {
        drawBorder: false
      }
    },
    x: {
      grid: {
        display: false
      }
    }
  },
  barPercentage: 0.7,
  categoryPercentage: 0.8
}

// Dados formatados para os gráficos
const pieChartData = computed(() => ({
  labels: props.despesasCategorias.map((item) => item.category),
  datasets: [
    {
      data: props.despesasCategorias.map((item) => item.total),
      backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF']
    }
  ]
}))

const fluxoCaixaData = computed(() => ({
  labels: fluxoCaixa.value.map((item) => item.mes),
  datasets: [
    {
      label: 'Receitas',
      data: fluxoCaixa.value.map((item) => item.receitas),
      borderColor: '#4CAF50',
      tension: 0.1,
      fill: false
    },
    {
      label: 'Despesas',
      data: fluxoCaixa.value.map((item) => item.despesas),
      borderColor: '#f44336',
      tension: 0.1,
      fill: false
    },
    {
      label: 'Saldo',
      data: fluxoCaixa.value.map((item) => item.saldo),
      borderColor: '#2196F3',
      tension: 0.1,
      fill: false
    }
  ]
}))

const comparativoMensalData = computed(() => ({
  labels: fluxoCaixa.value.map((item) => item.mes),
  datasets: [
    {
      label: 'Receitas',
      data: fluxoCaixa.value.map((item) => item.receitas),
      backgroundColor: '#4CAF50'
    },
    {
      label: 'Despesas',
      data: fluxoCaixa.value.map((item) => item.despesas),
      backgroundColor: '#f44336'
    }
  ]
}))

// Métodos
const formatValue = (value) => {
  return formatToLocaleBr(value)
}
</script>

<style scoped>
.card {
  @apply bg-white rounded-lg shadow-sm p-6;
}

.card-header {
  @apply mb-4;
}

.card-content {
  @apply relative;
}

@media (max-width: 768px) {
  .h-[300px] {
    height: 250px;
  }
}
</style>
