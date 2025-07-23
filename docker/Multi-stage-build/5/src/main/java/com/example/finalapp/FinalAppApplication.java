package com.example.finalapp;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@SpringBootApplication
public class FinalAppApplication {

    public static void main(String[] args) {
        SpringApplication.run(FinalAppApplication.class, args);
    }

    @GetMapping("/")
    public String hello() {
        return "Final Docker challenge complete!";
    }
}