<template>
  <div>
    <v-img
      class="mx-auto my-6"
      max-width="228"
      src="https://www.creativefabrica.com/wp-content/uploads/2022/02/18/Capitalist-financial-manager-icon-Graphics-25477159-1.jpg"
    ></v-img>

    <v-card class="mx-auto pa-12 pb-8" elevation="8" max-width="448" rounded="lg">
      <v-form @submit.prevent="executeLogin">
        <div class="text-subtitle-1 text-medium-emphasis">Email</div>

        <v-text-field
          density="compact"
          placeholder="Insira o Email"
          prepend-inner-icon="mdi-email-outline"
          v-model="email"
          variant="outlined"
        ></v-text-field>

        <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
          Senha

          <!--    <a class="text-caption text-decoration-none text-blue" href="#" rel="noopener noreferrer" target="_blank">
          Esqueceu a senha?</a> -->
        </div>

        <v-text-field
          :append-inner-icon="isPasswordVisible ? 'mdi-eye-off' : 'mdi-eye'"
          :type="isPasswordVisible ? 'text' : 'password'"
          density="compact"
          placeholder="Insira a senha"
          prepend-inner-icon="mdi-lock-outline"
          variant="outlined"
          @click:append-inner="isPasswordVisible = !isPasswordVisible"
          v-model="password"
        ></v-text-field>

        <v-btn
          type="submit"
          block
          class="mb-8"
          color="blue"
          size="large"
          variant="tonal"
          :disabled="isSendingRequest"
        >
          Entrar
        </v-btn>

        <v-card-text class="text-center">
          <router-link
            class="text-blue text-decoration-none"
            to="/register"
            rel="noopener noreferrer"
          >
            Cadastre-se <v-icon icon="mdi-chevron-right"></v-icon>
          </router-link>
        </v-card-text>
        <div v-if="errorMessage" class="mt-4 text-red-500">
          {{ errorMessage }}
        </div>
      </v-form>
    </v-card>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  data() {
    return {
      email: '',
      password: '',
      errorMessage: '',
      isSendingRequest: false,
      isPasswordVisible: false
    }
  },
  methods: {
    ...mapActions(['login']),
    async executeLogin() {
      this.isSendingRequest = true
      try {
        const loginData = { email: this.email, password: this.password }
        await this.login(loginData)
        this.$router.push('/home')
      } catch (error) {
        this.errorMessage = 'Login falhou. Verifique suas credenciais.'
      } finally {
        this.isSendingRequest = false
      }
    }
  }
}
</script>
