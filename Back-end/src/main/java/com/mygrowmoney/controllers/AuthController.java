package com.mygrowmoney.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.mygrowmoney.services.AuthService;

import java.util.HashMap;

@RestController
public class AuthController {
    @Autowired
    private AuthService auth;

    @PostMapping(value = "/sign-in")
    public void signIn (@RequestBody HashMap<String, String> body) {
        String email = body.get("email");
        String password = body.get("password");

        try {
            auth.signIn(email, password);
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }

    @PostMapping(value = "/sign-up")
    public void signUp (@RequestBody HashMap<String, String> body) {
        String name = body.get("name");
        String email = body.get("email");
        String password = body.get("password");

        auth.signUp(name, email, password);
    }

    @PostMapping(value = "/sign-out")
    public void signOut () {
        
    }
}