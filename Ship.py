import pygame
from Drawable import Drawable
from abc import ABC, abstractmethod 

class Ship(Drawable,ABC):
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

