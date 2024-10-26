<template>
  <base-user-template>
    <h2 class="mb-3 font-weight-bold text-lg">Receitas/Despesas</h2>
    <v-table v-if="transacoes.length > 0">
      <thead>
        <tr>
          <th class="text-left">Nome</th>
          <th class="text-left">Valor</th>
          <th class="text-left">Data</th>
          <th class="text-left">Excluir</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(transacao, index) in transacoes" :key="index">
          <td>{{ transacao.description }}</td>
          <td>R${{ transacao.value }}</td>
          <td>{{ transacao.date }}</td>
          <td>Butao</td>
        </tr>
      </tbody>
    </v-table>

    <router-link to="/transacoes/cadastro">Cadastrar</router-link>
  </base-user-template>
</template>

<script>
import BaseUserTemplate from '@/components/baseUser/BaseUserTemplate.vue'
import axiosMyGrowMoney from '@/services/axios-configs'

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
    async getTransacoes() {
      let url = '/transactions'

      try {
        const response = await axiosMyGrowMoney(url)
        console.log('transactions', response.data)

        this.transacoes = response.data.transactions
      } catch (error) {
        console.error(error)
      }
    }
  },
  async mounted() {
    await this.getTransacoes()
  }
}
</script>
