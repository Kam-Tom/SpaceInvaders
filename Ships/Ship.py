from Drawable import Drawable

class Ship(Drawable):
    def __init__(self,shoot_callback):
        pass
        
    def draw(self, surface):
        surface.blit(self.ship_model.image, self.rect)

    def check_colision(self, obj):
        pass

