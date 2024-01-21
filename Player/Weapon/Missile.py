import pygame
from Drawable import Drawable
from constants import SCREEN_HEIGHT

class Missile(Drawable):
    def __init__(self, size, image_path,on_disable):
        self.size = size
        self.velocity = 5
        self.image = pygame.image.load("Sprites/"+image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.on_disable = on_disable
        self.rect = self.image.get_rect()

    def enable(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 5
        self.rect.topleft = (x, y)

    def disable(self, obj):
        self.on_disable(obj)
        self.x = 0
        self.y = 0

    def draw(self, surface):
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        surface.blit(self.image, (self.x, self.y))

    def update(self):
        self.y -= self.velocity
        self.rect.topleft = (self.x, self.y)
        # if self.over_screen():
        #     self.disable(self)

    def over_screen(self):
        return not (self.y > 0 and self.y < SCREEN_HEIGHT)
    
    def check_colision(self, obj):
        pass
    
