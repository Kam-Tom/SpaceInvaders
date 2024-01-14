import pygame
from AIChicken import AIChicken


class Polish(AIChicken):

    def __init__(self):
        self.image = pygame.image.load("vaporeon.jpg")
        self.rect = self.image.get_rect()
        self.rect.center=(80,0) 
        self.image = pygame.transform.scale(self.image, (64,64))

    def update(self):
        self.rect.center=(self.x,self.y)
        self.y -= 1

    def disable(self):
        pass
    
    def enable(self,x,y):
        self.rect.center=(x,y) 
        self.x = x
        self.y = y
    
    
