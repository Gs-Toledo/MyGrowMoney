import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store';
import LoginPage from '@/views/LoginPage.vue';
import UserRegister from '../views/UserRegister.vue';
import HomePage from '@/views/HomePage.vue'

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
        component: LoginPage,
        meta: {title: 'Login'}
    },
    {
        path: '/register',
        name: 'Register',
        component: UserRegister,
        meta: {title: 'Cadastro'}
    },
    {
    path: '/home',
    name: 'Home',
    compo: HomePage,
    meta: {title: 'Home'}
}

]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes
})

//Hook para pegar o titulo das rotas
router.beforeEach((to, from, next) => {
    document.title = to.meta.title || 'App';
    next();
});

export default router
