import pygame
import random

from Drawable import Drawable
i = 0
class Missile(Drawable):
    def __init__(self, size, image_path,on_disable):
        self.size = size
        self.velocity = 5
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.on_disable = on_disable
        self.direction = 1
        self.rect = self.image.get_rect()
        global i
        print("Create : " + str(i))
        
        i+=1

    def enable(self, x, y, direction):
        self.x = x
        self.y = y
        self.velocity = 5
        self.direction = direction
        self.rect.topleft = (x, y)

    def disable(self):
        self.on_disable(self)
        self.x = 0
        self.y = 0

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def update(self):
        self.y -= self.velocity * self.direction
        self.rect.topleft = (self.x, self.y)
        if self.over_screen():
            self.disable()

    def over_screen(self):
        return not (self.y > 0 and self.y < 600)
    
    def tostring()->str:
        return "Missile"
    
    def tostring(self)->str:
        return "Missile"

