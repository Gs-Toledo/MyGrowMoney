import { createApp } from 'vue'
import App from './App.vue'
import store from '@/store'
import router from '@/router'
import vuetify from '@/plugins/vuetify'
import './style.css'
import "vue-toastification/dist/index.css";

import Toast from 'vue-toastification';
import toastOptions from '@/configs/toast';

const app = createApp(App)


app.use(router)
app.use(store)
app.use(vuetify)
app.use(Toast, toastOptions);
app.mount('#app')


