import pygame
from Drawable import Drawable
from constants import SCREEN_HEIGHT

class Projectile(Drawable):
    def __init__(self,on_disable):
        self.on_disable = on_disable
        self.size = (16,20)

    # Enable the projectile with given x, y coordinates
    def enable(self, x, y):
        self.pos = (x,y)
        self.rect.center = (x, y)

    def set_type(self,tag:str,velocity:float):
        self.velocity = velocity
        self.tag = tag
        # Load and scale the image of the projectile
        self.image = pygame.image.load("Sprites/"+tag+".png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()

    def disable(self):
        self.on_disable(self)

    def draw(self, surface):
        surface.blit(self.image, self.pos)

    # Update the position of the projectile
    def update(self):
        self.pos = (self.pos[0], self.pos[1] - self.velocity)
        self.rect.center = self.pos
        if self.over_screen():
            self.disable()

    # Check if the projectile is over the screen
    def over_screen(self):
        return not (self.pos[1] > 0 and self.pos[1] < SCREEN_HEIGHT)
    
    def check_colision(self, obj):
        pass
