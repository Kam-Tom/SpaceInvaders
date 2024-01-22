import time
from Player.Weapon.Weapon import Weapon


class LoadedWeapon(Weapon):
    def __init__(self):
        super().__init__()

    def shoot(self):
        self.context.on_shoot((self.context.x-1,self.context.y - 40))
        self.context.ammo -= 1
        if self.context.ammo > 0:
            self.context.change_weapon_state(ShootingWeapon())
        else:
            self.context.change_weapon_state(UnloadedWeapon())

class UnloadedWeapon(Weapon):
    def __init__(self):
        super().__init__()
        self.current_time = time.time()

    def shoot(self):
        self.context.weapon_cooldown = 4 + self.current_time
        if time.time() >= self.context.weapon_cooldown:
            self.context.reload()
            self.context.change_weapon_state(LoadedWeapon())

class ShootingWeapon(Weapon):
    def __init__(self):
        super().__init__()
        self.current_time = time.time()

    def shoot(self):
        self.context.weapon_cooldown = 0.5 + self.current_time
        if time.time() >= self.context.weapon_cooldown:
            self.context.change_weapon_state(LoadedWeapon())