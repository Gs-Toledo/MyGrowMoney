package com.mygrowmoney.services;

import com.mygrowmoney.models.User;
import com.mygrowmoney.repositories.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class AuthService {
    @Autowired
    private UserRepository userRepository;

    public User signUp (
        String name,
        String email,
        String password
    ) throws AuthServiceException {
        User userFoundByEmail = userRepository.findByEmail(email);

        if (userFoundByEmail != null) {
            throw new AuthServiceException("Email already registered: " + email);
        }

        User user = new User(
            name,
            email,
            password
        );

        return userRepository.save(user);
    }

    public User signIn (String email, String password) throws AuthServiceException {
        User user = userRepository.findByEmail(email);

        if (user == null) {
            throw new AuthServiceException("User was not found: " + email);
        }

        return user;
    }

    public static class AuthServiceException extends Exception {
        public AuthServiceException (String message) {
            super(message);
        }
    }
}
