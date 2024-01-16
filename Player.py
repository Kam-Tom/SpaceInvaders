from Ship import Ship
from ShipModel import ShipModelFactory

class Player(Ship):
    def __init__(self,ship_model_factory:ShipModelFactory):
        self.width = 64
        self.height = 75
        self.ship_model = ship_model_factory.get_ship_type((self.width, self.height),50,"spaceship.png")
        self.rect = self.ship_model.image.get_rect()
        self.rect.center=(0,0) 
        self.velocity = 5

    def enable(self, x, y):
        self.rect.center=(x,y) 
        self.x = x
        self.y = y
    def disable(self):
        pass
    def update(self):
        pass
    def moveLeft(self):
        if self.x > self.width // 2:
            self.x -= self.velocity
            self.rect.center=(self.x,self.y) 
    def moveRight(self):
        if self.x < 800 - self.width // 2:
            self.x += self.velocity
            self.rect.center=(self.x,self.y) 
    def shoot(self):
        pass
    def save(self):
        pass
    def restore(self):
        pass
