<template>
  <base-user-template>
    <h2 class="mb-3 font-weight-bold text-lg">Categorias</h2>
    <div v-if="isLoading && !hasError" class="d-flex justify-center mt-5">
      <v-progress-circular indeterminate color="primary" />
    </div>

    <div class="errorDiv" v-else-if="hasError && !isLoading">
      Erro ao carregas os dados, tente novamente mais tarde...
    </div>

    <section v-else-if="!isLoading && !hasError">
      <v-table v-if="categorias.length > 0 && !isLoading">
        <thead>
          <tr>
            <th class="text-left">Categoria</th>
            <th class="text-left">Excluir</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(categoria, index) in categorias" :key="index">
            <td>{{ categoria.name }}</td>
            <td><v-btn color="red" @click="deleteCategoria(categoria)">Deletar</v-btn></td>
          </tr>
        </tbody>
      </v-table>

      <p v-else>Nenhuma Categoria encontrada.</p>
    </section>

    <router-link to="/categorias/cadastro">Cadastrar</router-link>
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
      categorias: [],
      isLoading: true,
      hasError: false
    }
  },
  methods: {
    async getCategorias() {
      let url = '/categories'

      try {
        this.isLoading = true
        this.hasError = false
        const response = await axiosMyGrowMoney(url)
        console.log('categorias novas', response.data)

        this.categorias = response.data.categories
      } catch (error) {
        console.error(error)
        this.hasError = true
      } finally {
        this.isLoading = false
      }
    },
    async deleteCategoria(categoria) {
      const deletarConfirmado = confirm('Tem certeza que deseja Deletar a Categoria?')
      let url = `/categories/${categoria.id}`
      if (deletarConfirmado) {
        await axiosMyGrowMoney.delete(url)
        alert('Categoria deletada com sucesso')
        this.getCategorias()
      }
    }
  },
  async mounted() {
    await this.getCategorias()
  }
}
</script>
