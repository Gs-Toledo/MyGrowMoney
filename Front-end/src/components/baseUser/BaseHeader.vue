<template>
  <v-app-bar :elevation="2">
    <v-app-bar-title
      ><router-link class="text-black hover:text-blue-700" to="/home"
        >My Grow Money</router-link
      ></v-app-bar-title
    >
    <template v-slot:append>
      <v-btn icon="mdi-dots-vertical"></v-btn>
      <v-btn icon="mdi-logout" @click="showLogoutModal = true"></v-btn>
    </template>
  </v-app-bar>

  <v-dialog v-model="showLogoutModal" max-width="400">
    <v-card>
      <v-card-title class="headline">Confirmar Logout</v-card-title>
      <v-card-text>Você tem certeza que deseja sair?</v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text @click="showLogoutModal = false">Cancelar</v-btn>
        <v-btn color="blue darken-1" text @click="userlogout">Confirmar</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import router from '@/router'
import { mapActions } from 'vuex'

export default {
  data() {
    return {
      showLogoutModal: false
    }
  },
  methods: {
    ...mapActions(['logout']),
    userlogout() {
      console.log('deslogando...')
      this.logout(router)
      this.showLogoutModal = false
    }
  }
}
</script>
