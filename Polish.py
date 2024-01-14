import pygame
from AIChicken import AIChicken
from ShipModel import ShipModelFactory


class Polish(AIChicken):

    def __init__(self,ship_model_factory:ShipModelFactory):
        self.ship_model = ship_model_factory.get_ship_type((50,50),50,"vaporeon.jpg")
        self.rect = self.ship_model.image.get_rect()
        self.rect.center=(0,0) 

    def update(self):
        self.rect.center=(self.x,self.y)
        self.y -= 1

    def disable(self):
        pass
    
    def enable(self,x,y):
        self.rect.center=(x,y) 
        self.x = x
        self.y = y
    
    
