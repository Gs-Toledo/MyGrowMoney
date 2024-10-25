import axios from 'axios';
import store from '@/store';
import AuthService from './AuthService';
import router from '@/router';

const axiosMyGrowMoney = axios.create({
    baseURL: 'http://localhost:5000/',
});


axiosMyGrowMoney.interceptors.request.use(
    config => {
        const token = store.getters.getToken;
        if (token) {
            config.headers['Authorization'] = `Bearer ${token}`;
        }
        return config;
    },
    error => {
        return Promise.reject(error);
    }
);


axiosMyGrowMoney.interceptors.response.use(
    response => response,
    error => {
        if (error.response && error.response.status === 401) {

            console.error('Token inválido ou expirado');
            AuthService.logout(router)
        }
        return Promise.reject(error);
    }
);

export default axiosMyGrowMoney;
