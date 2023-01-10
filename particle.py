import pygame

class Particle:
    def __init__(self, x, y, image, screen):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 5
        self.screen = screen

    def update(self):
        self.rect.x += self.speed
        if self.rect.right > self.screen.get_width():  # If the particle goes off the screen
            self.rect.left = 0  # Wrap it around to the left side