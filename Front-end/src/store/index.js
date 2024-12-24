import { createStore } from 'vuex'
import AuthService from '@/services/AuthService';
import createPersistedState from 'vuex-persistedstate';

export default createStore({
    state: {
        token: null,
        user: null
    },
    mutations: {
        setToken(state, token) {
            state.token = token;
        },
        setUser(state, user) {
            state.user = user;
        }
    },
    actions: {
        async login({ commit }, credentials) {
            try {
                const response = await AuthService.login(credentials);
                const token = response.accessToken;
                const user = response.user;

                commit('setToken', token);
                commit('setUser', user);

                return token;
            } catch (error) {
                console.error('Erro na action de fazer login', error);
                throw error;
            }
        },
        logout({ commit }, router) {
            AuthService.logout(router);
            commit('setToken', null);
            commit('setUser', null);
        }
    },
    getters: {
        isAuthenticated: state => !!state.token,
        getToken: state => state.token,
        getUser: state => state.user
    },
    plugins: [
        createPersistedState({
            key: 'loggedUser',
            paths: ['token', 'user']
        }),
    ],
})
