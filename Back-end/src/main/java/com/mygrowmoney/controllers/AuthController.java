package com.mygrowmoney.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.security.core.AuthenticationException;

import com.mygrowmoney.AuthenticationService;
import com.mygrowmoney.infra.jwt.JwtService;
import com.mygrowmoney.models.User;

import java.util.HashMap;

@RestController
public class AuthController {
    @Autowired
    private AuthenticationService auth;

    @Autowired
    private JwtService jwtService;

    @PostMapping(value = "/sign-in", produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<String> signIn (@RequestBody HashMap<String, String> body) {
        String email = body.get("email");
        String password = body.get("password");

        try {
            User user = auth.signIn(email, password);

            String jwtToken = jwtService.encode(user.getEmail());

            return ResponseEntity
                .status(HttpStatus.OK)
                .body(jwtToken);
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

    @PostMapping(value = "/sign-up", produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<String> signUp (@RequestBody HashMap<String, String> body) {
        String name = body.get("name");
        String email = body.get("email");
        String password = body.get("password");

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
}