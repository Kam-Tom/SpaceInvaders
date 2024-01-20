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
        #start from over screen
        self.rect.center=(SCREEN_WIDTH/2,-SCREEN_HEIGHT) 
        #set destination point
        self.destination = (x,y)
        self.pos = (SCREEN_WIDTH/2,-SCREEN_HEIGHT)
        self.x = x
        self.y = y

    def disable(self):
        #play 
        pass

    def update(self):
        
        self.rect.center=(self.x,self.y)

        if self.x >= SCREEN_WIDTH - BORDER:
            self.pos
        if self.x <= BORDER:
            self.x = 0
            self.y += 50
        if self.y >= 450:
            self.x = 0
            self.y = 70

    def check_colision(self,obj):
        pass
    
    
    
    
