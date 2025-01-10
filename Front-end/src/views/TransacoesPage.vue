<template>
  <base-user-template>
    <h2 class="mb-3 font-weight-bold text-lg">Receitas/Despesas</h2>

    <div v-if="isLoading && !hasError" class="d-flex justify-center mt-5">
      <v-progress-circular indeterminate color="primary" />
    </div>

    <div class="errorDiv" v-else-if="hasError && !isLoading">
      Erro ao carregar as transações, tente novamente mais tarde...
    </div>

    <section v-else-if="!isLoading && !hasError">
      <v-table v-if="transacoes.length > 0">
        <thead>
          <tr>
            <th class="text-left">Nome</th>
            <th class="text-left">Valor</th>
            <th>Categoria</th>
            <th class="text-left">Data</th>
            <th class="text-left">Recorrente?</th>
            <th class="text-left"></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(transacao, index) in transacoes" :key="index">
            <td><router-link :to="`/transacoes/${transacao.id}`">{{ transacao.description }}</router-link></td>
            <td
              :class="{
                'text-red-600': transacao.type == 'despesa',
                'text-green-600': transacao.type == 'receita'
              }"
            >
              R${{ formatarValorMonetario(transacao.value) }}
            </td>
            <th>{{ transacao.category.name }}</th>
            <td>{{ formatDate(transacao.date) }}</td>
            <td v-if="transacao.is_recurring">Sim</td>
            <td v-else>Não</td>
            <td>
              <v-btn color="red" @click="deleteTransacao(transacao)">Deletar</v-btn>
            </td>
          </tr>
        </tbody>
      </v-table>

      <p v-else>Nenhuma transação encontrada.</p>
    </section>

    <v-btn class="mt-5"><router-link to="/transacoes/cadastro">Cadastrar</router-link></v-btn>
  </base-user-template>
</template>

<script>
import BaseUserTemplate from '@/components/baseUser/BaseUserTemplate.vue'
import axiosMyGrowMoney from '@/services/axios-configs'
import { formatDateFromIso, formatNumberToMoneyDouble } from '@/utils/formatUtils'
import { initToast } from '@/utils/toastUtils'

export default {
  components: {
    BaseUserTemplate
  },
  data() {
    return {
      transacoes: [],
      toast: initToast(),
      isLoading: true,
      hasError: false
    }
  },
  methods: {
    async getTransacoes() {
      const url = '/transactions'

      try {
        this.isLoading = true
        this.hasError = false
        const response = await axiosMyGrowMoney(url)
        console.log('transactions', response.data)

        this.transacoes = response.data.transactions
      } catch (error) {
        console.error(error)
        this.hasError = true
      } finally {
        this.isLoading = false
      }
    },
    async deleteTransacao(transacao) {
      const deletarConfirmado = confirm('Tem certeza que deseja Deletar a Transação?')
      const url = `/transactions/${transacao.id}`

      if (deletarConfirmado) {
        try {
          await axiosMyGrowMoney.delete(url)
          this.toast.success('Transação deletada com sucesso')
          await this.getTransacoes()
        } catch (error) {
          console.error('Erro ao deletar transação:', error)
          this.toast.error('Erro ao deletar a transação. Tente novamente.')
        }
      }
    },
    formatDate(isoDate) {
      return formatDateFromIso(isoDate)
    },
    formatarValorMonetario(value) {
      return formatNumberToMoneyDouble(value)
    }
  },
  async mounted() {
    await this.getTransacoes()
  }
}
</script>
