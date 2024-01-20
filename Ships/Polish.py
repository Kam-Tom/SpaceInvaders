import pygame
import random

from Ships.AIChicken import AIChicken
from Ships.ShipModel import ShipModelFactory

from constants import SCREEN_HEIGHT,SCREEN_WIDTH,BORDER

class Polish(AIChicken):

    def __init__(self,ship_model_factory:ShipModelFactory):
        super().__init__(ship_model_factory)
        self.ship_model = ship_model_factory.get_ship_type((50,50),50,"Polish.jpg")
        self.rect = self.ship_model.image.get_rect()
        self.rect.center=(0,0) 
        self.dir = (1,1)
        self.init_hp = 1

    def enable(self,x,y):
        self.rect.center=(x, 0) 
        self.pos = (x, 0)
        self.x = x
        self.y = 0
        self.speed = 3
        self.direction = 1

    def disable(self):
        #play 
        pass

    def update(self):
        self.x += self.speed * self.direction
        self.y += self.speed * self.direction
        self.rect.center=(self.x,self.y)
        if self.y >= SCREEN_HEIGHT / 2 or self.y <= 0 or self.x >= SCREEN_WIDTH / 2 or self.x <= 0:
            self.direction *= -1

    def check_colision(self,obj):
        pass