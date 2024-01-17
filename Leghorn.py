import pygame
import random
from AIChicken import AIChicken
from ShipModel import ShipModelFactory


class Leghorn(AIChicken):
    
    def __init__(self,ship_model_factory:ShipModelFactory):
        self.ship_model = ship_model_factory.get_ship_type((50,50),50,"vaporeon.jpg")
        self.rect = self.ship_model.image.get_rect()
        self.rect.center=(0,0) 

    def disable(self):
        pass
    def enable(self, x, y):
        self.rect.center=(x,y) 
        self.random_float = 2*random.random() - 1
        self.x = x
        self.y = y
    def update(self):
        self.x += self.random_float
        self.y += self.random_float
        self.rect.center=(self.x,self.y) 
        if self.x > 825:
            self.x = -25
        if self.y > 625:
            self.y = -25
        if self.x < -25:
            self.x = 825
        if self.y < -25:
            self.y = 625

