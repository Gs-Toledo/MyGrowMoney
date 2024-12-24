<template>
  <base-user-template>
    <h2 class="mb-3 font-weight-bold text-lg">Cadastro de Categorias</h2>
    <v-form @submit.prevent="postCadastroNewCategoria" id="form-cadastro-categoria">
      <v-row>
        <v-col>
          <v-text-field
            label="Nome da Categoria"
            v-model="newCategoria.name"
            type="text"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-text-field
            label="Limite"
            prefix="R$"
            v-model="newCategoria.limit"
            type="number"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-btn class="mt-4" type="submit" form="form-cadastro-categoria"> Cadastrar </v-btn>
    </v-form>
  </base-user-template>
</template>

<script>
import BaseUserTemplate from '@/components/baseUser/BaseUserTemplate.vue'
import axiosMyGrowMoney from '@/services/axios-configs'
import { initToast } from '@/utils/toastUtils'

export default {
  components: {
    BaseUserTemplate
  },
  data() {
    return {
      newCategoria: {
        name: '',
        limit: 0
      },
      toast: initToast()
    }
  },
  methods: {
    async postCadastroNewCategoria() {
      let url = '/categories'
      if (this.newCategoria.name.trim() == '') {
        this.toast.warning('Preencha corretamente os campos')
        return
      }
      try {
        await axiosMyGrowMoney.post(url, this.newCategoria)
        this.toast.success('Categoria cadastrada com sucesso')
      } catch (error) {
        console.error('Erro ao cadastrar categoria', error)
        this.toast.error('Erro ao cadastrar a nova categoria, tente novamente!')
      }
    }
  },
  async mounted() {}
}
</script>
