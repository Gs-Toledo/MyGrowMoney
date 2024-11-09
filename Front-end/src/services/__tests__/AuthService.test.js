import { describe, it, expect, vi, beforeEach } from 'vitest';
import axiosMyGrowMoney from '../axios-configs';
import AuthService from '../AuthService';

// Mock axios-configs e validationUtils
vi.mock('../axios-configs');


// Mock do localStorage
// eslint-disable-next-line no-undef
global.localStorage = {
    getItem: vi.fn(),
    setItem: vi.fn(),
    removeItem: vi.fn(),
};

// Mock de router.push
const mockRouter = { push: vi.fn() };

describe('AuthService', () => {
    beforeEach(() => {
        vi.clearAllMocks();
    });

    describe('login', () => {
        it('should throw an error if email or password is empty', async () => {
            const loginData = { email: '', password: '' };

            await expect(AuthService.login(loginData)).rejects.toThrow('Usuario ou senha não podem estar vazios.');
        });

        it('should call /sign-in endpoint with correct parameters', async () => {
            const loginData = { email: 'test@example.com', password: 'password123' };
            const mockResponse = { data: { token: 'fakeToken' } };

            axiosMyGrowMoney.post.mockResolvedValue(mockResponse);

            const result = await AuthService.login(loginData);

            expect(axiosMyGrowMoney.post).toHaveBeenCalledWith('/sign-in', loginData);
            expect(result).toEqual(mockResponse.data);
        });

        it('should throw an error if axios request fails', async () => {
            const loginData = { email: 'test@example.com', password: 'password123' };

            axiosMyGrowMoney.post.mockRejectedValue(new Error('Network Error'));

            await expect(AuthService.login(loginData)).rejects.toThrow('Network Error');
        });
    });

    describe('createAccount', () => {
        it('should throw an error if email, password, or name is empty', async () => {
            const accountData = { email: '', password: '', name: '' };

            await expect(AuthService.createAccount(accountData)).rejects.toThrow('Usuario ou senha não podem estar vazios.');
        });

        it('should call /sign-up endpoint with correct parameters', async () => {
            const accountData = { email: 'newuser@example.com', password: 'newpassword', name: 'New User' };
            const mockResponse = { data: { message: 'Account created' } };

            axiosMyGrowMoney.post.mockResolvedValue(mockResponse);

            const result = await AuthService.createAccount(accountData);

            expect(axiosMyGrowMoney.post).toHaveBeenCalledWith('/sign-up', accountData);
            expect(result).toEqual(mockResponse.data);
        });
    });

    describe('logout', () => {
        it('should push to /login route and remove access_token from localStorage', () => {
            localStorage.setItem('acess_token', 'fakeToken');

            AuthService.logout(mockRouter);

            expect(mockRouter.push).toHaveBeenCalledWith('/login');

            setTimeout(() => {
                expect(localStorage.removeItem).toHaveBeenCalledWith('acess_token');
            }, 100);
        });
    });
});