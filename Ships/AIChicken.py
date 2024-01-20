import random
from Ships.Ship import Ship
from Player.Weapon.Missile import Missile
from Player.Weapon.WeaponStates import LoadedWeapon

class AIChicken(Ship):
    def __init__(self, ship_model_factory):
        super().__init__(ship_model_factory)
        self.ammo = 10
        self.missiles = []
        self.state = None
        self.change_weapon_state(LoadedWeapon())

    def move(self):
        pass

    def shoot(self):
        missile = Missile((10, 10), "missile_red.png", self.on_missile_disable)
        missile.enable(self.x, self.y, -1)
        self.missiles.append(missile)
        self.ammo -= 1
        # self.state.shoot()

    def reload(self):
        self.ammo = 10

    def change_weapon_state(self, state):
        self.state = state
        self.state.set_context(self)

    def on_missile_disable(self, missile):
        self.missiles.remove(missile)

    def drop(self):
        pass

    def update(self):
        super().update()
        for missile in self.missiles:
            missile.update()
        self.shoot()

    def draw(self, surface):
        super().draw(surface)
        for missile in self.missiles:
            missile.draw(surface)