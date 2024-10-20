<template>
  <base-user-template>
    <h2 class="mb-3 font-weight-bold text-lg">Cadastro de Receitas/Despesas</h2>
    <v-row>
      <v-col>
        <v-textarea label="Descrição" v-model="form.descricao"></v-textarea>

        <v-text-field label="Valor" prefix="R$" v-model="form.valor" type="number"></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-date-input label="Data" v-model="form.data"></v-date-input>

        <v-select label="Categoria" :items="categorias" v-model="form.categoria"></v-select>
      </v-col>
    </v-row>
    <v-row>
      <v-radio-group v-model="form.tipo">
        <v-radio label="Receita" value="receita"></v-radio>
        <v-radio label="Despesa" value="despesa"></v-radio>
      </v-radio-group>
    </v-row>

    <v-btn class="mt-4" type="button" @click="postCadastrarReceitaDespesa"> Enviar </v-btn>
  </base-user-template>
</template>

<script>
import BaseUserTemplate from '@/components/baseUser/BaseUserTemplate.vue'
import { VDateInput } from 'vuetify/labs/VDateInput'

export default {
  components: {
    BaseUserTemplate,
    VDateInput
  },
  data() {
    return {
      form: {
        descricao: '',
        valor: null,
        data: null,
        categoria: null,
        tipo: 'receita'
      },
      categorias: [
        { text: 'Alimentação', value: 'alimentacao' },
        { text: 'Transporte', value: 'transporte' },
        { text: 'Saúde', value: 'saude' },
        { text: 'Lazer', value: 'lazer' }
      ]
    }
  },
  methods: {
    postCadastrarReceitaDespesa() {
      console.log('Teste de Formulário enviado:', this.form)
    }
  }
}
</script>
