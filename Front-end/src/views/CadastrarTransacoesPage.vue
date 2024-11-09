<template>
  <base-user-template>
    <h2 class="mb-3 font-weight-bold text-lg">Cadastro de Transação</h2>
    <v-row>
      <v-col>
        <v-textarea label="Descrição" v-model="form.description"></v-textarea>

        <v-text-field label="Valor" prefix="R$" v-model="form.value" type="number"></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-date-input label="Data" v-model="form.date"></v-date-input>

        <v-select
          label="Categoria"
          :items="categorias"
          item-title="name"
          item-value="id"
          v-model="form.categoryId"
        ></v-select>
        <span class="text-red" v-if="selectedCategoriaLimite">Limite da categoria: R${{ selectedCategoriaLimite }}</span>
      </v-col>
    </v-row>
    <v-row>
      <v-radio-group v-model="form.type">
        <v-radio label="Receita" value="receita"></v-radio>
        <v-radio label="Despesa" value="despesa"></v-radio>
      </v-radio-group>
    </v-row>

    <v-row>
      <v-col>
        <v-checkbox
          label="Transação Recorrente?"
          v-model="form.is_recurring"
          class="mt-4"
        ></v-checkbox>
      </v-col>
    </v-row>

    <v-btn
      class="mt-4"
      :disabled="isSendingRequest"
      type="button"
      @click="postCadastrarReceitaDespesa"
    >
      Enviar
    </v-btn>

    <p class="text-red" v-if="avisoLimiteCategoria">{{ avisoLimiteCategoria }}</p>
  </base-user-template>
</template>

<script>
import BaseUserTemplate from '@/components/baseUser/BaseUserTemplate.vue'
import axiosMyGrowMoney from '@/services/axios-configs'
import { VDateInput } from 'vuetify/labs/VDateInput'

export default {
  components: {
    BaseUserTemplate,
    VDateInput
  },
  data() {
    return {
      form: {
        description: '',
        value: null,
        date: null,
        categoryId: null,
        type: 'receita',
        is_recurring: false
      },
      categorias: [],
      selectedCategoriaLimite: null,
      avisoLimiteCategoria: null,
      isSendingRequest: false
    }
  },
  watch: {
    'form.categoryId': function () {
      this.setSelectedCategoryLimit()
    }
  },
  methods: {
    async postCadastrarReceitaDespesa() {
      console.log('Teste de Formulário enviado:', this.form)

      let url = '/transactions'
      this.isSendingRequest = true
      try {
        const response = await axiosMyGrowMoney.post(url, {
          ...this.form,
          date: this.form.date.toISOString()
        })

        alert('Cadastro realizado com sucesso!')
        console.log(response.data)

        this.avisoLimiteCategoria = this.handleLimiteCadastradoCategoria(response.data)
      } catch (error) {
        console.error('Erro ao cadastrar', error)

        alert('Erro no cadastro: ' + error?.response?.data.message)
      } finally {
        this.isSendingRequest = false
      }
    },
    async getCategoriasCadastradasCliente() {
      let url = '/categories'

      try {
        const response = await axiosMyGrowMoney(url)
        console.log('categorias novas', response.data)

        this.categorias = response.data.categories
      } catch (error) {
        console.error(error)
      }
    },
    setSelectedCategoryLimit() {
      // Usando o valor do v-model diretamente para encontrar o limite
      const selectedCategory = this.categorias.find(
        (category) => category.id === this.form.categoryId
      )
      if (selectedCategory) {
        this.selectedCategoriaLimite = selectedCategory.limit
      }
      console.log(this.selectedCategoriaLimite)
    },
    handleLimiteCadastradoCategoria(data) {
      switch (data.budget_alert) {
        case 'over':
          return 'Limite total da categoria Ultrapassado!!'
        case 'almost':
          return 'Limite total da categoria quase atingido!!'
        case 'far':
          return null
      }
    }
  },
  async mounted() {
    await this.getCategoriasCadastradasCliente()
  }
}
</script>
