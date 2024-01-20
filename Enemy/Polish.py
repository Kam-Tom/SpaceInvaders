import pygame
import random

from Enemy.AIChicken import AIChicken
from Ships.ShipModel import ShipModelFactory

class Polish(AIChicken):

    def __init__(self,ship_model_factory:ShipModelFactory, shoot_callback,drop_callback,disable_callback):
        super().__init__(shoot_callback,drop_callback,disable_callback)

        self.ship_model = ship_model_factory.get_ship_type((50,50),(2,0.1),"Polish.jpg")
        self.rect = self.ship_model.image.get_rect()
        self.rect.center=(0,0) 
        self.dir = (1,1)


    # def enable(self,x,y):
    #     #start from over screen
    #     self.rect.center=(SCREEN_WIDTH/2,-SCREEN_HEIGHT) 
    #     #set destination point
    #     self.destination = (x,y)
    #     self.pos = (SCREEN_WIDTH/2,-SCREEN_HEIGHT)
    #     self.in_position = False


    # def move_to_start(self):
    #     difference = pygame.math.Vector2(self.destination[0] - self.pos[0],self.destination[1] - self.pos[1])

    #     if abs(difference[0])+abs(difference[1]) < 50 :
    #         self.in_position = True
    #         return
        
    #     difference = pygame.math.Vector2.normalize(difference)
    #     difference = (difference[0] * MOVE_TO_START_SPEED, difference[1] * MOVE_TO_START_SPEED)
    #     self.pos = (self.pos[0]+difference[0],self.pos[1]+difference[1])
    #     self.rect.center = self.pos

    # def update(self):
        
    #     if self.in_position == False:
    #         self.move_to_start()
    #         return

    #     self.pos = (self.pos[0] + self.ship_model.base_speed[0] * self.dir[0],self.pos[1] +self.ship_model.base_speed[1] * self.dir[1])

    #     self.rect.center = self.pos

    #     if self.pos[0] >= SCREEN_WIDTH - BORDER:
    #         self.dir = (-1,1)
    #     if self.pos[0] <= BORDER:
    #         self.dir = (1,1)
    #     if self.pos[1] >= SCREEN_HEIGHT * 0.70:
    #         self.dir = (self.dir[0],0)

        

    
    
    
    
