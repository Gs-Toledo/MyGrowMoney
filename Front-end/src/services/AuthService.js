import axios from 'axios';

class AuthService {
    static async login(loginData) {
        try {
            const params = new URLSearchParams(
                {
                    user: loginData.user, 
                    pass: loginData.pass
                }
            );

            const response = await axios.post('http://localhost:8081/api/login', params);
            return response.data;
        } catch (error) {
            console.error('Erro ao realizar o login:', error);
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
