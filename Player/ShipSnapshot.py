class ShipSnapshot():
    def __init__(self,speed:float,max_ammo:int,max_health:int):
        self._speed = speed
        self._max_ammo = max_ammo
        self._max_health = max_health

    def get_speed(self) -> float:
        return self._speed

    def get_max_ammo(self) -> int:
        return self._max_ammo
    
    def get_max_health(self) -> int:
        return self._max_health

    def get_coins(self) -> int:
        return self._coins