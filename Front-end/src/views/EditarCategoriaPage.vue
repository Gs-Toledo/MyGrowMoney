<template>
  <base-user-template>
    <h2 class="mb-3 font-weight-bold text-lg">Editar Categoria</h2>
    <v-form
      @submit.prevent="atualizarDadosCategoria(idCategoria)"
      id="form-editar-categoria"
      v-if="!isLoading && !hasError"
    >
      <v-row>
        <v-col>
          <v-text-field
            label="Nome da Categoria"
            v-model="categoria.name"
            type="text"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-text-field
            label="Limite"
            prefix="R$"
            v-model="categoria.limit"
            type="number"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-btn class="mt-4" :disabled="isSendingRequest" type="submit" form="form-editar-categoria">
        Editar
      </v-btn>
    </v-form>
    <span class="errorDiv" v-else-if="hasError && !isLoading">Erro ao buscar dados...</span>
    <div v-else-if="isLoading && !hasError">
      <v-progress-circular indeterminate color="primary" />
    </div>
  </base-user-template>
</template>

<script>
import BaseUserTemplate from '@/components/baseUser/BaseUserTemplate.vue'
import axiosMyGrowMoney from '@/services/axios-configs'
import { initToast } from '@/utils/toastUtils'

export default {
  props: ['idCategoria'],
  components: {
    BaseUserTemplate
  },
  data() {
    return {
      categoria: {},
      toast: initToast(),
      isSendingRequest: false,
      isLoading: true,
      hasError: false
    }
  },
  methods: {
    async atualizarDadosCategoria(idCategoria) {
      let url = `/categories/${idCategoria}`

      try {
        this.isSendingRequest = true
        await axiosMyGrowMoney.put(url, { name: this.categoria.name, limit: this.categoria.limit })
        this.toast.success('Categoria atualizada com sucesso')
      } catch (error) {
        console.error(error)
        this.toast.error('Erro ao editar a categoria')
      } finally {
        this.isSendingRequest = false
      }
    },
    async getCategoriaById(idCategoria) {
      let url = `/categories/${idCategoria}`

      try {
        this.isLoading = true
        this.hasError = false
        const response = await axiosMyGrowMoney.get(url)
        console.log('categoria', response.data.category)
        this.categoria = response.data.category
      } catch (error) {
        console.error(error)
        this.hasError = true
      } finally {
        this.isLoading = false
      }
    }
  },
  async mounted() {
    await this.getCategoriaById(this.idCategoria)
  }
}
</script>
