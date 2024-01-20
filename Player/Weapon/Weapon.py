from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self):
        self.context = None

    def set_context(self, context):
        self.context = context

    @abstractmethod
    def shoot(self, direction):
        pass