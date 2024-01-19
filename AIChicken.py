import random
from Ship import Ship
from Missile import Missile

class AIChicken(Ship):
    def __init__(self, ship_model_factory):
        super().__init__(ship_model_factory)
        self.missiles = []

    def move(self):
        pass

    def shoot(self):
        missile = Missile((10, 10), "missile_red.png", self.on_missile_disable)
        missile.enable(self.x, self.y, -1)
        self.missiles.append(missile)

    def on_missile_disable(self, missile):
        self.missiles.remove(missile)

    def drop(self):
        pass

    def update(self):
        super().update()
        for missile in self.missiles:
            missile.update()
        if random.random() < 0.001:
            self.shoot()

    def draw(self, surface):
        super().draw(surface)
        for missile in self.missiles:
            missile.draw(surface)