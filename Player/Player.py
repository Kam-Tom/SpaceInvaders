import pygame
from Ships.Ship import Ship
from Ships.ShipModel import ShipModelFactory
from Player.Weapon.Missile import Missile
from Player.Weapon.WeaponStates import LoadedWeapon
from Enemy.Egg import Egg

class Player(Ship):
    def __init__(self,ship_model_factory:ShipModelFactory,shoot_callback,disable_callback):
        super().__init__(shoot_callback,disable_callback)

        self.width = 64
        self.height = 75
        self.ship_model = ship_model_factory.get_ship_type((self.width, self.height),(0.1,0),"spaceship.png")
        self.rect = self.ship_model.image.get_rect()
        self.rect.center=(0,0) 
        self.velocity = 5
        self.missiles = []
        self.on_shoot = shoot_callback
        self.ammo = 10
        self.state = None
        self.change_weapon_state(LoadedWeapon())
        self.ammo_bar_piece = pygame.transform.scale(pygame.image.load('Sprites/ammo.png'), (10, 20))

    def enable(self, x, y):
        self.rect.center=(x,y) 
        self.x = x
        self.y = y

    def disable(self):
        pass

    def update(self):
        pass

    def moveLeft(self):
        if self.x > self.width // 2:
            self.x -= self.velocity
            self.rect.center=(self.x,self.y) 

    def moveRight(self):
        if self.x < 1600 - self.width // 2:
            self.x += self.velocity
            self.rect.center=(self.x,self.y) 

    def shoot(self):
        # self.on_shoot((self.x-1,self.y-40), 1)
        self.state.shoot(1)

    def reload(self):
        self.ammo = 10

    def change_weapon_state(self, state):
        self.state = state
        self.state.set_context(self)

    def draw_ammo_bar(self, screen):
        for i in range(self.ammo):
            ammo_rect = self.ammo_bar_piece.get_rect()
            ammo_rect.bottomleft = (25 * i, 900)
            screen.blit(self.ammo_bar_piece, ammo_rect)

    def save(self):
        pass

    def restore(self):
        pass

    def check_colision(self, obj):
        if self.rect.colliderect(obj.rect) and isinstance(obj,Egg):
            obj.disable()
