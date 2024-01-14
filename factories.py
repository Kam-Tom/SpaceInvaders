from abc import ABC, abstractmethod 
from Drawable import Drawable
#Ships
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
        return Missile()