<template>
  <base-user-template>
    <dashboard-home />
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
      transacoes: []
    }
  },
  methods: {
    async getAllTransactions() {
      let url = '/transactions'

      try {
        const response = await axiosMyGrowMoney.get(url)
        console.log('response transactions', response.data)
        this.transacoes = response.data.transactions
      } catch (error) {
        console.error('erro ao buscar transacoes', error)
      }
    }
  },
  async mounted() {
    this.getAllTransactions()
  }
}
</script>

<style scoped>
.v-card-title {
  font-weight: bold;
}
</style>
