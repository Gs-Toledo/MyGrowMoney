package com.mygrowmoney;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.GetMapping;

@RestController()
public class HelloWorldController {
    @GetMapping("/")
    public String get () {
        return "Hello, World!";
    }   
}
