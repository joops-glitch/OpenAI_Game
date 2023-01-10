#particle.py

import pygame

class Particle:
    def __init__(self, x, y, image, screen, bullets, distance):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 5
        self.screen = screen
        self.distance = distance
        self.bullets = bullets

    def update(self):
        self.rect.x += self.speed
        if self.rect.right > self.screen.get_width():  # If the particle goes off the screen
            self.rect.left = 0  # Wrap it around to the left side
        if self.rect.x > self.distance:  # If the particle has traveled the set distance
            self.kill()  # Remove the particle from the bullets list
        
    def kill(self):
        self.bullets.remove(self)