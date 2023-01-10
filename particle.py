#particle.py

import pygame

class Particle:
    def __init__(self, x, y, screen, bullets, bullet_color, distance, draw_text_fn):
        self.x = x
        self.y = y
        self.speed = 5
        self.screen = screen
        self.bullets = bullets
        self.bullet_color = bullet_color
        self.distance = distance
        self.draw_text = draw_text_fn

    def update(self):
        self.x += self.speed
        self.y += self.speed
        if self.x > self.screen.get_width() or self.y > self.screen.get_height(): 
            self.bullets.remove(self)
        self.draw_text(self.screen, "-", self.x, self.y, color=self.bullet_color)

#     def update(self):
#         self.x += self.speed
#         if self.x > len(self.map[0])*16: #if it goes off screen
#             self.x = 0
#         self.draw_text(self.screen, self.bullet_char, self.x, self.y, color=self.bullet_color)