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
          <div class="text-2xl font-bold text-green-600" v-if="temDadosMesAtual">
            R$ {{ formatValue(resumoMesAtual.receitas) }}
          </div>
          <div class="text-gray-500" v-else>Sem dados no momento...</div>
        </div>
      </div>

      <div class="card">
        <div class="card-header flex items-center justify-between pb-2">
          <h3 class="text-sm font-medium">Despesas do Mês</h3>
          <i class="text-red-500">↓</i>
        </div>
        <div class="card-content">
          <div class="text-2xl font-bold text-red-600" v-if="temDadosMesAtual">
            R$ {{ formatValue(resumoMesAtual.despesas) }}
          </div>
          <div class="text-gray-500" v-else>Sem dados no momento...</div>
        </div>
      </div>

      <div class="card">
        <div class="card-header flex items-center justify-between pb-2">
          <h3 class="text-sm font-medium">Saldo do Mês</h3>
          <i class="text-blue-500">↗</i>
        </div>
        <div class="card-content">
          <div class="text-2xl font-bold text-blue-600" v-if="temDadosMesAtual">
            R$ {{ formatValue(resumoMesAtual.saldo) }}
          </div>
          <p class="text-xs text-gray-500" v-if="temDadosMesAtual">
            Economia de {{ calcularPercentualEconomia }}% da receita
          </p>
          <div class="text-gray-500" v-if="!temDadosMesAtual">Sem dados no momento...</div>
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
        <div class="card-content h-[300px]" v-if="despesasCategorias.length > 0">
          <PieChart :data="pieChartData" :options="pieChartOptions" />
        </div>
        <div class="card-content" v-else>
          <span class="text-slate-500">Cadastre Transações e Categorias primeiro...</span>
        </div>
      </div>

      <!-- Gráfico de Linha -->
      <div class="card">
        <div class="card-header">
          <h3 class="text-lg font-semibold">Fluxo de Caixa</h3>
        </div>
        <div class="card-content h-[300px]" v-if="monthlySummary.length > 0">
          <LineChart :data="fluxoCaixaData" :options="lineChartOptions" />
        </div>
        <div class="card-content" v-else>
          <span class="text-slate-500">Cadastre Transações e Categorias primeiro...</span>
        </div>
      </div>
    </div>

    <!-- Resumo Mensal -->
    <div class="card">
      <div class="card-header">
        <div class="flex justify-space-between">
          <h3 class="text-lg font-semibold">Resumo Financeiro - {{ mesAtual }} {{ anoAtual }}</h3>
          <v-btn @click="handleExportCsv">Exportar CSV</v-btn>
        </div>
      </div>
      <div class="card-content">
        <!-- Grid de resumo -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
          <div class="p-4 bg-gray-50 rounded-lg">
            <p class="text-sm text-gray-500">Saldo Inicial</p>
            <p class="text-lg font-bold text-gray-900" v-if="temDadosMesAtual">
              R$ {{ formatValue(resumoMesAtual.saldo_inicial) }}
            </p>
            <div class="text-gray-500" v-if="!temDadosMesAtual">Sem dados no momento...</div>
          </div>
          <div class="p-4 bg-gray-50 rounded-lg">
            <p class="text-sm text-gray-500">Total Receitas</p>
            <p class="text-lg font-bold text-green-600" v-if="temDadosMesAtual">
              + R$ {{ formatValue(resumoMesAtual.receitas) }}
            </p>
            <div class="text-gray-500" v-if="!temDadosMesAtual">Sem dados no momento...</div>
          </div>
          <div class="p-4 bg-gray-50 rounded-lg">
            <p class="text-sm text-gray-500">Total Despesas</p>
            <p class="text-lg font-bold text-red-600" v-if="temDadosMesAtual">
              - R$ {{ formatValue(resumoMesAtual.despesas) }}
            </p>
            <div class="text-gray-500" v-if="!temDadosMesAtual">Sem dados no momento...</div>
          </div>
          <div class="p-4 bg-gray-50 rounded-lg">
            <p class="text-sm text-gray-500">Saldo Final</p>
            <p class="text-lg font-bold text-blue-600" v-if="temDadosMesAtual">
              R$ {{ formatValue(resumoMesAtual.saldo_final) }}
            </p>
            <div class="text-gray-500" v-if="!temDadosMesAtual">Sem dados no momento...</div>
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
import { computed } from 'vue'
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
import { formatToLocaleBr } from '@/utils/formatUtils'
import { getCurrentMonthName, getCurrentYear } from '@/utils/dateUtils'
import CsvHandler from '@/utils/CsvHandler'

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
  },
  monthlySummary: {
    type: Array,
    required: true
  }
})

const handleExportCsv = () => {
  try {
    CsvHandler.exportCsv(props.monthlySummary)
  } catch (error) {
    console.error('erro em export csv', error)
  }
}

const mesAtual = computed(() => {
  return getCurrentMonthName()
})

const anoAtual = computed(() => {
  return getCurrentYear()
})

const temDadosMesAtual = computed(() => {
  return props.monthlySummary.some(
    (item) => item.mes == mesAtual.value && item.ano == anoAtual.value
  )
})

const resumoMesAtual = computed(() => {
  const resumo = props.monthlySummary.filter((item) => {
    return item.mes == mesAtual.value && item.ano == anoAtual.value
  })
  console.log(resumo)
  return resumo[0]
})

const calcularPercentualEconomia = computed(() => {
  return ((resumoMesAtual.value.saldo / resumoMesAtual.value.receitas) * 100).toFixed(1)
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
  labels: props.monthlySummary.map((item) => item.mes),
  datasets: [
    {
      label: 'Receitas',
      data: props.monthlySummary.map((item) => item.receitas),
      borderColor: '#4CAF50',
      tension: 0.1,
      fill: false
    },
    {
      label: 'Despesas',
      data: props.monthlySummary.map((item) => item.despesas),
      borderColor: '#f44336',
      tension: 0.1,
      fill: false
    },
    {
      label: 'Saldo',
      data: props.monthlySummary.map((item) => item.saldo_final),
      borderColor: '#2196F3',
      tension: 0.1,
      fill: false
    }
  ]
}))

const comparativoMensalData = computed(() => ({
  labels: props.monthlySummary.map((item) => item.mes),
  datasets: [
    {
      label: 'Receitas',
      data: props.monthlySummary.map((item) => item.receitas),
      backgroundColor: '#4CAF50'
    },
    {
      label: 'Despesas',
      data: props.monthlySummary.map((item) => item.despesas),
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
