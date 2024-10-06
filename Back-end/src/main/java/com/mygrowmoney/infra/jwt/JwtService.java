package com.mygrowmoney.infra.jwt;

import io.jsonwebtoken.impl.DefaultJwtBuilder;
import io.jsonwebtoken.impl.DefaultJwtParserBuilder;
import io.jsonwebtoken.io.Decoders;
import io.jsonwebtoken.security.Keys;

import java.security.Key;
import java.util.Date;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

@Service
public class JwtService {
    @Value("${security.jwt.secret-key}")
    private String secretKey;

    @Value("${security.jwt.expiration-time}")
    private long expiration;

    private Key getSignInKey () {
        return Keys.hmacShaKeyFor(Decoders.BASE64.decode(secretKey));
    }

    public String encode (String subject) {
        if (subject == null || subject.isEmpty()) {
            throw new IllegalArgumentException("Subject cannot be null or empty.");
        }

        return new DefaultJwtBuilder()
            .subject(subject)
            .issuedAt(new Date(System.currentTimeMillis()))
            .expiration(new Date(System.currentTimeMillis() + expiration))
            .signWith(getSignInKey())
            .compact();
    }

    public String decode (String token) {
        if (token == null || token.isEmpty()) {
            throw new IllegalArgumentException("Token cannot be null or empty.");
        }

        String subject = new DefaultJwtParserBuilder()
            .setSigningKey(getSignInKey())
            .build()
            .parseSignedClaims(token)
            .getPayload()
            .getSubject();

        if (subject == null || subject.isEmpty()) {
            throw new IllegalStateException("Token does not have a valid subject claim.");
        }

        return subject;
    }

    public static class JwtToken {}
}