import pygame
import random
from Ships.AIChicken import AIChicken
from Ships.ShipModel import ShipModelFactory


class Leghorn(AIChicken):
    
    def __init__(self,ship_model_factory:ShipModelFactory, on_disable):
        super().__init__(ship_model_factory)
        self.ship_model = ship_model_factory.get_ship_type((50,50),50,"Leghorn.jpg")
        self.rect = self.ship_model.image.get_rect()
        self.on_disable = on_disable
        self.rect.center=(0,0) 
        self.life = 3

    def disable(self):
        self.on_disable(self)

    def enable(self, x, y):
        self.rect.center=(x,y) 
        self.random_float = abs(2*random.random() - 1)
        self.x = x
        self.y = y

    def update(self, chickens):
        self.y += self.random_float
        self.rect.center=(self.x,self.y) 
        if self.x > 825:
            self.x = -25
        if self.y > 625:
            self.disable()
        if self.x < -25:
            self.x = 825
        if self.y < 0:
            self.random_float = abs(self.random_float)
        for chicken in chickens:
            if self != chicken and pygame.sprite.collide_rect(self, chicken):
                self.random_float = -self.random_float
                break

    def hit(self):
        self.life -= 1
        if self.life <= 0:
            pass
            # self.disable()

    def hp_reset(self):
        self.life = 3

