package com.mygrowmoney;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.BadCredentialsException;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;

import com.mygrowmoney.models.User;
import com.mygrowmoney.repositories.UserRepository;

@Component
public class CustomAuthenticationManager implements AuthenticationManager {
    @Autowired
    UserRepository userRepository;

    @Override
    public Authentication authenticate(Authentication authentication) throws AuthenticationException {
        BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();

        System.out.println("authenticate");

        User user = userRepository.findByEmail(authentication.getPrincipal().toString());

        if (user == null) {
            throw new RuntimeException("User not found");
        }

        if (!passwordEncoder.matches(authentication.getPrincipal().toString(), user.getPassword())) {
            throw new RuntimeException("Password does not match");
        }

        System.out.println("Authencation user: " + user);

        return new UsernamePasswordAuthenticationToken(
            authentication.getPrincipal(),
            authentication.getCredentials()
        );
    }
}
