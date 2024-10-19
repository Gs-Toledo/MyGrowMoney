<template>
  <v-app>
    <base-header />
    <v-main>
      <v-navigation-drawer expand-on-hover rail>
        <v-list>
          <v-list-item
            :prepend-avatar="userImg"
            subtitle="Usuario X"
            title="User Image"
          ></v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list density="compact" nav>
          <v-list-item prepend-icon="mdi-folder" title="Sessão 1"></v-list-item>
          <v-list-item prepend-icon="mdi-account-multiple" title="Sessão 2"></v-list-item>
          <v-list-item prepend-icon="mdi-star" title="Sessão 3"></v-list-item>
        </v-list>
      </v-navigation-drawer>

      <v-container>
        <slot></slot>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import BaseHeader from '@/components/baseUser/BaseHeader.vue'
export default {
  components: {
    BaseHeader
  },
  data() {
    return {
      userImg: 'https://w1.pngwing.com/pngs/386/684/png-transparent-face-icon-user-icon-design-user-profile-share-icon-avatar-black-and-white-silhouette.png'
    }
  }
}
</script>
