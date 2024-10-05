package com.mygrowmoney.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;
import java.util.UUID;

import com.mygrowmoney.models.User;

public interface UserRepository extends JpaRepository<User, UUID>{
    User findByEmail(String email);
}