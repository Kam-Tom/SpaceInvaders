import pygame
from AIChicken import AIChicken


class Leghorn(AIChicken):
    
    def __init__(self):
        self.image = pygame.image.load("vaporeon.jpg")
        self.rect = self.image.get_rect()
        self.rect.center=(80,0) 

    def update(self):
        pass

