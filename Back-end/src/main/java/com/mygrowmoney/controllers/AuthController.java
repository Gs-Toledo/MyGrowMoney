package com.mygrowmoney.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.mygrowmoney.AuthenticationService;
import com.mygrowmoney.AuthenticationService.SignInOutput;
import com.mygrowmoney.AuthenticationService.SignUpOutput;

import java.util.HashMap;

@RestController
public class AuthController {
    @Autowired
    private AuthenticationService auth;

    @PostMapping(value = "/sign-in", produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<SignInOutput> signIn (@RequestBody HashMap<String, String> body) {
        String email = body.get("email");
        String password = body.get("password");

        try {
            SignInOutput signInOutput = auth.signIn(email, password);

            return ResponseEntity
                .ok()
                .body(signInOutput);
        } catch (Exception exception) {
            System.err.println(exception);
            return ResponseEntity
                .internalServerError()
                .build();
        }
    }

    @PostMapping(value = "/sign-up", produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<SignUpOutput> signUp (@RequestBody HashMap<String, String> body) {
        String name = body.get("name");
        String email = body.get("email");
        String password = body.get("password");

        try {
            SignUpOutput signUpOutput = auth.signUp(name, email, password);

            return ResponseEntity
                .ok()
                .body(signUpOutput);
        } catch (Exception exception) {
            return ResponseEntity
                .internalServerError()
                .build();
        }
    }
}