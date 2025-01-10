<template>
  <base-user-template>
    <div class="title-section">
      <h2 class="mb-3 font-weight-bold text-lg">Configurações</h2>
    </div>
    <section>
      <v-form @submit.prevent="atualizarMoedaPrincial" v-if="!isLoading && !hasError">
        <v-row>
          <v-select
            label="Moeda Principal"
            :items="moedas"
            item-title="name"
            item-value="id"
            v-model="moedaPrincipal.id"
            required
          ></v-select>

          <!-- <v-col> </v-col> -->
        </v-row>
        <v-btn class="mt-4" :disabled="isSendingRequest" type="submit"> Salvar (em desenvolvimento) </v-btn>
      </v-form>
      <span class="errorDiv" v-else-if="hasError && !isLoading">Erro ao buscar dados...</span>
      <div v-else-if="isLoading && !hasError">
        <v-progress-circular indeterminate color="primary" />
      </div>
    </section>
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
      moedaPrincipal: {},
      moedas: [],
      isSendingRequest: true,
      isLoading: true,
      hasError: false
    }
  },
  methods: {
    async atualizarMoedaPrincial() {},
    async getMoedasFromApi() {
      let url = '/moedas'

      try {
        this.isLoading = true
        this.hasError = false
        const response = await axiosMyGrowMoney.get(url)

        console.log('moedas', response.data)
        this.moedas = Object.entries(response.data).map(([key, value]) => ({
            id: key, // Codigo da moeda
            name: value // Nome da moeda
        }))
        console.log(this.moedas)
      } catch (error) {
        console.error(error)
        this.hasError = true
      } finally {
        this.isLoading = false
      }
    }
  },
  async mounted() {
    await this.getMoedasFromApi()
  }
}
</script>
