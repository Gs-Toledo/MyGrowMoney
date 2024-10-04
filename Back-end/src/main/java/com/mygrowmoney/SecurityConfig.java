package com.mygrowmoney;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.stereotype.Service;

import org.springframework.security.config.http.SessionCreationPolicy;

import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;

@Configuration
@EnableWebSecurity
public class SecurityConfig {
    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
            .csrf(csrf -> csrf.disable())  // Disable CSRF for APIs
            .authorizeHttpRequests(authorize -> authorize
                .requestMatchers("/sign-in", "/sign-up", "/error").permitAll()  // Allow access to auth endpoints
                .anyRequest().authenticated()  // Protect all other endpoints
            )
            .sessionManagement(sessionManagement -> sessionManagement
                .sessionCreationPolicy(SessionCreationPolicy.IF_REQUIRED) // Set session creation policy
                .maximumSessions(1)  // Only allow one session per user
            );

        return http.build();
    }

    @Service
    public static class UserDetailsServiceImpl implements UserDetailsService {
        public UserDetails loadUserByUsername (String username) throws UsernameNotFoundException {
            System.out.println("loadUserByUsername");

            return null;
        }
    }
}