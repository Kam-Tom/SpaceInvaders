from Ships.Ship import Ship
from Projectile import Projectile
from constants import SCREEN_HEIGHT,SCREEN_WIDTH,BORDER,MOVE_TO_START_SPEED
import pygame
import random

class AIChicken(Ship):
    def __init__(self,shoot_callback,drop_callback,disable_callback):
        super().__init__(shoot_callback,disable_callback)
        self.on_drop = drop_callback
        self.drop_chance = 0.5
        self.dir = (1,1)

    def shoot(self):
        self.on_shoot(self.pos)

    def drop(self):
        self.on_drop(self.pos)

    def draw(self, surface):
        super().draw(surface)
    
    def hit(self):
        self.drop()
    
    def check_colision(self, obj):
        if self.rect.colliderect(obj.rect) and isinstance(obj, Projectile) and obj.tag=="missile":
            obj.disable()
            self.hit()


    def enable(self,x,y):
        #start from over screen
        self.rect.center=(SCREEN_WIDTH/2,-SCREEN_HEIGHT) 
        #set destination point
        self.destination = (x,y)
        self.pos = (SCREEN_WIDTH/2,-SCREEN_HEIGHT)
        self.in_position = False


    def move_to_start(self):
        difference = pygame.math.Vector2(self.destination[0] - self.pos[0],self.destination[1] - self.pos[1])

        if abs(difference[0])+abs(difference[1]) < 50 :
            self.in_position = True
            return
        
        difference = pygame.math.Vector2.normalize(difference)
        difference = (difference[0] * MOVE_TO_START_SPEED, difference[1] * MOVE_TO_START_SPEED)
        self.pos = (self.pos[0]+difference[0],self.pos[1]+difference[1])
        self.rect.center = self.pos

    def update(self):
        
        if self.in_position == False:
            self.move_to_start()
            return

        self.pos = (self.pos[0] + self.ship_model.base_speed[0] * self.dir[0],self.pos[1] +self.ship_model.base_speed[1] * self.dir[1])

        self.rect.center = self.pos

        if self.pos[0] >= SCREEN_WIDTH - BORDER:
            self.dir = (-1,1)
        if self.pos[0] <= BORDER:
            self.dir = (1,1)
        if self.pos[1] >= SCREEN_HEIGHT * 0.70:
            self.dir = (self.dir[0],0)

    def disable(self):
        super().disable()
        if random.random() < self.drop_chance:
            self.drop()
