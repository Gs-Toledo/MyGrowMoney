import { isEmpty } from '../utils/validationUtils';
import axiosMyGrowMoney from './axios-configs';

class AuthService {
    static async login(loginData) {
        try {

            if (isEmpty(loginData.email) || isEmpty(loginData.password)) {
                throw new Error('Usuario ou senha não podem estar vazios.');
            }

            const bodyParams =
            {
                email: loginData.email,
                password: loginData.password
            }

            const response = await axiosMyGrowMoney.post('/sign-in', bodyParams);
            return response.data;
        } catch (error) {
            console.error('Erro ao realizar o login:', error);
            throw error;
        }
    }

    static async createAccount(accountData) {
        try {
            if (isEmpty(accountData.email) || isEmpty(accountData.password) || isEmpty(accountData.name)) {
                throw new Error('Usuario ou senha não podem estar vazios.');
            }

            const bodyParams =
            {
                name: accountData.name,
                email: accountData.email,
                password: accountData.password
            }

            const response = await axiosMyGrowMoney.post('/sign-up', bodyParams);
            return response.data;
        } catch (error) {
            console.error('Erro ao realizar o Cadastro:', error);
            throw error;
        }
    }

    static logout(router) {
        router.push('/login');
        setTimeout(() => {
            localStorage.removeItem('loggedUser');
        }, 100);
    }
}

export default AuthService;
