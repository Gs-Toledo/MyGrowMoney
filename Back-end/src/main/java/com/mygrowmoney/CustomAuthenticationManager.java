package com.mygrowmoney;

import java.util.Arrays;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.BadCredentialsException;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;

import com.mygrowmoney.models.User;
import com.mygrowmoney.repositories.UserRepository;

@Component
public class CustomAuthenticationManager implements AuthenticationManager {
    @Autowired
    UserRepository userRepository;

    @Override
    public Authentication authenticate(Authentication authentication) throws AuthenticationException {
        PasswordEncoder passwordEncoder = new SimplePasswordEncoder();

        System.out.println("authenticate");

        User user = userRepository.findByEmail(authentication.getPrincipal().toString());

        if (user == null) {
            throw new UsernameNotFoundException("User not found:" + authentication.getPrincipal());
        }

        if (!passwordEncoder.matches(authentication.getCredentials().toString(), user.getPassword())) {
            throw new BadCredentialsException("Password does not match");
        }

        System.out.println("Authencation user: " + user);

        return UsernamePasswordAuthenticationToken.authenticated(
            authentication.getPrincipal(),
            authentication.getCredentials(),
            Arrays.asList(
                new GrantedAuthority[] {
                    new SimpleGrantedAuthority("User")
                }
            )
        );
    }

    public static class SimplePasswordEncoder implements PasswordEncoder {
        @Override
        public String encode(CharSequence rawPassword) {
            return rawPassword.toString();
        }
    
        @Override
        public boolean matches(CharSequence rawPassword, String encodedPassword) {
            return rawPassword.toString().equals(encodedPassword);
        }
    }
}
