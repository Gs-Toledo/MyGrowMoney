package com.mygrowmoney.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.AuthenticationException;

import com.mygrowmoney.services.AuthService;

import java.util.HashMap;


@RestController
public class AuthController {
    @Autowired
    private AuthService auth;

    @Autowired
    private AuthenticationManager authenticationManager;


    @PostMapping(value = "/sign-in", produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<String> signIn (@RequestBody HashMap<String, String> body) {
        String email = body.get("email");
        String password = body.get("password");

        System.out.println("Email: " + email);
        System.out.println("Password: " + password);

        try {
            Authentication authentication = authenticationManager.authenticate(
                UsernamePasswordAuthenticationToken.unauthenticated(email, password)
            );

            return ResponseEntity
                .status(HttpStatus.OK)
                .body("" + authentication.isAuthenticated());
        } catch (AuthenticationException exception) {
            return ResponseEntity
                .status(HttpStatus.BAD_REQUEST)
                .body(exception.getMessage());
        } catch (Exception exception) {
            return ResponseEntity
                .status(HttpStatus.INTERNAL_SERVER_ERROR)
                .body(exception.getMessage());
        }
    }

    @PostMapping(value = "/sign-up")
    public ResponseEntity<String> signUp (@RequestBody HashMap<String, String> body) {
        String name = body.get("name");
        String email = body.get("email");
        String password = body.get("password");

        System.out.println("Email: " + email);
        System.out.println("Password: " + password);
        System.out.println("Name: " + name);

        try {
            auth.signUp(name, email, password);

            return ResponseEntity
                .status(HttpStatus.CREATED)
                .build();
        } catch (Exception exception) {
            return ResponseEntity
                .status(HttpStatus.INTERNAL_SERVER_ERROR)
                .body(exception.getMessage());
        }
    }

    @PostMapping(value = "/sign-out")
    public void signOut () {
        
    }
}