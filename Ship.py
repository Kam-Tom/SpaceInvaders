from Drawable import Drawable

class Ship(Drawable):
    def __init__(self):
        pass
        
    def draw(self, surface):
        surface.blit(self.ship_model.image, self.rect)

