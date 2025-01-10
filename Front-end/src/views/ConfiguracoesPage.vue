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
        <v-btn class="mt-4" :disabled="isSendingRequest" type="submit"> Salvar </v-btn>
      </v-form>
    </section>
  </base-user-template>
</template>

<script>
import BaseUserTemplate from '@/components/baseUser/BaseUserTemplate.vue'

export default {
  components: {
    BaseUserTemplate
  },
  data() {
    return {
      moedaPrincipal: {},
      moedas: [],
      isSendingRequest: false,
      isLoading: false,
      hasError: false
    }
  },
  methods: {
    async atualizarMoedaPrincial() {
        
    }
  }
}
</script>
