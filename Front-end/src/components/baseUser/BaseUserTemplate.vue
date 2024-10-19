<template>
  <v-app>
    <base-header />
    <v-main>
      <v-container>
        <slot></slot>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import BaseHeader from "@/components/baseUser/BaseHeader.vue";
export default {
  components: {
    BaseHeader,
  },
};
</script>
