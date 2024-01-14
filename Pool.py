from Drawable import Drawable
from factories import ShipFactory

class Pool:
    def __init__(self):
        self.pools = {}
        self.factories = {}
    
    def register_category(self, category: str, factory: ShipFactory, initial_size: int):
        self.pools[category] = []
        self.factories[category] = factory
        for i in range(initial_size):
            self.pools[category].append(factory.create())

    def get_object(self, category: str) -> Drawable:
        if category not in self.pools:
            raise ValueError(f"Category '{category}' not registered in the object pool.")
        
        if not self.pools[category]:
            # If the pool is empty, create a new object
            return self.factories[category].create()
        else:
            # Otherwise, return an object from the pool
            return self.pools[category].pop()
        
    def return_object(self, category: str, obj: Drawable):
        # Return the object to the pool
        if category not in self.pools:
            raise ValueError(f"Category '{category}' not registered in the object pool.")
        
        self.pools[category].append(obj)