import pygame
from AIChicken import AIChicken


class Broiler(AIChicken):
    
    def __init__(self):
        self.image = pygame.image.load("vaporeon.jpg")
        new_width = 100  # specify the new width
        new_height = 100  # specify the new height
        self.image = pygame.transform.scale(self.image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.center=(400,400) 

    def update(self):
        pass

