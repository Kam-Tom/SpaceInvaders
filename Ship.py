import pygame
from Drawable import Drawable
from abc import ABC, abstractmethod 
from ShipType import ShipType

class Ship(Drawable,ABC):
    # def __init__(self,ship_type:ShipType):
    #     self.ship_type = ship_type
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)

