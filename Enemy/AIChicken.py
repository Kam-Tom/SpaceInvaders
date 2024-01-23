from Ships.Ship import Ship
from Projectile import Projectile
from constants import SCREEN_HEIGHT,SCREEN_WIDTH,BORDER,MOVE_TO_START_SPEED
import pygame
import random

# Klasa AIChicken dziedziczy po klasie Ship
class AIChicken(Ship):
    # Konstruktor klasy AIChicken
    def __init__(self,shoot_callback,drop_callback,disable_callback):
        # Wywołanie konstruktora klasy nadrzędnej
        super().__init__(shoot_callback,disable_callback)
        # Przypisanie funkcji callback do zdarzenia drop
        self.on_drop = drop_callback
        # Szansa na zdarzenie drop
        self.drop_chance = 1
        # Kierunek ruchu statku
        self.dir = (1,1)

    # Metoda wywołująca zdarzenie strzału
    def shoot(self):
        self.on_shoot(self.pos)

    # Metoda wywoływana gdy statek ma zrzucić przedmiot
    def drop(self):
        self.on_drop(self.pos)

    # Metoda rysująca statek na ekranie
    def draw(self, surface):
        super().draw(surface)
    
    def hit(self):
        pass
    
    # Metoda sprawdzająca kolizję statku z innym obiektem
    def check_colision(self, obj):
        if self.rect.colliderect(obj.rect) and isinstance(obj, Projectile) and obj.tag=="missile":
            obj.disable()
            self.hit()

    # Metoda umożliwiająca aktywację statku
    def enable(self,x,y):
        # Ustawienie początkowej pozycji statku
        self.rect.center=(SCREEN_WIDTH/2,-SCREEN_HEIGHT) 
        # Ustawienie punktu docelowego
        self.destination = (x,y)
        self.pos = (SCREEN_WIDTH/2,-SCREEN_HEIGHT)
        self.in_position = False

    # Metoda umożliwiająca ruch statku do punktu startowego
    def move_to_start(self):
        difference = pygame.math.Vector2(self.destination[0] - self.pos[0],self.destination[1] - self.pos[1])

        if abs(difference[0])+abs(difference[1]) < 50 :
            self.in_position = True
            return
        
        difference = pygame.math.Vector2.normalize(difference)
        difference = (difference[0] * MOVE_TO_START_SPEED, difference[1] * MOVE_TO_START_SPEED)
        self.pos = (self.pos[0]+difference[0],self.pos[1]+difference[1])
        self.rect.center = self.pos

    # Metoda aktualizująca pozycję statku na ekranie
    def update(self):
        
        # Jeśli statek nie jest na pozycji startowej, to najpierw go tam przesuń
        if self.in_position == False:
            self.move_to_start()
            return

        # Przesuń statek w kierunku zadanym przez dir o wartość prędkości
        self.pos = (self.pos[0] + self.ship_model.base_speed[0] * self.dir[0],self.pos[1] +self.ship_model.base_speed[1] * self.dir[1])

        self.rect.center = self.pos

        # Jeśli statek dotrze do krawędzi ekranu, to zmień kierunek
        if self.pos[0] >= SCREEN_WIDTH - BORDER:
            self.dir = (-1,1)
        if self.pos[0] <= BORDER:
            self.dir = (1,1)
        if self.pos[1] >= SCREEN_HEIGHT * 0.70:
            self.dir = (self.dir[0],0)

    # Metoda wywoływana gdy statek zostanie zniszczony
    def disable(self):
        super().disable()
        if random.random() < self.drop_chance:
            self.drop()
