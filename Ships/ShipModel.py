import pygame

class ShipModel():
    def __init__(self,size:(int,int),base_speed:float,image_path:str):
        self.size = size
        self.base_speed = base_speed
        self.image = pygame.image.load("Sprites/"+image_path)
        self.image = pygame.transform.scale(self.image, size)

class ShipModelFactory():
    def __init__(self):
        self.ship_models = {}

    def get_ship_type(self,size:(int,int),base_speed:float,img_path:str):
        model_key = (size, base_speed,img_path)
        if model_key not in self.ship_models:
            self.ship_models[model_key] = ShipModel(size, base_speed,img_path)
        return self.ship_models[model_key]
    