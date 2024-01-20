import pygame
import random
from Enemy.AIChicken import AIChicken
from Ships.ShipModel import ShipModelFactory

from constants import SCREEN_HEIGHT,SCREEN_WIDTH,BORDER


class Leghorn(AIChicken):
    
    def __init__(self,ship_model_factory:ShipModelFactory, shoot_callback,drop_callback,disable_callback):
        super().__init__(shoot_callback,drop_callback,disable_callback)
        self.ship_model = ship_model_factory.get_ship_type((50,50),(0.1,0.01),"Leghorn.jpg")
        self.rect = self.ship_model.image.get_rect()

        self.rect.center=(0,0) 
        self.life = 3
        self.shoot_chance = 0.1

    def disable(self):
        self.on_disable(self)

    def enable(self, x, y):
        self.rect.center=(x,y) 
        self.x = x
        self.y = y
        self.direction = 1

    def update(self):
        if random.random() > self.shoot_chance:
            self.shoot()

        self.y += self.random_float
        self.rect.center=(self.x,self.y) 
        if self.y >= SCREEN_HEIGHT / 2 or self.y <= 0:
            self.direction *= -1


    def hit(self):
        self.life -= 1
        if self.life <= 0:
            self.disable()

    def hp_reset(self):
        self.life = 3

