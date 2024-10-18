import axios from 'axios';
import { isEmpty } from '../utils/validationUtils';

class AuthService {
    static async login(loginData) {
        try {

            if (isEmpty(loginData.email) || isEmpty(loginData.password)) {
                throw new ValidationError('Usuario ou senha não podem estar vazios.');
            }

            const bodyParams =
            {
                email: loginData.email,
                password: loginData.password
            }

            const response = await axios.post('http://localhost:5000/api/login', bodyParams);
            return response.data;
        } catch (error) {
            console.error('Erro ao realizar o login:', error);
            throw error;
        }
    }

    static async createAccount(accountData) {
        try {
            if (isEmpty(accountData.email) || isEmpty(accountData.password)) {
                throw new ValidationError('Usuario ou senha não podem estar vazios.');
            }

            const bodyParams =
            {
                email: loginData.email,
                password: loginData.password
            }

            const response = await axios.post('http://localhost:5000/api/cadastro', bodyParams);
            return response.data;
        } catch (error) {
            console.error('Erro ao realizar o Cadastro:', error);
            throw error;
        }
    }

    static logout(router) {
        router.push('/login');
        setTimeout(() => {
            localStorage.removeItem('acess_token');
        }, 100);
    }
}

export default AuthService;
