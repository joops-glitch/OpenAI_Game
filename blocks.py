#blocks.py

import pygame

class Platform:
    def __init__(self, x, y, width, height, image):
        self.image = image
        self.rect = pygame.Rect(x, y, width, height)
    
    def update(self):
        # Update the platform's position, if necessary
        pass