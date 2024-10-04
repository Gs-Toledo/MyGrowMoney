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
    ) {
        User userFoundByEmail = userRepository.findByEmail(email);

        if (userFoundByEmail != null) {
            throw new RuntimeException("Email already registered: " + email);
        }

        User user = new User(
            name,
            email,
            password
        );

        return userRepository.save(user);
    }

    public User signIn (String email, String password) {
        User user = userRepository.findByEmail(email);

        if (user == null) {
            throw new RuntimeException("User was not found: " + email);
        }

        return user;
    }
    
}
