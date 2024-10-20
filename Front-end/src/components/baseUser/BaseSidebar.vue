<template>
  <v-navigation-drawer expand-on-hover rail>
    <v-list>
      <v-list-item :prepend-avatar="userImg" subtitle="Usuario X" title="User Image"></v-list-item>
    </v-list>

    <v-divider></v-divider>

    <v-list density="compact" nav>
      <router-link class="text-black" to="/receitas-despesas"
        ><v-list-item prepend-icon="mdi-piggy-bank-outline" title="Receitas/Despesas"></v-list-item
      ></router-link>
      <v-list-item prepend-icon="mdi-account-multiple" title="Sessão 2"></v-list-item>
      <v-list-item prepend-icon="mdi-star" title="Sessão 3"></v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  data() {
    return {
      userImg:
        'https://w1.pngwing.com/pngs/386/684/png-transparent-face-icon-user-icon-design-user-profile-share-icon-avatar-black-and-white-silhouette.png'
    }
  }
}
</script>
