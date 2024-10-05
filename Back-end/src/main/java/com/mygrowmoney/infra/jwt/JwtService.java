package com.mygrowmoney.infra.jwt;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.JwtParserBuilder;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.impl.DefaultJwtBuilder;
import io.jsonwebtoken.impl.DefaultJwtParserBuilder;
import io.jsonwebtoken.io.Decoders;
import io.jsonwebtoken.security.Keys;
import java.security.Key;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.function.Function;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Service;
import io.jsonwebtoken.security.SecureDigestAlgorithm;

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
        return new DefaultJwtBuilder()
            .subject(subject)
            .issuedAt(new Date(System.currentTimeMillis()))
            .expiration(new Date(System.currentTimeMillis() + expiration))
            .signWith(getSignInKey())
            .compact();
    }

    public String decode (String token) {
        return new DefaultJwtParserBuilder()
            .setSigningKey(getSignInKey())
            .build()
            .parseUnsecuredClaims(token)
            .getPayload()
            .getSubject();
    }

    public static class JwtToken {}
}