from Drawable import Drawable
import pygame
from constants import SCREEN_HEIGHT, EGG_VELOCITY

class Egg(Drawable):
    def __init__(self, size, image_path,on_disable):
        self.size = size
        self.velocity = EGG_VELOCITY
        self.image = pygame.image.load("Sprites/"+image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.on_disable = on_disable
        self.rect = self.image.get_rect()

    def enable(self, x, y):
        self.x = x
        self.y = y
        self.velocity = EGG_VELOCITY

    def disable(self):
        self.on_disable(self)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def update(self):
        self.y += self.velocity
        self.rect.topleft = (self.x, self.y)
        if self.over_screen():
            self.disable()

    def over_screen(self):
        return not (self.y > 0 and self.y < SCREEN_HEIGHT)
    
    def check_colision(self, obj):
        pass
    
