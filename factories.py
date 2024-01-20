from abc import ABC, abstractmethod 
from Drawable import Drawable
#Ships
from Player.Player import Player
from Ships.Broiler import Broiler
from Ships.Polish import Polish
from Ships.Leghorn import Leghorn
#Missile
from Player.Weapon.Missile import Missile

from Ships.ShipModel import ShipModelFactory

ship_model_factory = ShipModelFactory()

class DrawableFactory(ABC):
    @abstractmethod
    def create(self) -> Drawable:
        pass

class PlayerFactory(DrawableFactory):
    def __init__(self,on_shoot) -> None:
        self.on_shoot = on_shoot
    def create(self) -> Drawable:
        return Player(ship_model_factory,self.on_shoot)

class BroilerFactory(DrawableFactory):
    def __init__(self,on_shoot) -> None:
        self.on_shoot = on_shoot
    def create(self) -> Drawable:
        return Broiler(ship_model_factory, self.on_shoot)
    
class LeghornFactory(DrawableFactory):
    def __init__(self,on_disable) -> None:
        self.on_disable = on_disable
    def create(self) -> Drawable:
        return Leghorn(ship_model_factory,self.on_disable)
    
class PolishFactory(DrawableFactory):
    def create(self) -> Drawable:
        return Polish(ship_model_factory)
    
class MissileFactory(DrawableFactory):
    def __init__(self,on_disable) -> None:
        self.on_disable = on_disable
    def create(self) -> Drawable:
        return Missile((5, 10), "missile_blue.png",self.on_disable)
