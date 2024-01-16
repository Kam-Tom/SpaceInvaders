import pygame
import random

from Drawable import Drawable

class Missile(Drawable):
    def __init__(self, size, image_path):
        self.size = size
        self.velocity = 5
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)

    def enable(self,x,y):
        self.x = x
        self.y = y
    def disable(self):
        self.x = 0
        self.y = 0
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
    def update(self):
        self.y -= self.velocity

    def over_screen(self):
        return not (self.y > 0 and self.y < 600)
