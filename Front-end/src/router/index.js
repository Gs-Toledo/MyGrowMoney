import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store';
import LoginPage from '@/views/LoginPage.vue';

const routes = [
    {
        path: '/',
        name: 'Root',
        beforeEnter: (to, from, next) => {
            if (store.getters.isAuthenticated) {
                next('/home');
            } else {
                next('/login');
            }
        }
    },
    {
        path: '/login',
        name: 'Login',
        component: LoginPage
    },

]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes
})

export default router
