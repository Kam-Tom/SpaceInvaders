import pygame
from Player.Weapon.Decorator import Decorator

class Multiplier(Decorator):
    def __init__(self, component):
        super(Multiplier, self).__init__(component)
        self.multiplier = 5
        # Load images
        image1 = pygame.image.load("trail_1.png")
        image2 = pygame.image.load("trail_2.png")
        image3 = pygame.image.load("trail_3.png")

        # Create a list of images
        self.images = [image1, image2, image3]
        self.current_frame = 0
        self.timer = 0
    
    def draw(self, surface):
        # self.timer += 1
        # if self.timer > 60:
        #     self.timer = 0
        #     current_frame = (current_frame + 1) % len(self.image)

        surface.blit(self.ship_model.image, self.rect)

        super().draw(surface)

    def enable(self, x, y):
        self.component.size = (self.component.size[0] * self.multiplier, self.component.size[1] * self.multiplier)
        super().enable(x, y)

    def disable(self, obj):
        self.component.size = (self.component.rect.width / self.multiplier, self.component.rect.height / self.multiplier)
        super(Multiplier, self).disable(obj)
        # self.component.on_disable(self)
        # self.on_disable(self)
        # self.x = 0
        # self.y = 0

    def update(self, obj):
        super(Multiplier, self).update(obj)
        # if self.over_screen():
        #     self.disable(self)
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