import axios from 'axios';
import { isEmpty } from '../utils/validationUtils';

class AuthService {
    static async login(loginData) {
        try {

            if (isEmpty(loginData.user) || isEmpty(loginData.pass)) {
                throw new ValidationError('Usuario ou senha não podem estar vazios.');
            }

            const bodyParams =
            {
                user: loginData.user,
                pass: loginData.pass
            }

            const response = await axios.post('http://localhost:8081/api/login', bodyParams);
            return response.data;
        } catch (error) {
            console.error('Erro ao realizar o login:', error);
            throw error;
        }
    }

    static async createAccount(accountData) {
        try {
            if (isEmpty(accountData.user) || isEmpty(accountData.pass)) {
                throw new ValidationError('Usuario ou senha não podem estar vazios.');
            }

            const bodyParams =
            {
                user: loginData.user,
                pass: loginData.pass
            }

            const response = await axios.post('http://localhost:8081/api/cadastro', bodyParams);
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
