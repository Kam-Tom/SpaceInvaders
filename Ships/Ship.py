from Drawable import Drawable

class Ship(Drawable):
    def __init__(self,shoot_callback,disable_callback):
        self.on_shoot = shoot_callback
        self.on_disable = disable_callback
        
    def draw(self, surface):
        surface.blit(self.ship_model.image, self.rect)

    def disable(self):
        self.on_disable(self)

