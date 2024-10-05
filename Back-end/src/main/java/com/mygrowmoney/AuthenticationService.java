package com.mygrowmoney;

import com.mygrowmoney.models.User;
import com.mygrowmoney.repositories.UserRepository;
import com.mygrowmoney.services.AuthService.AuthServiceException;

import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
public class AuthenticationService {
    private final UserRepository userRepository;
    
    private final PasswordEncoder passwordEncoder;
    
    private final AuthenticationManager authenticationManager;

    public AuthenticationService(
        UserRepository userRepository,
        AuthenticationManager authenticationManager,
        PasswordEncoder passwordEncoder
    ) {
        this.authenticationManager = authenticationManager;
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
    }

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
        authenticationManager.authenticate(
            new UsernamePasswordAuthenticationToken(email, password)
        );

        User user = userRepository.findByEmail(email);

        if (user == null) {
            throw new RuntimeException("User not found: " + user);
        }

        return user;
    }
}