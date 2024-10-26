<template>
  <base-user-template>
    <h2 class="mb-3 font-weight-bold text-lg">Categorias</h2>
    <v-table v-if="categorias.length > 0">
      <thead>
        <tr>
          <th class="text-left">Categoria</th>
          <th class="text-left">Excluir</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(categoria, index) in categorias" :key="index">
          <td>{{ categoria.name }}</td>
          <td>Butao</td>
        </tr>
      </tbody>
    </v-table>

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
      categorias: []
    }
  },
  methods: {
    async getCategorias() {
      let url = '/categories'

      try {
        const response = await axiosMyGrowMoney(url)
        console.log('categorias novas', response.data)

        this.categorias = response.data.categories
      } catch (error) {
        console.error(error)
      }
    }
  },
  async mounted() {
    await this.getCategorias()
  }
}
</script>
