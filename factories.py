import Ship
from Broiler import Broiler
from Polish import Polish
from Leghorn import Leghorn
from abc import ABC, abstractmethod 

class ShipFactory(ABC):
    @abstractmethod
    def create(self) -> Ship:
        pass

class BroilerFactory(ShipFactory):
    def create(self) -> Ship:
        return Broiler()
    
class LeghornFactory(ShipFactory):
    def create(self) -> Ship:
        return Leghorn()
    
class PolishFactory(ShipFactory):
    def create(self) -> Ship:
        return Polish()