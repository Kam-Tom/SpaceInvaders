import pygame
from abc import ABC, abstractmethod 

class Drawable(pygame.sprite.Sprite,ABC):
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def enable(self,x,y):
        pass

    @abstractmethod
    def disable(self):
        pass

    @abstractmethod
    def draw(self, surface):
        pass