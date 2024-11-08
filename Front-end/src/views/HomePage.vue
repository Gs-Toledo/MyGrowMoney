<template>
  <base-user-template> ola home </base-user-template>
</template>

<script>
import BaseUserTemplate from '@/components/baseUser/BaseUserTemplate.vue'
import axiosMyGrowMoney from '@/services/axios-configs';
export default {
  components: {
    BaseUserTemplate
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
        this.transacoes = response.data
      } catch (error) {
        console.error('erro ao buscar transacoes',error)
      }
    }
  }
}
</script>

<style scoped>
.v-card-title {
  font-weight: bold;
}
</style>
