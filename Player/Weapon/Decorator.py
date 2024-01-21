from Drawable import Drawable

class Decorator(Drawable):
    _component = None

    def __init__(self, component):
        self._component = component
        self.rect = self._component.rect

    @property
    def component(self):
        return self._component

    def enable(self, x, y):
        self._component.enable(x, y)
        # self.x = x
        # self.y = y
        # self.velocity = 5
        # self.rect.topleft = (x, y)

    def disable(self, obj):
        self._component.disable(obj)
        # self.on_disable(self)
        # self.x = 0
        # self.y = 0

    def draw(self, surface):
        self._component.draw(surface)

    def update(self):
        self.rect = self._component.rect
        self._component.update()
        # self.y -= self.velocity
        # self.rect.topleft = (self.x, self.y)
        # if self.over_screen():
        #     self.disable()

    def over_screen(self):
        return self._component.over_screen()
    
    def check_colision(self, obj):
        pass

     