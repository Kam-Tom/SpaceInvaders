import pygame
from Player.Weapon.Decorator import Decorator

class Explosion(Decorator):
    def __init__(self, component):
        super(Explosion, self).__init__(component)
        self.image = pygame.image.load("Sprites/explosion.png")
        self.image = pygame.transform.scale(self.image, (64,64))
        self.flag = False
        self.x=0
        self.y=0
    
    def draw(self, surface):
        self.surface = surface
        if self.flag:
            surface.blit(self.image, (self.x, self.y))
        super(Explosion, self).draw(surface)

    def enable(self, x, y):
        # self.x = x
        # self.y = y
        # self.velocity = 5
        # self.rect.topleft = (x, y)
        self.x, self.y = x, y
        super(Explosion, self).enable(x, y)

    def disable(self, obj):
        # self.component.on_disable(self)
        self.flag = True
        super(Explosion, self).disable(obj)
        # self.on_disable(self)
        # self.x = 0
        # self.y = 0

    def update(self):
        if self.over_screen():
            self.disable(self)
        super(Explosion, self).update()
        # self.y -= self.velocity
        # self.rect.topleft = (self.x, self.y)
        # if self.over_screen():
        #     self.disable()

    def over_screen(self):
        return super(Explosion, self).over_screen()
    
    def check_colision(self, obj):
        pass

    def unpack(self):
        return self.component