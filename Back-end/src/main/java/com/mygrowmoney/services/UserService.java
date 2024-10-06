package com.mygrowmoney.services;

import java.util.UUID;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.mygrowmoney.models.User;
import com.mygrowmoney.repositories.UserRepository;

@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;

    public Optional<GetUserByIdOutput> getUserById (UUID userId) {
        return this.userRepository.findById(userId)
            .map(user -> new GetUserByIdOutput()
                .withId(user.getId())
                .withName(user.getName())
            );
    }

    public class GetUserByIdOutput {
        public UUID id;
        public String name;

        public GetUserByIdOutput withId (UUID id) {
            this.id = id;

            return this;
        }

        public GetUserByIdOutput withName (String name) {
            this.name = name;

            return this;
        }
    }
}
