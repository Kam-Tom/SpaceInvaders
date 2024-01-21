import pygame, sys
import time

from pygame.locals import *
from Pool import Pool
from factories import *
from Player.Player import Player
from Enemy.Broiler import Broiler
from Enemy.Egg import Egg
from Player.Weapon.Missile import Missile
from GameInputHandler import GameInputHandler
from constants import *
from Menu import Menu


class Game:
   def __init__(self):
      pygame.init()
      self._FPS = 60
      self._FramePerSec = pygame.time.Clock()
      self.menu = Menu(self)
      self.in_menu = True

      #set background
      self._DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
      self._DISPLAYSURF.fill(BLACK)
      pygame.display.set_caption("Space Invaders")
      self.font = pygame.font.SysFont('comicsans', 20)

      #set Object Pool
      self.game_objects = []
      self.pool = Pool()
      self.pool.register_category(Player.__name__,PlayerFactory(self.shoot,self.destroy_object,self.collect),1)
      self.pool.register_category(Broiler.__name__,BroilerFactory(self.enemy_shoot,self.destroy_object,self.drop),10)
      self.pool.register_category(Leghorn.__name__,LeghornFactory(self.enemy_shoot,self.destroy_object,self.drop),10)
      self.pool.register_category(Polish.__name__,PolishFactory(self.enemy_shoot,self.destroy_object,self.drop),10)
      self.pool.register_category(Missile.__name__,MissileFactory(self.destroy_object),100)
      self.pool.register_category(Egg.__name__,EggFactory(self.destroy_object),100)
      self.pool.register_category(Drop.__name__,DropFactory(self.destroy_object),100)
      
      self.player = self.pool.get_object("Player")
      #set Input handler
      self.input_handler = GameInputHandler(self.player)
      self.to_destroy = []

      self.level = 1

   def start_game(self):
      self.in_menu = False

   def collect(self):
      print("Money +1")
   
   def destroy_object(self,obj):
      #queue object
      self.to_destroy.append(obj)

   def enemy_shoot(self, pos:(int,int)):
      egg = self.pool.get_object(Egg.__name__)
      egg.enable(*pos)
      self.game_objects.append(egg)

   def shoot(self, pos:(int,int)):
      missile = self.pool.get_object("Missile")
      missile.enable(*pos)
      self.game_objects.append(missile)
   
   def drop(self, pos:(int,int)):
      drop = self.pool.get_object(Drop.__name__)
      drop.enable(*pos)
      self.game_objects.append(drop)

   def generate_lvl(self):

      self.player.enable(800, 850)

      self.game_objects.append(self.player)

      for i in range(0,800,300): 
         ship = self.pool.get_object(Polish.__name__)
         ship.hp_reset()
         ship.enable(i,70)
         self.game_objects.append(ship)
      for i in range(100,800,100):
         ship = self.pool.get_object(Leghorn.__name__)
         ship.hp_reset()
         ship.enable(i,120)
         self.game_objects.append(ship)

      for i in range(100,600,300):
         ship = self.pool.get_object(Broiler.__name__)
         ship.enable(i,i + 20)
         ship.hp_reset()
         self.game_objects.append(ship)


   def on_event(self, event):
      if event.type == QUIT:
         self.exit()

   def game_loop(self):
      #update
      for obj in self.game_objects:
         obj.update()

      #check check_colisions
      for i in range(len(self.game_objects)):
         for j in range(i+1,len(self.game_objects)):
            #skip destroyed objects
            if self.game_objects[i] in self.to_destroy:
               continue
            self.game_objects[i].check_colision(self.game_objects[j])

      #remove old objects
      for obj in self.to_destroy:
         self.pool.return_object(obj.__class__.__name__,obj)
         self.game_objects.remove(obj)
      
      self.to_destroy = []
      
   def render(self):
      self._DISPLAYSURF.fill(BLACK)
      self._DISPLAYSURF.blit(self.font.render(f"Level: {self.level}", 1, (255,255,255)), (10, 0))
      self.player.draw_ammo_bar(self._DISPLAYSURF)
      for obj in self.game_objects:
         obj.draw(self._DISPLAYSURF)

      

   def exit(self):
      pygame.quit()
      sys.exit()
 
   def execute(self):
      while(True):
         if self.in_menu:
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                  self.exit()
               self.menu.handle_event(event)

            self.menu.update()
            self.menu.draw(self._DISPLAYSURF)
         else:
            if len(self.game_objects) <= 1:
               self.generate_lvl()

            for event in pygame.event.get():
               self.on_event(event)

            self.game_loop()
            self.render()
            self.input_handler.handle_input()

         pygame.display.update()
         self._FramePerSec.tick(self._FPS)


if __name__ == "__main__" :
    game = Game()
    game.execute()
