<template>
    ola home
</template>

<script>
export default {
  data() {
    return {
      transacoes: [
        { description: "Salário", type: "receita", amount: 5000 },
        { description: "Aluguel", type: "despesa", amount: 1500 },
        { description: "Supermercado", type: "despesa", amount: 800 },
        { description: "Freelance", type: "receita", amount: 2200 },
      ],
    };
  },
};
</script>

<style scoped>
.v-card-title {
  font-weight: bold;
}
</style>
