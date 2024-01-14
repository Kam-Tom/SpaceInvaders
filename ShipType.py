import pygame

class ShipType():
    def __init__(self,size:(int,int),base_speed:float,image_path:str):
        self.size = size
        self.base_speed = base_speed
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)

class ShipTypeFactory():
    def __init__(self):
        self.ship_types = {}

    def get_ship_type(self,size:(int,int),base_speed:float,img_path:str):
        ship_type = ShipType(size, base_speed,img_path)
        if ship_type not in self.ship_types:
            self.ship_types[ship_type] = ship_type
        return self.ship_types[ship_type]
    