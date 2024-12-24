<template>
  <v-navigation-drawer expand-on-hover rail>
    <v-list>
      <v-list-item :prepend-avatar="userImg" subtitle="Investidor" :title="getUser.name"></v-list-item>
    </v-list>

    <v-divider></v-divider>

    <v-list density="compact" nav>
      <router-link class="text-black" to="/transacoes"
        ><v-list-item prepend-icon="mdi-piggy-bank-outline" title="Transações"></v-list-item
      ></router-link>
      <router-link class="text-black" to="/categorias">
        <v-list-item prepend-icon="mdi-account-multiple" title="Categorias"></v-list-item>
      </router-link>
      <!-- <v-list-item prepend-icon="mdi-star" title="Sessão 3"></v-list-item> -->
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  data() {
    return {
      userImg:
        'https://w1.pngwing.com/pngs/386/684/png-transparent-face-icon-user-icon-design-user-profile-share-icon-avatar-black-and-white-silhouette.png'
    }
  },
  computed: {
    ...mapGetters(['getUser'])
  }
}
</script>
