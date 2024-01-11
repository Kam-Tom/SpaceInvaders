import pygame, sys
from pygame.locals import *
from Broiler import Broiler
# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Game:
   def __init__(self):
      pygame.init()
      self._FPS = 60
      self._FramePerSec = pygame.time.Clock()

      # Screen information
      SCREEN_WIDTH = 800
      SCREEN_HEIGHT = 600

      #set background
      self._DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
      self._DISPLAYSURF.fill(WHITE)
      pygame.display.set_caption("Space Invaders")
      
 
 
   def on_event(self, event):
      if event.type == QUIT:
         self.exit()

   def game_loop(self):
      pass

   def render(self):
      self.vaporeon.draw(self._DISPLAYSURF)
      

   def exit(self):
      pygame.quit()
      sys.exit()
 
   def execute(self):
      self.vaporeon = Broiler()
      while(True):

         for event in pygame.event.get():
            self.on_event(event)

         self.game_loop()
         self.render()

         pygame.display.update()
         self._FramePerSec.tick(self._FPS)


if __name__ == "__main__" :
    game = Game()
    game.execute()