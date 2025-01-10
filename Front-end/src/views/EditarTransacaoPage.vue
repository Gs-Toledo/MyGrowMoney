<template>
  <base-user-template>
    <div class="title-section">
      <h2 class="mb-3 font-weight-bold text-lg">Editar Transação</h2>
    </div>
    <section>
      <v-form @submit.prevent="atualizarTransacao">
        <v-row>
          <v-col>
            <v-textarea label="Descrição" v-model="transacao.description" required></v-textarea>

            <v-text-field
              label="Valor"
              prefix="R$"
              v-model="transacao.value"
              type="number"
              required
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-date-input label="Data" v-model="transacao.date"></v-date-input>

            <v-select
              label="Categoria"
              :items="categorias"
              item-title="name"
              item-value="id"
              v-model="transacao.categoryId"
              required
            ></v-select>
            <!-- <span class="text-red" v-if="selectedCategoriaLimite"
              >Limite da categoria: R${{ selectedCategoriaLimite }}</span
            > -->
          </v-col>
        </v-row>
        <v-row>
          <v-radio-group v-model="transacao.type">
            <v-radio label="Receita" value="receita"></v-radio>
            <v-radio label="Despesa" value="despesa"></v-radio>
          </v-radio-group>
        </v-row>

        <v-row>
          <v-col>
            <v-checkbox
              label="Transação Recorrente?"
              v-model="transacao.is_recurring"
              class="mt-4"
            ></v-checkbox>
          </v-col>
        </v-row>

        <v-btn class="mt-4" :disabled="isSendingRequest" type="submit"> Editar </v-btn>
      </v-form>
    </section>
  </base-user-template>
</template>

<script>
import BaseUserTemplate from '../components/baseUser/BaseUserTemplate.vue'
import axiosMyGrowMoney from '@/services/axios-configs'
import { initToast } from '@/utils/toastUtils'

export default {
  props: ['idTransacao'],
  components: {
    BaseUserTemplate
  },
  data() {
    return {
      transacao: {},
      categorias: [],
      isLoading: true,
      hasError: false,
      isSendingRequest: false,
      toast: initToast()
    }
  },
  methods: {
    async getTransacaoById(idTransacao) {
      let url = `/transactions/${idTransacao}"`

      try {
        const response = await axiosMyGrowMoney.get(url)
        console.log(response.data)
      } catch (error) {
        throw new Error(error)
      }
    },
    async getCategoriasCadastradasCliente() {
      let url = '/categories'

      try {
        const response = await axiosMyGrowMoney.get(url)
        console.log('categorias novas', response.data)

        this.categorias = response.data.categories
      } catch (error) {
        throw new Error(error)
      }
    },
    async atualizarTransacao(idTransacao) {
      let url = `/transactions/${idTransacao}`

      try {
        this.isSendingRequest = true
        await axiosMyGrowMoney.put(url, this.transacao)
        this.toast.success('Transação editada com sucesso')
      } catch (error) {
        console.error(error)
        this.toast.error('Erro ao editar transação')
      } finally {
        this.isSendingRequest = false
      }
    }
  },
  async mounted() {
    try {
      this.isLoading = true
      this.hasError = false
      Promise.all([this.getCategoriasCadastradasCliente(), this.getTransacaoById(this.idTransacao)])
    } catch (error) {
      console.error(error)
      this.hasError = true
    } finally {
      this.isLoading = false
    }
  }
}
</script>
