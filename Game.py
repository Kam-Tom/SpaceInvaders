import pygame, sys
from pygame.locals import *
from Pool import Pool
from factories import *
from Player.Player import Player
from Ships.Broiler import Broiler
from Player.Weapon.Missile import Missile
from GameInputHandler import GameInputHandler
import time
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
      self.last_shot_time = 0

      # Screen information
      SCREEN_WIDTH = 800
      SCREEN_HEIGHT = 600

      #set background
      self._DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
      self._DISPLAYSURF.fill(BLACK)
      pygame.display.set_caption("Space Invaders")

      self.game_objects = []
      self.pool = Pool()
      self.pool.register_category(Player.__name__,PlayerFactory(self.shoot),1)
      self.pool.register_category(Broiler.__name__,BroilerFactory(),10)
      self.pool.register_category(Missile.__name__,MissileFactory(self.destroy_object),100)
      self.player = self.pool.get_object("Player")
      self.player.enable(400, 550)
      self.input_handler = GameInputHandler(self.player)
   
   def destroy_object(self,obj):
      self.pool.return_object(obj.__class__.__name__,obj)
      self.game_objects.remove(obj)

   def shoot(self, pos:(int,int)):
      current_time = time.time()
      if current_time - self.last_shot_time >= 1:
         missile = self.pool.get_object("Missile")
         missile.enable(*pos, 1)
         self.game_objects.append(missile)
         self.last_shot_time = current_time

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
         if isinstance(obj, Broiler):
            obj.update(self.game_objects)
         else:
            obj.update()
      # self.player.move_missiles()
      for obj1 in self.game_objects:
         for obj2 in self.game_objects:
            if isinstance(obj1, Missile) and isinstance(obj2, Broiler) and obj1.rect.colliderect(obj2.rect):
               obj2.hit()
               self.destroy_object(obj1)
               if obj2.life <= 0:
                  self.destroy_object(obj2)
               break

   def render(self):
      self._DISPLAYSURF.fill(BLACK)
      for obj in self.game_objects:
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
