package com.mygrowmoney.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.mygrowmoney.services.UserService;
import com.mygrowmoney.services.UserService.GetUserByIdOutput;

import java.util.Optional;
import java.util.UUID;
import java.net.URI;

@RequestMapping("/users")
@RestController
public class UserController {
    @Autowired
    private UserService userService;

    @GetMapping("/me")
    public ResponseEntity<Void> me () {
        try {
            Authentication authentication =  SecurityContextHolder.getContext().getAuthentication();

            UUID userId = (UUID) authentication.getPrincipal();
    
            return ResponseEntity
                .status(HttpStatus.FOUND)
                .location(new URI("/users/" + userId))
                .build();
        } catch (Exception ex) {
            System.err.println(ex);

            return ResponseEntity
                .internalServerError()
                .build();
        }
    }

    @GetMapping("/{userId}")
    public ResponseEntity<Optional<GetUserByIdOutput>> getUserById (@PathVariable UUID userId) {
        try {
            return ResponseEntity
                .ok(this.userService.getUserById(userId));
        } catch (Exception ex) {
            return ResponseEntity
                .internalServerError()
                .build();
        }
    }
}