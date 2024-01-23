import pygame
import random
import math
from Enemy.AIChicken import AIChicken
from Ships.ShipModel import ShipModelFactory
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, BORDER

# Klasa Leghorn dziedziczy po klasie AIChicken
class Leghorn(AIChicken):
    
    # Inicjalizacja klasy
    def __init__(self,ship_model_factory:ShipModelFactory, shoot_callback,drop_callback,disable_callback):
        super().__init__(shoot_callback,drop_callback,disable_callback)
        # Tworzenie modelu statku
        self.ship_model = ship_model_factory.get_ship_type((50,50),(1,1),"Leghorn.jpg")
        # Ustalanie pozycji statku
        self.rect = self.ship_model.image.get_rect()
        self.rect.center=(0,0)
        # Inicjalizacja kąta i prędkości obrotu
        self.angle = 0
        self.rotation_speed = 0.05
        # Inicjalizacja promienia
        self.radius = 5

        # Szansa na strzał
        self.shoot_change = 0.001

        # Ilość życia
        self.life = 3

        # Obrazy reprezentujące ilość życia
        self.hp_images = {
            3: pygame.transform.scale(pygame.image.load('Sprites/hp3on3.png'), (50, 10)),
            2: pygame.transform.scale(pygame.image.load('Sprites/hp2on3.png'), (50, 10)),
            1: pygame.transform.scale(pygame.image.load('Sprites/hp1on3.png'), (50, 10))
        }
        self.hp_image = self.hp_images[self.life]

    # Funkcja wywoływana po otrzymaniu obrażeń
    def hit(self):
        self.life -= 1
        if self.life <= 0:
            self.disable()
        else:
            self.hp_image = self.hp_images[self.life]
    
    # Funkcja wywoływana po aktywacji statku
    def enable(self, x, y):
        super().enable(x, y)
        self.life = 3
        self.hp_image = self.hp_images[self.life]

    # Rysowanie statku na ekranie
    def draw(self, screen):
        screen.blit(self.ship_model.image, self.rect)
        hp_rect = self.hp_image.get_rect()
        hp_rect.center = (self.rect.centerx, self.rect.centery - self.rect.height // 2 - hp_rect.height // 2)
        screen.blit(self.hp_image, hp_rect)

    # Aktualizacja stanu statku
    def update(self):
        if self.in_position == False:
            self.move_to_start()
            return

        # Aktualizacja kąta i pozycji statku
        self.angle += self.rotation_speed
        self.pos = (self.pos[0] + math.cos(self.angle) * self.radius, self.pos[1] + math.sin(self.angle) * self.radius)
        
        self.rect.center = self.pos

        # Losowy strzał
        if random.random() < self.shoot_change:
            self.shoot()
            
    # Resetowanie ilości życia
    def hp_reset(self):
        self.life = 3
