import pygame
import time

from Ships.Ship import Ship
from Ships.ShipModel import ShipModelFactory
from Projectile import Projectile
from Player.Weapon.WeaponStates import LoadedWeapon

from constants import SCREEN_HEIGHT

class Player(Ship):
    def __init__(self,ship_model_factory:ShipModelFactory,shoot_callback,disable_callback,collect_callback):
        super().__init__(shoot_callback,disable_callback)

        self.width = 64
        self.height = 75
        self.ship_model = ship_model_factory.get_ship_type((self.width, self.height),(0.1,0),"spaceship.png")
        self.rect = self.ship_model.image.get_rect()
        self.rect.center=(0,0) 
        self.velocity = 5
        self.missiles = []
        self.on_shoot = shoot_callback
        self.on_collect = collect_callback
        self.ammo = 10
        self.weapon_cooldown = 0
        self.state = None
        self.change_weapon_state(LoadedWeapon())
        self.ammo_bar_piece = pygame.transform.scale(pygame.image.load('Sprites/ammo.png'), (10, 20))
        self.health = 5
        self.heart_image = pygame.transform.scale(pygame.image.load('Sprites/heart.png'), (50, 50))

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
        self.state.shoot()

    def reload(self):
        self.ammo = 10

    def change_weapon_state(self, state):
        self.state = state
        self.state.set_context(self)

    def draw_ammo_bar(self, screen, font):
        screen.blit(font.render(f"Cooldown: {max(round(self.weapon_cooldown - time.time(), 2), 0)}", 1, (255,255,255)), (0, SCREEN_HEIGHT - 30))
        for i in range(self.ammo):
            ammo_rect = self.ammo_bar_piece.get_rect()
            ammo_rect.bottomleft = (25 * i, 850)
            screen.blit(self.ammo_bar_piece, ammo_rect)

    def draw_health_bar(self, screen):
        for i in range(self.health):
            heart_rect = self.heart_image.get_rect()
            heart_rect.topleft = (50 * i, 775)
            screen.blit(self.heart_image, heart_rect)

    def save(self):
        pass

    def restore(self):
        pass

    def check_colision(self, obj):
        if self.rect.colliderect(obj.rect) and isinstance(obj, Projectile) and obj.tag=="egg":
            obj.disable()
            self.health -= 1
        if self.rect.colliderect(obj.rect) and isinstance(obj, Projectile) and obj.tag=="coin":
            self.on_collect()
            obj.disable()
