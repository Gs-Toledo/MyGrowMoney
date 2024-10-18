<template>
  <v-app>
    <base-header />
    <v-main>
      <v-container class="fill-height justify-center">
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
