from abc import ABC, abstractmethod

class ShootStrategy(ABC):
    @abstractmethod
    def shoot(self,pool,pos):
        pass
