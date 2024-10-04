<template>
  <v-img
    class="mx-auto my-6"
    max-width="228"
    src="https://www.creativefabrica.com/wp-content/uploads/2022/02/18/Capitalist-financial-manager-icon-Graphics-25477159-1.jpg"
  ></v-img>

  <v-card class="mx-auto pa-12 pb-8" elevation="8" max-width="448" rounded="lg">
    <div class="text-subtitle-1 text-medium-emphasis">Email</div>

    <v-text-field
      density="compact"
      placeholder="Insira o Email desejado."
      prepend-inner-icon="mdi-email-outline"
      v-model="email"
      variant="outlined"
    ></v-text-field>

    <div
      class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between"
    >
      Senha
    </div>

    <v-text-field
      :append-inner-icon="isPasswordVisible ? 'mdi-eye-off' : 'mdi-eye'"
      :type="isPasswordVisible ? 'text' : 'password'"
      density="compact"
      placeholder="Cadastre a senha desejada"
      prepend-inner-icon="mdi-lock-outline"
      variant="outlined"
      @click:append-inner="isPasswordVisible = !isPasswordVisible"
      v-model="password"
    ></v-text-field>

    <div
      class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between"
    >
      Confirmar Senha
    </div>

    <v-text-field
      type="password"
      density="compact"
      placeholder="Confirme a senha acima"
      prepend-inner-icon="mdi-lock-outline"
      variant="outlined"
      v-model="confirmPassword"
    ></v-text-field>

    <v-btn
      block
      class="mb-8"
      color="blue"
      size="large"
      variant="tonal"
      :disabled="isSendingRequest"
      @click="registerUser"
    >
      Cadastrar
    </v-btn>

    <router-link to="/login" class="text-blue-500 hover:underline">
      Voltar para Login
    </router-link>

    <div v-if="errorMessage" class="mt-4 text-red-500">
      {{ errorMessage }}
    </div>
  </v-card>
</template>

<script>
import AuthService from "@/services/AuthService";

export default {
  data() {
    return {
      email: "",
      password: "",
      confirmPassword: "",
      errorMessage: "",
      isSendingRequest: false,
      isPasswordVisible: false,
    };
  },
  methods: {
    async registerUser() {
      this.errorMessage = "";
      if (!this.validatePasswordFields()) {
        this.errorMessage = "As senhas não coincidem.";
        return;
      }

      this.isSendingRequest = true;
      try {
        const accountData = {
          email: this.email,
          password: this.password,
        };

        await AuthService.createAccount(accountData);
        alert("Cadastro concluido com sucesso!");
        this.$router.push("/login");
      } catch (error) {
        if (error.response?.data?.message) {
          this.errorMessage = error.response.data.message;
        } else {
          this.errorMessage =
            "Erro ao realizar o cadastro. Tente novamente mais tarde.";
        }
      } finally {
        this.isSendingRequest = false;
      }
    },
    validatePasswordFields() {
      return this.password === this.confirmPassword;
    },
  },
};
</script>
