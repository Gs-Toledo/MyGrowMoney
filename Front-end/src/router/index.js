import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store';
import LoginPage from '@/views/LoginPage.vue';
import UserRegister from '@/views/UserRegister.vue';
import HomePage from '@/views/HomePage.vue'
import ErrorPage from '@/views/ErrorPage.vue';
import CadastroReceitasDespesasPage from '@/views/CadastroReceitasDespesasPage.vue';
import CategoriasPage from '@/views/CategoriasPage.vue';

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
        path: '/:catchAll(.*)',
        name: 'NotFound',
        component: ErrorPage,
        props: {
            errorCode: 404,
            errorMessage: 'A página que você está procurando não foi encontrada.',
        },
        meta: { title: 'Erro 404 - Não Encontrado' }
    },
    {
        path: '/forbidden',
        name: 'Forbidden',
        component: ErrorPage,
        props: {
            errorCode: 403,
            errorMessage: 'Você não tem permissão para acessar esta página.',
        },
        meta: { title: 'Erro 403 - Proibido' }
    },
    {
        path: '/login',
        name: 'Login',
        component: LoginPage,
        meta: { title: 'Login' }
    },
    {
        path: '/register',
        name: 'Register',
        component: UserRegister,
        meta: { title: 'Cadastro' }
    },
    {
        path: '/home',
        name: 'Home',
        component: HomePage,
        meta: { title: 'Home' }
    },
    {
        path: '/receitas-despesas',
        name: 'CadastrarReceitasDespesas',
        component: CadastroReceitasDespesasPage,
        meta: { title: 'Receitas e Despesas' }
    },
    {
        path: '/categorias',
        name: 'Categorias',
        component: CategoriasPage,
        meta: { title: 'Categorias' }
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
