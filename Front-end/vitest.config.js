// vitest.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue';
import path from 'path'

export default defineConfig({
  plugins: [vue()],
  test: {
    globals: true,
    environment: 'jsdom',
    css: false,
    server: {
      deps: {
        inline: ['vuetify']
      }
    }
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'), // Configura o alias @ para apontar para ./src
    },
  },
})
