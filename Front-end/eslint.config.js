import globals from "globals";
import pluginJs from "@eslint/js";
import pluginVue from "eslint-plugin-vue";


export default [
  {
    files: ["**/*.{js,mjs,cjs,vue}"],
    languageOptions: {
      globals: globals.browser,
    },
    plugins: {
      js: pluginJs,
      vue: pluginVue,
    },
  },
  pluginJs.configs.recommended,
  pluginVue.configs["essential"],
  {
    extends: [
      "plugin:vue/vue3-recommended",
      "airbnb-base",
    ],
    plugins: [
      "vue",
    ],
  },
];