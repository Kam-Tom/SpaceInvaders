import pygame
from AIChicken import AIChicken
from ShipModel import ShipModelFactory
import random

class Broiler(AIChicken):
    
    def __init__(self,ship_model_factory:ShipModelFactory):
        super().__init__(ship_model_factory)
        self.ship_model = ship_model_factory.get_ship_type((10,50),50,"Leghorn.jpg")
        self.rect = self.ship_model.image.get_rect()
        self.rect.center=(0,0)
        self.missiles = []

    def disable(self):
        pass
    
    def enable(self, x, y):
        y = random.randint(0, 312)
        self.rect.center=(x,y) 
        self.random_float = 2*random.random() - 1
        self.x = x
        self.y = y

    def update(self, chickens):
        super().update()
        self.x += self.random_float
        self.y += self.random_float
        self.rect.center=(self.x,self.y) 
        if self.x > 825:
            self.x = -25
        if self.y > 312:
            self.random_float = -abs(self.random_float)
        if self.x < -25:
            self.x = 825
        if self.y < -25:
            self.y = random.randint(0, 312)
        if self.y < 0:
            self.random_float = abs(self.random_float)
        for chicken in chickens:
            if self != chicken and pygame.sprite.collide_rect(self, chicken):
                self.random_float = -self.random_float
                break