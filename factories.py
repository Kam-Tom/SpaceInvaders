from abc import ABC, abstractmethod 
from Drawable import Drawable
#Ships
from Broiler import Broiler
from Polish import Polish
from Leghorn import Leghorn
#Missile
from Missile import Missile


class DrawableFactory(ABC):
    @abstractmethod
    def create(self) -> Drawable:
        pass

class BroilerFactory(DrawableFactory):
    def create(self) -> Drawable:
        return Broiler()
    
class LeghornFactory(DrawableFactory):
    def create(self) -> Drawable:
        return Leghorn()
    
class PolishFactory(DrawableFactory):
    def create(self) -> Drawable:
        return Polish()
    
class MissileFactory(DrawableFactory):
    def create(self) -> Drawable:
        return Missile()