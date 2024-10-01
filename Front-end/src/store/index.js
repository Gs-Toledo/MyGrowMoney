import { createStore } from 'vuex'
import AuthService from '@/services/AuthService';
import createPersistedState from 'vuex-persistedstate';

export default createStore({
    state: {
        token: null
    },
    mutations: {
        setToken(state, token) {
            state.token = token;
        },
    },
    actions: {
        async login({ commit }, credentials) {
            try {
                const response = await AuthService.login(credentials);
                console.log(response)
                const token = response.access_token;

                commit('setToken', token);

                return token;
            } catch (error) {
                console.error('Erro na action de fazer login', error);
                throw error;
            }
        },
        logout({ commit }, router) {
            AuthService.logout(router);
            commit('setToken', null);
        }
    },
    getters: {
        isAuthenticated: state => !!state.token,
        getToken: state => state.token,
    },
    plugins: [
        createPersistedState({
            key: 'acess_token',
            paths: ['token'],
        }),
    ],
})
