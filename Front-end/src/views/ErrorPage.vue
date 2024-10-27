<!-- src/views/ErrorPage.vue -->
<template>
  <div class="error-page">
    <h1>{{ errorCode }}</h1>
    <p>{{ errorMessage }}</p>
    <router-link to="/">Voltar para a página inicial</router-link>
  </div>
</template>

<script>
export default {
  props: {
    errorCode: {
      type: Number,
      default: 404
    },
    errorMessage: {
      type: String,
      default: 'A página que você está procurando não foi encontrada.'
    }
  }
}
</script>

<style scoped>
.error-page {
  text-align: center;
  margin-top: 50px;
}
.error-page h1 {
  font-size: 5rem;
  color: #ff5252;
}
.error-page p {
  font-size: 1.5rem;
}
</style>
