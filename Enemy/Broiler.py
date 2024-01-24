import pygame
import random
from Enemy.AIChicken import AIChicken
from Ships.ShipModel import ShipModelFactory
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, BORDER

# Klasa Broiler dziedziczy po klasie AIChicken
class Broiler(AIChicken):
    
    # Inicjalizacja klasy
    def __init__(self,ship_model_factory:ShipModelFactory, shoot_callback,drop_callback,disable_callback):
        super().__init__(shoot_callback,drop_callback,disable_callback)
        # Tworzenie modelu statku
        self.ship_model = ship_model_factory.get_ship_type((50,50),(0,2),"Broiler.jpg")
        # Ustalanie pozycji statku
        self.rect = self.ship_model.image.get_rect()
        self.rect.center=(0,0)

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

        # Aktualizacja pozycji statku
        self.pos = (self.pos[0] + self.ship_model.base_speed[0] * self.dir[0],self.pos[1] +self.ship_model.base_speed[1] * self.dir[1])

        self.rect.center = self.pos

        # Zmiana kierunku ruchu statku w zależności od jego pozycji
        if self.pos[0] >= SCREEN_WIDTH - BORDER:
            self.dir = (-1,1)
        if self.pos[0] <= BORDER:
            self.dir = (1,1)
        if self.pos[1] >= SCREEN_HEIGHT * 0.70:
            self.dir = (self.dir[0],-1)
        if self.pos[1] <= 25:
            self.dir = (self.dir[0],1)

        # Losowy strzał
        if random.random() < self.shoot_change:
            self.shoot()

    # Resetowanie ilości życia
    def hp_reset(self):
        self.life = 3
