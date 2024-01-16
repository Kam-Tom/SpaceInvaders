from abc import ABC, abstractmethod 
from Drawable import Drawable
#Ships
from Player import Player
from Broiler import Broiler
from Polish import Polish
from Leghorn import Leghorn
#Missile
from Missile import Missile

from ShipModel import ShipModelFactory

ship_model_factory = ShipModelFactory()

class DrawableFactory(ABC):
    @abstractmethod
    def create(self) -> Drawable:
        pass

class PlayerFactory(DrawableFactory):
    def create(self) -> Drawable:
        return Player(ship_model_factory)

class BroilerFactory(DrawableFactory):
    def create(self) -> Drawable:
        return Broiler(ship_model_factory)
    
class LeghornFactory(DrawableFactory):
    def create(self) -> Drawable:
        return Leghorn(ship_model_factory)
    
class PolishFactory(DrawableFactory):
    def create(self) -> Drawable:
        return Polish(ship_model_factory)
    
class MissileFactory(DrawableFactory):
    def create(self) -> Drawable:
        return Missile((5, 10), "missile_blue.png")
