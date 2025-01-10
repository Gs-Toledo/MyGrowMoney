<template>
  <base-user-template>
  <p class="text-h4">Bem-vindo, {{ getUser.name }}</p>
    <dashboard-home
      :despesasCategorias="despesasCategorias"
      :monthlySummary="monthlySummary"
      v-if="!isLoading"
    />
  </base-user-template>
</template>

<script>
import BaseUserTemplate from '@/components/baseUser/BaseUserTemplate.vue'
import DashboardHome from '@/components/graficos/DashboardHome.vue'
import axiosMyGrowMoney from '@/services/axios-configs'
import { mapGetters } from 'vuex';
export default {
  components: {
    BaseUserTemplate,
    DashboardHome
  },
  data() {
    return {
      despesasCategorias: [],
      monthlySummary: [],
      isLoading: true
    }
  },
  computed: {
    ...mapGetters(['getUser'])
  },
  methods: {
    async getDespesasPorCategoria() {
      let url = '/expenses-by-category'

      try {
        const response = await axiosMyGrowMoney.get(url)
        this.despesasCategorias = response.data.data
        console.log('response despesas categorias', this.despesasCategorias)
      } catch (error) {
        console.error('erro ao buscar despesas categorias')
        throw new Error(error)
      }
    },
    async getMonthlySummary() {
      let url = '/monthly-summary'

      try {
        const response = await axiosMyGrowMoney.get(url)
        this.monthlySummary = response.data.data
        console.log('response Fluxo caixa', response.data)
      } catch (error) {
        console.error('erro ao buscar fluxo caixa')
        throw new Error(error)
      }
    }
  },
  async mounted() {
    try {
      this.isLoading = true
      await Promise.all([this.getDespesasPorCategoria(), this.getMonthlySummary()])
    } catch (error) {
      console.error(error)
    } finally {
      this.isLoading = false
    }
  }
}
</script>

<style scoped>
.v-card-title {
  font-weight: bold;
}
</style>
