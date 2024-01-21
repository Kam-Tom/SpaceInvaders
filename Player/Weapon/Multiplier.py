import pygame
from Player.Weapon.Decorator import Decorator

class Multiplier(Decorator):
    def __init__(self, component):
        super(Multiplier, self).__init__(component)
        self.multiplier = 5
    
    def draw(self, surface):
        super(Multiplier, self).draw(surface)

    def enable(self, x, y):
        # self.x = x
        # self.y = y
        # self.velocity = 5
        # self.rect.topleft = (x, y)
        self.component.size = (self.component.size[0] * self.multiplier, self.component.size[1] * self.multiplier)
        super(Multiplier, self).enable(x, y)

    def disable(self, obj):
        self.component.size = (self.component.size[0] / self.multiplier, self.component.size[1] / self.multiplier)
        # self.component.on_disable(self)
        super(Multiplier, self).disable(obj)
        # self.on_disable(self)
        # self.x = 0
        # self.y = 0

    def update(self):
        if self.over_screen():
            self.disable(self)
        super(Multiplier, self).update()
        # self.y -= self.velocity
        # self.rect.topleft = (self.x, self.y)
        # if self.over_screen():
        #     self.disable()

    def over_screen(self):
        return super(Multiplier, self).over_screen()
    
    def check_colision(self, obj):
        pass

    def unpack(self):
        return self.component