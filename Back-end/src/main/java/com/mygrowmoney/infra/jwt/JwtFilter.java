package com.mygrowmoney.infra.jwt;

import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import org.hibernate.mapping.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.lang.NonNull;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.web.authentication.WebAuthenticationDetailsSource;
import org.springframework.stereotype.Component;
import org.springframework.web.client.HttpClientErrorException.Forbidden;
import org.springframework.web.filter.OncePerRequestFilter;

import com.mygrowmoney.models.User;
import com.mygrowmoney.repositories.UserRepository;

import io.jsonwebtoken.lang.Arrays;
import io.jsonwebtoken.lang.Collections;

import java.io.IOException;
import java.util.UUID;

@Component
public class JwtFilter extends OncePerRequestFilter {
    @Autowired
    private JwtService jwtService;

    @Autowired
    private UserRepository userRepository;

    @Override
    protected void doFilterInternal(
        @NonNull HttpServletRequest request,
        @NonNull HttpServletResponse response,
        @NonNull FilterChain filterChain
    ) throws ServletException, IOException {
        final String authorizationHeader = request.getHeader("Authorization");

        System.out.println("Authorization: " + authorizationHeader);
        
        if (authorizationHeader != null && authorizationHeader.startsWith("Bearer ")) {
            final String jwtToken = authorizationHeader.substring(7);
            final String jwtSubject = jwtService.decode(jwtToken);

            Authentication authentication = SecurityContextHolder.getContext().getAuthentication();

            if (jwtSubject != null && authentication == null) {
                UUID userId = UUID.fromString(jwtSubject);

                User user = this.userRepository.findById(userId)
                    .orElseThrow(() -> new IllegalStateException("User not found: " + userId + "."));

                UsernamePasswordAuthenticationToken authToken = new UsernamePasswordAuthenticationToken(
                    user.getId(),
                    user.getPassword(),
                    Collections.emptyList()
                );

                // authToken.setDetails(new WebAuthenticationDetailsSource().buildDetails(request));

                SecurityContextHolder.getContext().setAuthentication(authToken);
            }
        }

        filterChain.doFilter(request, response);
    }
}