from abc import ABC, abstractmethod 
from Drawable import Drawable
#Ships
from Player.Player import Player
from Enemy.Broiler import Broiler
from Enemy.Polish import Polish
from Enemy.Leghorn import Leghorn
#Missile
from Player.Weapon.Missile import Missile

from Ships.ShipModel import ShipModelFactory

ship_model_factory = ShipModelFactory()

class DrawableFactory(ABC):
    @abstractmethod
    def create(self) -> Drawable:
        pass

class PlayerFactory(DrawableFactory):
    def __init__(self,shoot_callback,disable_callback) -> None:
        self.on_shoot = shoot_callback
        self.on_disable = disable_callback
    def create(self) -> Drawable:
        return Player(ship_model_factory,self.on_shoot,self.on_disable)

class BroilerFactory(DrawableFactory):
    def __init__(self,shoot_callback,disable_callback,drop_callback) -> None:
        self.on_shoot = shoot_callback
        self.on_disable = disable_callback
        self.on_drop = drop_callback
    def create(self) -> Drawable:
        return Broiler(ship_model_factory, self.on_shoot,self.on_drop,self.on_disable)
    
class LeghornFactory(DrawableFactory):
    def __init__(self,shoot_callback,disable_callback,drop_callback) -> None:
        self.on_shoot = shoot_callback
        self.on_disable = disable_callback
        self.on_drop = drop_callback
    def create(self) -> Drawable:
        return Leghorn(ship_model_factory, self.on_shoot,self.on_drop,self.on_disable)
    
class PolishFactory(DrawableFactory):
    def __init__(self,shoot_callback,disable_callback,drop_callback) -> None:
        self.on_shoot = shoot_callback
        self.on_disable = disable_callback
        self.on_drop = drop_callback
    def create(self) -> Drawable:
        return Polish(ship_model_factory, self.on_shoot,self.on_drop,self.on_disable)
    
class MissileFactory(DrawableFactory):
    def __init__(self,disable_callback) -> None:
        self.on_disable = disable_callback
    def create(self) -> Drawable:
        return Missile((5, 10), "missile_blue.png",self.on_disable)
