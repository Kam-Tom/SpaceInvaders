import pygame
import random

from Ships.AIChicken import AIChicken
from Ships.ShipModel import ShipModelFactory

from Player.Weapon.Missile import Missile
from Player.Weapon.WeaponStates import LoadedWeapon

from constants import SCREEN_HEIGHT,SCREEN_WIDTH,BORDER

class Broiler(AIChicken):
    
    def __init__(self,ship_model_factory:ShipModelFactory, on_shoot):
        super().__init__(ship_model_factory)
        self.ship_model = ship_model_factory.get_ship_type((50,50),50,"Broiler.jpg")
        self.rect = self.ship_model.image.get_rect()
        self.rect.center=(0,0)
        self.life = 3

        # self.on_shoot = on_shoot
        # self.ammo = 10
        # self.state = None
        # self.change_weapon_state(LoadedWeapon())

        self.hp_images = {
            3: pygame.transform.scale(pygame.image.load('Sprites/hp3on3.png'), (50, 10)),
            2: pygame.transform.scale(pygame.image.load('Sprites/hp2on3.png'), (50, 10)),
            1: pygame.transform.scale(pygame.image.load('Sprites/hp1on3.png'), (50, 10))
        }
        self.hp_image = self.hp_images[self.life]

    def hit(self):
        self.life -= 1
        if self.life <= 0:
            pass # self.disable()
        else:
            self.hp_image = self.hp_images[self.life]

    def hp_reset(self):
        self.life = 3
        self.hp_image = self.hp_images[self.life]

    # def shoot(self):
    #     self.state.shoot(-1)

    # def reload(self):
    #     self.ammo = 10

    # def change_weapon_state(self, state):
    #     self.state = state
    #     self.state.set_context(self)

    def draw(self, screen):
        screen.blit(self.ship_model.image, self.rect)
        hp_rect = self.hp_image.get_rect()
        hp_rect.center = (self.rect.centerx, self.rect.centery - self.rect.height // 2 - hp_rect.height // 2)
        screen.blit(self.hp_image, hp_rect)

    def disable(self):
        pass
    
    def enable(self, x, y):
        self.rect.center=(x, 0) 
        self.random_float = (2*random.random() - 1) + 0.1
        self.x = x
        self.y = y

    def update(self):
        super().update()
        self.x += self.random_float
        self.rect.center=(self.x,self.y) 
        if self.y >= SCREEN_HEIGHT / 2 or self.y <= 0:
            self.random_float = -abs(self.random_float)
