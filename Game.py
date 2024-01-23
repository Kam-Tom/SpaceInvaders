import pygame, sys
import time, random
from pygame.locals import *
from Pool import Pool
from factories import *
from Player.Player import Player
from Enemy.Broiler import Broiler
from Projectile import Projectile
from ShootingStrategies.NormalShoot import NormalShoot
from ShootingStrategies.MultiShoot import MultiShoot
from ShootingStrategies.TripleShoot import TripleShoot
from GameInputHandler import GameInputHandler
from constants import *
from Menu import Menu
from Shop import Shop

class Game:
   def __init__(self):
      pygame.init()
      self._FPS = 60
      self._FramePerSec = pygame.time.Clock()
      self.menu = Menu(self)
      self.in_menu = True
      self.game_over = False
      self.shop = Shop(self)
      self.in_shop = False
      self.back_to_menu_rect = pygame.Rect(0, 0, 0, 0)
      self.retry_rect = pygame.Rect(0, 0, 0, 0)
      self.selected_option = 0

      #set background
      self._DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
      self._DISPLAYSURF.fill(BLACK)
      pygame.display.set_caption("Space Invaders")
      self.font = pygame.font.SysFont('comicsans', 20)
      self.game_over_font = pygame.font.SysFont('comicsans', 50)

      #set Object Pool
      self.game_objects = []
      self.pool = Pool()
      self.pool.register_category(Player.__name__,PlayerFactory(self.shoot,self.destroy_object,self.collect),1)
      self.pool.register_category(Broiler.__name__,BroilerFactory(self.enemy_shoot,self.destroy_object,self.drop),10)
      self.pool.register_category(Leghorn.__name__,LeghornFactory(self.enemy_shoot,self.destroy_object,self.drop),10)
      self.pool.register_category(Polish.__name__,PolishFactory(self.enemy_shoot,self.destroy_object,self.drop),10)

      self.pool.register_category(Projectile.__name__,ProjectileFactory(self.destroy_object),100)

      self.shoot_strategy = MultiShoot()
      self.player = self.pool.get_object("Player")
      #set Input handler
      self.input_handler = GameInputHandler(self.player)
      self.to_destroy = []

      self.level = 1
      self.coins = 0

   def start_game(self):   
      self.in_menu = False
      self.in_shop = False

   def enter_shop(self):
      self.in_menu = False
      self.in_shop = True

   def exit_shop(self):
      self.in_menu = False
      self.in_shop = False
      self.state = 'game'

   def collect(self):
      self.coins += 1

   def get_player_balance(self):
      return self.coins

   def deduct_balance(self, amount):
      if self.coins >= amount:
         self.coins -= amount
      else:
         print("Not enough money!")

   def add_balance(self, amount):
      self.coins += amount


   def start_next_level(self):
      self.level += 1
      self.generate_lvl()
      
   def destroy_object(self,obj):
      #queue object to destroy
      self.to_destroy.append(obj)

   def enemy_shoot(self, pos:(int,int)):
      egg = self.pool.get_object(Projectile.__name__)
      egg.set_type("egg",-5)
      egg.enable(*pos)
      self.game_objects.append(egg)

   def shoot(self, pos:(int,int)):
      missiles = self.shoot_strategy.shoot(self.pool,pos)

      self.game_objects.extend(missiles)
   
   def drop(self, pos:(int,int)):
      drop = self.pool.get_object(Projectile.__name__)
      drop.set_type("coin",-2)
      drop.enable(*pos)
      self.game_objects.append(drop)

   def generate_lvl(self):

      self.player.enable(800, 850)

      if self.player not in self.game_objects:
         self.game_objects.append(self.player)

      for i in range(100,1600,1600 - 100 * self.level): 
         ship = self.pool.get_object(Polish.__name__)
         ship.hp_reset()
         ship.enable(i + random.randint(10, 100),70)
         self.game_objects.append(ship)
      for i in range(100,1600,1000 - 200 * self.level):
         ship = self.pool.get_object(Leghorn.__name__)
         ship.hp_reset()
         ship.enable(i + random.randint(10, 100),120)
         self.game_objects.append(ship)

      for i in range(100,1600,1600 - 150 * self.level):
         ship = self.pool.get_object(Broiler.__name__)
         ship.hp_reset()
         ship.enable(i + random.randint(10, 100),random.randint(0, 600))
         self.game_objects.append(ship)


   def on_event(self, event):
      if event.type == QUIT:
         self.exit()

   def game_loop(self):
      #update
      for obj in self.game_objects:
         # if isinstance(obj, (Missile, Multiplier, Pierce)):
         #    obj.update(obj)
         # else:
            obj.update()

      if self.player.health <= 0:
         self.game_over = True
         self.selected_option = 0

      for i in range(len(self.game_objects)):
         for j in range(len(self.game_objects)):
            if self.game_objects[i] in self.to_destroy:
               continue
            self.game_objects[i].check_colision(self.game_objects[j])

      for obj in self.to_destroy:
         self.pool.return_object(obj.__class__.__name__,obj)
         if obj in self.game_objects:
            self.game_objects.remove(obj)
      
      self.to_destroy = []

      enemies = [obj for obj in self.game_objects if isinstance(obj, (Broiler, Leghorn, Polish))]
      if not enemies:
         if not hasattr(self, 'timer_started') or not self.timer_started:
            self.timer_started = True
            self.timer = pygame.time.get_ticks()

         if pygame.time.get_ticks() - self.timer > 1000:
            self.enter_shop()
            self.timer_started = False

      if self.player.health <= 0:
         self.game_over = True
         self.selected_option = 0

      #check check_colisions
      for i in range(len(self.game_objects)):
         for j in range(len(self.game_objects)):
            #skip destroyed objects
            if self.game_objects[i] in self.to_destroy:
               continue
            self.game_objects[i].check_colision(self.game_objects[j])

      #remove old objects
      for obj in self.to_destroy:
         self.pool.return_object(obj.__class__.__name__,obj)
         if obj in self.game_objects:
            self.game_objects.remove(obj)
      
      self.to_destroy = []
      
   def render(self):

      self._DISPLAYSURF.fill(BLACK)
      self._DISPLAYSURF.blit(self.font.render(f"Level: {self.level}", 1, (255,255,255)), (0, 0))
      self.player.draw_ammo_bar(self._DISPLAYSURF, self.font)
      self.player.draw_health_bar(self._DISPLAYSURF)
      self._DISPLAYSURF.blit(self.font.render(f"Coins: {self.coins}", 1, (255,255,255)), (0, 750))
      for obj in self.game_objects:
         obj.draw(self._DISPLAYSURF)
      
      if self.game_over:
         game_over_text = self.game_over_font.render("Game Over", 1, (255,255,255))
         retry_text = self.font.render("Retry", 1, (255,0,0) if self.selected_option == 0 else (255,255,255))
         back_to_menu_text = self.font.render("Back to menu", 1, (255,0,0) if self.selected_option == 1 else (255,255,255))
         game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
         self.retry_rect = retry_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50))
         self.back_to_menu_rect = back_to_menu_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 100))
         self._DISPLAYSURF.blit(game_over_text, game_over_rect)
         self._DISPLAYSURF.blit(retry_text, self.retry_rect)
         self._DISPLAYSURF.blit(back_to_menu_text, self.back_to_menu_rect)

   def exit(self):
      pygame.quit()
      sys.exit()
 
   def execute(self):
      self.angle = 0
      while(True):

         if self.in_menu:
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                  self.exit()
               self.menu.handle_event(event)

            self.menu.update()
            self.menu.draw(self._DISPLAYSURF)
         elif self.in_shop:
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                  self.exit()
               self.shop.handle_event(event)

            self.shop.draw(self._DISPLAYSURF)

         else:
            if self.game_over:
               for event in pygame.event.get():
                  if event.type == pygame.MOUSEBUTTONDOWN:
                     mouse_pos = pygame.mouse.get_pos()
                     if self.retry_rect.collidepoint(mouse_pos):
                        self.game_over = False
                        self.player.health = 5
                        self.game_objects = []
                        self.generate_lvl()
                        break
                     elif self.back_to_menu_rect.collidepoint(mouse_pos):
                        self.in_menu = True
                        self.game_over = False
                        self.player.health = 5
                        self.game_objects = []
                        break
                  elif event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % 2
                     elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % 2
                     elif event.key == pygame.K_RETURN:
                        if self.selected_option == 0:
                           self.game_over = False
                           self.player.health = 5
                           self.game_objects = []
                           self.generate_lvl()
                        elif self.selected_option == 1:
                           self.in_menu = True
                           self.game_over = False
                           self.player.health = 5
                           self.game_objects = []
                        break
               self.render()
               pygame.display.update()
               continue

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
