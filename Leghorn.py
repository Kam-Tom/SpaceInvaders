import pygame
from Ship import Ship


class Leghorn(Ship):
    
    def __init__(self):
        self.image = pygame.image.load("vaporeon.jpg")
        self.rect = self.image.get_rect()
        self.rect.center=(80,0) 

    def update(self):
        pass

