import pygame
from Player.Weapon.Decorator import Decorator
from Enemy.AIChicken import AIChicken

class Pierce(Decorator):
    def __init__(self, component):
        super(Pierce, self).__init__(component)
        self.image = pygame.image.load("Sprites/missile_pierce.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        super(Pierce, self).draw(surface)

    def enable(self, x, y):
        super(Pierce, self).enable(x, y)
        # self.x = x
        # self.y = y
        # self.velocity = 5
        # self.rect.topleft = (x, y)

    def disable(self, obj):
        super(Pierce, self).disable(obj)
        # self.component.on_disable(self)
        # self.on_disable(self)
        # self.x = 0
        # self.y = 0

    def update(self, obj):
        super(Pierce, self).update(obj)
        # if self.over_screen():
        #     self.disable(self)
        # self.y -= self.velocity
        # self.rect.topleft = (self.x, self.y)
        # if self.over_screen():
        #     self.disable()

    def over_screen(self):
        return super(Pierce, self).over_screen()
    
    def check_colision(self, obj):
        if self.rect.colliderect(obj.rect) and (isinstance(obj, (AIChicken))):
            obj.hit()

    def unpack(self):
        return self.component