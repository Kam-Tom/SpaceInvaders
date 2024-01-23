from Drawable import Drawable
from factories import DrawableFactory

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Pool(metaclass=SingletonMeta):
    def __init__(self):
        self.pools = {}
        self.factories = {}
    
    def register_category(self, category: str, factory: DrawableFactory, initial_size: int):
        self.pools[category] = []
        self.factories[category] = factory
        for i in range(initial_size):
            self.pools[category].append(self.factories[category].create())

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