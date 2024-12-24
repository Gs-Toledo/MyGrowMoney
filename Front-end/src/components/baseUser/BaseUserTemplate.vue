<template>
  <v-app>
    <base-header />
    <v-main>
      <div id="toast-container"></div>
      <base-sidebar />
      <v-container>
        <slot></slot>
      </v-container>
    </v-main>
    
  </v-app>
</template>

<script>
import BaseHeader from '@/components/baseUser/BaseHeader.vue'
import BaseSidebar from '@/components/baseUser/BaseSidebar.vue'

export default {
  components: {
    BaseHeader,
    BaseSidebar
  }
}
</script>
