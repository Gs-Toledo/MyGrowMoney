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
import com.mygrowmoney.services.AuthService;

import java.util.HashMap;

@RestController
public class AuthController {
    @Autowired
    private AuthService auth;

    @Autowired
    private AuthenticationManager authenticationManager;


    @PostMapping(value = "/sign-in", produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<Void> signIn (@RequestBody HashMap<String, String> body) {
        String email = body.get("email");
        String password = body.get("password");

        System.out.println(email);
        System.out.println(password);

        Authentication authenticationRequest =
			UsernamePasswordAuthenticationToken.unauthenticated(
                email,
                password
            );

        Authentication authenticationResponse =
			this.authenticationManager.authenticate(authenticationRequest);


        System.out.println(authenticationResponse.getPrincipal().toString());

        return ResponseEntity.ok().build();

        // try {
        //     auth.signIn(email, password);

        //     return ResponseEntity.status(HttpStatus.OK).build();
        // } catch (Exception ex) {
        //     System.out.println(ex.getMessage());

        //     return ResponseEntity.status(HttpStatus.OK).build();
        // }
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