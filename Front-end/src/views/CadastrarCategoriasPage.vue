<template>
  <base-user-template>
    <h2 class="mb-3 font-weight-bold text-lg">Cadastro de Categorias</h2>
    <v-row>
      <v-col>
        <v-text-field label="Nome da Categoria" v-model="newCategoria" type="text"></v-text-field>
      </v-col>
    </v-row>
    <v-btn class="mt-4" type="button" @click="postCadastroNewCategoria"> Cadastrar </v-btn>
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
      newCategoria: ''
    }
  },
  methods: {
    async postCadastroNewCategoria() {
      console.log('Teste de Formulário enviado:', this.form)
      let url = '/categories'
      if (this.newCategoria.trim() == '') {
        alert('Preencha corretamente os campos')
        return
      }
      try {
        await axiosMyGrowMoney.post(url, { name: this.newCategoria })
        alert('categoria cadastrada com sucesso')
      } catch (error) {
        console.error('Erro ao cadastrar categoria', error)
        alert('Erro ao cadastrar a nova categoria, tente novamente!')
      }
    }
  },
  async mounted() {

  }
}
</script>
