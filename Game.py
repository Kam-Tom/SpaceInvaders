import pygame, sys
from pygame.locals import *
from Pool import Pool
from factories import *
from Player import Player
from Polish import Polish
from Broiler import Broiler
from Leghorn import Leghorn
from Missile import Missile
from GameInputHandler import GameInputHandler
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
      self._DISPLAYSURF.fill(BLACK)
      pygame.display.set_caption("Space Invaders")

      self.game_objects = []
      self.pool = Pool()
      self.pool.register_category("Player",PlayerFactory(),1)
      self.pool.register_category("Broiler",BroilerFactory(),10)
      self.pool.register_category("Missile",MissileFactory(),100)
      self.player = self.pool.get_object("Player")
      self.player.enable(400, 550)
      self.player.set_pool(self.pool)
      self.input_handler = GameInputHandler(self.player)
      
 
   def genereate_lvl(self):
      self.game_objects.append(self.player)
      for i in range(0,900,50):
         ship = self.pool.get_object("Broiler")
         ship.enable(i,0)
         self.game_objects.append(ship)


   def on_event(self, event):
      if event.type == QUIT:
         self.exit()

   def game_loop(self):
      for obj in self.game_objects:
         obj.update()
      self.player.move_missiles()

   def render(self):
      self._DISPLAYSURF.fill(BLACK)
      for obj in self.game_objects:
         obj.draw(self._DISPLAYSURF)
      for obj in self.player.missiles:
         obj.draw(self._DISPLAYSURF)
      

   def exit(self):
      pygame.quit()
      sys.exit()
 
   def execute(self):
      self.genereate_lvl()
      while(True):

         for event in pygame.event.get():
            self.on_event(event)

         self.game_loop()
         self.render()

         pygame.display.update()

         self.input_handler.handle_input()

         self._FramePerSec.tick(self._FPS)


if __name__ == "__main__" :
    game = Game()
    game.execute()
