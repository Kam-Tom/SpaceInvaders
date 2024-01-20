import pygame
import random

from Ships.AIChicken import AIChicken
from Ships.ShipModel import ShipModelFactory


class Polish(AIChicken):

    def __init__(self,ship_model_factory:ShipModelFactory):
        super().__init__(ship_model_factory)
        self.ship_model = ship_model_factory.get_ship_type((50,50),50,"Polish.jpg")
        self.rect = self.ship_model.image.get_rect()
        self.rect.center=(0,0) 
        self.life = 1

    def enable(self,x,y):
        self.rect.center=(x,y) 
        self.random_float = random.random() + 4
        self.x = x
        self.y = y

    def disable(self):
        pass

    def update(self,chickens):
        self.rect.center=(self.x,self.y)
        self.x += self.random_float
        if self.x >= 825:
            self.x = 0
            self.y += 50
        if self.y >= 450:
            self.x = 0
            self.y = 70

    def hit(self):
        self.life -= 1
        if self.life <= 0:
            pass
            # self.disable()
    
    
    
    
