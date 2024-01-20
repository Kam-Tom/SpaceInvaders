import pygame
import random
import math
from Enemy.AIChicken import AIChicken
from Ships.ShipModel import ShipModelFactory

class Polish(AIChicken):

    def __init__(self,ship_model_factory:ShipModelFactory, shoot_callback,drop_callback,disable_callback):
        super().__init__(shoot_callback,drop_callback,disable_callback)

        self.ship_model = ship_model_factory.get_ship_type((50,50),(2,0.1),"Polish.jpg")
        self.rect = self.ship_model.image.get_rect()
        self.rect.center=(0,0) 
        self.dir = (1,1)
        self.shoot_change = 0.01

        self.shoot_change = 0.01

        self.life = 3

        self.hp_images = {
            3: pygame.transform.scale(pygame.image.load('Sprites/hp3on3.png'), (50, 10)),
            2: pygame.transform.scale(pygame.image.load('Sprites/hp2on3.png'), (50, 10)),
            1: pygame.transform.scale(pygame.image.load('Sprites/hp1on3.png'), (50, 10))
        }
        self.hp_image = self.hp_images[self.life]

    def hit(self):
        self.life -= 1
        if self.life <= 0:
            self.disable()
        else:
            self.hp_image = self.hp_images[self.life]
    
    def enable(self, x, y):
        super().enable(x, y)
        self.life = 3
        self.hp_image = self.hp_images[self.life]


    def draw(self, screen):
        screen.blit(self.ship_model.image, self.rect)
        hp_rect = self.hp_image.get_rect()
        hp_rect.center = (self.rect.centerx, self.rect.centery - self.rect.height // 2 - hp_rect.height // 2)
        screen.blit(self.hp_image, hp_rect)

    def update(self):
        super().update()
        if self.in_position == False:
            return
        if random.random() < self.shoot_change:
            self.shoot()
            
    def hp_reset(self):
        self.life = 3
        

    
    
    
    
