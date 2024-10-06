package com.mygrowmoney;

import com.mygrowmoney.infra.jwt.JwtService;
import com.mygrowmoney.models.User;
import com.mygrowmoney.repositories.UserRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.BadCredentialsException;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.stereotype.Service;

@Service
public class AuthenticationService {
    @Autowired
    private UserRepository userRepository;
    
    @Autowired
    private JwtService jwtService;
    
    @Autowired
    private AuthenticationManager authenticationManager;

    public SignUpOutput signUp (
        String name,
        String email,
        String password
    ) {
        if (name == null || name.isEmpty()) {
            throw new IllegalArgumentException("Name cannot be null or empty");
        }

        if (email == null || email.isEmpty()) {
            throw new IllegalArgumentException("Email cannot be null or empty");
        }

        if (password == null || password.isEmpty()) {
            throw new IllegalArgumentException("Password cannot be null or empty");
        }

        User userFoundByEmail = userRepository.findByEmail(email);

        if (userFoundByEmail != null) {
            return new SignUpOutput()
                .withSuccess(false)
                .withMessage("Email already registered");
        }

        User user = new User(
            name,
            email,
            password
        );

        userRepository.save(user);

        return new SignUpOutput()
            .withSuccess(true)
            .withMessage("Signed up successfully");
    }

    public SignInOutput signIn (
        String email,
        String password
    ) {
        if (email == null || email.isEmpty()) {
            throw new IllegalArgumentException("Email cannot be null or empty");
        }

        if (password == null || password.isEmpty()) {
            throw new IllegalArgumentException("Password cannot be null or empty");
        }

        try {
            authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(email, password)
            );
        } catch (BadCredentialsException exception) {
            return new SignInOutput()
                .withSuccess(false)
                .withMessage("User not found or password does not match");
        }

        User user = userRepository.findByEmail(email);

        String accessToken = jwtService.encode(user.getId().toString());

        return new SignInOutput()
            .withSuccess(true)
            .withMessage("Signed in sucessfully")
            .withAccessToken(accessToken);
    }

    public static class SignInOutput {
        public Boolean success;
        public String message;
        public String accessToken;

        public SignInOutput withSuccess (Boolean success) {
            this.success = success;

            return this;
        }

        public SignInOutput withMessage (String message) {
            this.message = message;

            return this;
        }

        public SignInOutput withAccessToken (String accessToken) {
            this.accessToken = accessToken;

            return this;
        }
    }

    public static class SignUpOutput {
        public Boolean success;
        public String message;

        public SignUpOutput withSuccess (Boolean success) {
            this.success = success;

            return this;
        }

        public SignUpOutput withMessage (String message) {
            this.message = message;

            return this;
        }
    }

}