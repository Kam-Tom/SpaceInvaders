from Drawable import Drawable
from factories import DrawableFactory

# SingletonMeta is a metaclass for creating singleton classes
class SingletonMeta(type):
    _instances = {}  # Dictionary to hold singleton instances

    def __call__(cls, *args, **kwargs):
        # If an instance for this class does not exist, create one
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        # Return the instance
        return cls._instances[cls]

# Pool is a singleton class for managing object pools
class Pool(metaclass=SingletonMeta):
    def __init__(self):
        self.pools = {}  # Dictionary to hold object pools
        self.factories = {}  # Dictionary to hold factories for creating objects
    
    # Register a category of objects with a factory and an initial size
    def register_category(self, category: str, factory: DrawableFactory, initial_size: int):
        self.pools[category] = []  # Create an empty pool for this category
        self.factories[category] = factory  # Store the factory for this category
        # Create initial objects for this category
        for i in range(initial_size):
            self.pools[category].append(self.factories[category].create())

    def get_object(self, category: str) -> Drawable:
        if category not in self.pools:
            raise ValueError(f"Category '{category}' not registered in the object pool.")
        
        # If the pool for this category is empty, create a new object
        if not self.pools[category]:
            return self.factories[category].create()
        else:
            return self.pools[category].pop()
        
    # Return an object to a category
    def return_object(self, category: str, obj: Drawable):
        if category not in self.pools:
            raise ValueError(f"Category '{category}' not registered in the object pool.")
        
        self.pools[category].append(obj)