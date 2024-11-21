<template>
  <base-user-template>
    <dashboard-home 
      :despesasCategorias="despesasCategorias" v-if="!isLoading"/>
  </base-user-template>
</template>

<script>
import BaseUserTemplate from '@/components/baseUser/BaseUserTemplate.vue'
import DashboardHome from '@/components/graficos/DashboardHome.vue'
import axiosMyGrowMoney from '@/services/axios-configs'
export default {
  components: {
    BaseUserTemplate,
    DashboardHome
  },
  data() {
    return {
      despesasCategorias: [],
      isLoading: true
    }
  },
  methods: {
    async getDespesasPorCategoria() {
      let url = '/expenses-by-category'

      try {
        this.isLoading = true
        const response = await axiosMyGrowMoney.get(url)
        this.despesasCategorias = response.data.data
        console.log('response despesas categorias', this.despesasCategorias)
      } catch (error) {
        console.error('erro ao buscar despesas categorias', error)
      } finally {
        this.isLoading = false
      }
    }
  },
  async mounted() {
    this.getDespesasPorCategoria()
  }
}
</script>

<style scoped>
.v-card-title {
  font-weight: bold;
}
</style>
