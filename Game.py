import pygame, sys
import time, random
from pygame.locals import *
from Pool import Pool
from factories import *
from Player.Player import Player
from Enemy.Broiler import Broiler
from Projectile import Projectile
from ShootingStrategies.BigShoot import BigShoot
from ShootingStrategies.DoubleShoot import DoubleShoot
from ShootingStrategies.TripleShoot import TripleShoot
from GameInputHandler import GameInputHandler
from constants import *
from Menu import Menu
from Shop import Shop

class Game:
   def __init__(self):
      #initial setup
      pygame.init()
      self._FPS = 60
      self._FramePerSec = pygame.time.Clock()

      #game veriables
      self.level = 1
      self.coins = 0

      #set background
      self.setup_background()

      #set Object Pool
      self.setup_pool()

      #start with default shooting strategy
      self.shoot_strategy = BigShoot()

      #setup player
      self.player = self.pool.get_object("Player")

      #setup shop and main menu screen
      self.setup_menus()

      #set Input handler
      self.input_handler = GameInputHandler(self.player)

      #list to queue object to destroy
      self.to_destroy = []


   def setup_pool(self):
      self.game_objects = []
      self.pool = Pool()
      self.pool.register_category(Player.__name__,PlayerFactory(self.shoot,self.destroy_player,self.collect),1)
      self.pool.register_category(Broiler.__name__,BroilerFactory(self.enemy_shoot,self.destroy_object,self.drop),10)
      self.pool.register_category(Leghorn.__name__,LeghornFactory(self.enemy_shoot,self.destroy_object,self.drop),10)
      self.pool.register_category(Polish.__name__,PolishFactory(self.enemy_shoot,self.destroy_object,self.drop),10)
      self.pool.register_category(Projectile.__name__,ProjectileFactory(self.destroy_object),100)
   
   def setup_menus(self):
      self.menu = Menu(self)
      self.in_menu = True
      self.game_over = False
      self.shop = Shop(self)
      self.in_shop = False
      self.back_to_menu_rect = pygame.Rect(0, 0, 0, 0)
      self.retry_rect = pygame.Rect(0, 0, 0, 0)
      self.selected_option = 0

   def setup_background(self):
      self._DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
      self._DISPLAYSURF.fill(BLACK)
      pygame.display.set_caption("Space Invaders")
      self.font = pygame.font.SysFont('comicsans', 20)
      self.game_over_font = pygame.font.SysFont('comicsans', 50)
   

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

   def collect(self,drop_type):
      #change shooting type based on collected bonus
      if drop_type == "big_shoot":
         self.shoot_strategy = BigShoot()
      elif drop_type == "double_shoot":
         self.shoot_strategy = DoubleShoot()
      elif drop_type == "triple_shoot":
         self.shoot_strategy = TripleShoot()
      #if collected coin, add coin
      elif drop_type == "coin":
         self.coins += 1
      else:
         print("Wrong Drop Type")

   def start_next_level(self):
      self.state = 'shop'
      self.level += 1
      self.generate_lvl()
      
   def destroy_object(self,obj):
      #queue object to destroy
      self.to_destroy.append(obj)

   def destroy_player(self,obj):
      self.game_over = True
      self.selected_option = 0

   def enemy_shoot(self, pos:(int,int)):
      egg = self.pool.get_object(Projectile.__name__)
      egg.size = (16,16)
      egg.set_type("egg",-5)
      egg.enable(*pos)
      self.game_objects.append(egg)

   def shoot(self, pos:(int,int)):
      missiles = self.shoot_strategy.shoot(self.pool,pos)
      self.game_objects.extend(missiles)     
   
   def drop(self, pos:(int,int)):
      drop = self.pool.get_object(Projectile.__name__)
      item = random.choices(["coin","big_shoot","double_shoot","triple_shoot"], [0.50,0.30,0.15,0.05])[0]
      drop.size = (16,16)
      drop.set_type(item,-2)
      drop.enable(*pos)
      self.game_objects.append(drop)

   def generate_lvl(self):

      self.player.enable(SCREEN_WIDTH/2, SCREEN_HEIGHT-BORDER*4)
      self.player.reset_hp()
      self.player.reset_ammo()

      if self.player not in self.game_objects:
         self.game_objects.append(self.player)

      for i in range(0, self.level * 2): 
         ship = self.pool.get_object(Polish.__name__)
         ship.hp_reset()
         ship.enable(random.randint(BORDER * 2, SCREEN_WIDTH - BORDER * 2), random.randint(BORDER * 4, int(SCREEN_HEIGHT * 0.7) - BORDER * 2))
         self.game_objects.append(ship)
      for i in range(0, self.level * 2):
         ship = self.pool.get_object(Leghorn.__name__)
         ship.hp_reset()
         ship.enable(random.randint(BORDER * 2, SCREEN_WIDTH - BORDER * 2), random.randint(BORDER * 4, int(SCREEN_HEIGHT * 0.5) - BORDER * 2))
         self.game_objects.append(ship)

      for i in range(0, self.level * 3):
         ship = self.pool.get_object(Broiler.__name__)
         ship.hp_reset()
         ship.enable(random.randint(BORDER * 2, SCREEN_WIDTH - BORDER * 2), random.randint(BORDER * 4, int(SCREEN_HEIGHT * 0.7) - BORDER * 2))
         self.game_objects.append(ship)

   def game_loop(self):
      #update
      for obj in self.game_objects:
            obj.update()


      enemies = [obj for obj in self.game_objects if isinstance(obj, (Broiler, Leghorn, Polish))]
      if not enemies:
         if not hasattr(self, 'timer_started') or not self.timer_started:
            self.timer_started = True
            self.timer = pygame.time.get_ticks()

         if pygame.time.get_ticks() - self.timer > 100:
            self.enter_shop()
            self.timer_started = False

      #check check_colisions
      for i in range(len(self.game_objects)):
         for j in range(i+1,len(self.game_objects)):
            #skip destroyed objects
            if self.game_objects[i] in self.to_destroy or self.game_objects[j] in self.to_destroy:
               continue
            self.game_objects[i].check_colision(self.game_objects[j])

      #remove old objects
      for obj in self.to_destroy:
         self.pool.return_object(obj.__class__.__name__,obj)
         if obj in self.game_objects:
            self.game_objects.remove(obj)

      #objects destroyed, clear list
      self.to_destroy = []
      
   def render(self):
      #clear background
      self._DISPLAYSURF.fill(BLACK)

      self.render_GUI()

      #render every game object
      for obj in self.game_objects:
         obj.draw(self._DISPLAYSURF)

      #render game over screen
      if self.game_over:
         self.render_game_over()
   
   def render_GUI(self):
      self._DISPLAYSURF.fill(BLACK)
      self._DISPLAYSURF.blit(self.font.render(f"Level: {self.level}", 1, (255,255,255)), (0, 0))
      self.player.draw_ammo_bar(self._DISPLAYSURF, self.font)
      self.player.draw_health_bar(self._DISPLAYSURF)
      self._DISPLAYSURF.blit(self.font.render(f"Coins: {self.coins}", 1, (255,255,255)), (0, 750))

   def render_game_over(self):
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
 
   def on_event(self, event):
      if event.type == QUIT:
         self.exit()

      if self.in_menu:
         self.menu.handle_event(event)
      
      if self.in_shop:
         self.shop.handle_event(event)

      if self.game_over:
         self.game_over_handle_event(event)

   def clear_lvl(self):
      self.game_over = False
      self.player.reset_hp()
      self.player.reset_ammo()
      self.coins = 0
      self.level = 1
      self.in_shop = False
      self.game_objects = []

   def game_over_handle_event(self, event):
      #Mouse input
      if event.type == pygame.MOUSEBUTTONDOWN:
         mouse_pos = pygame.mouse.get_pos()
         #retry
         if self.retry_rect.collidepoint(mouse_pos):
            self.clear_lvl()
            self.generate_lvl()
         #go back to menu
         elif self.back_to_menu_rect.collidepoint(mouse_pos):
            self.in_menu = True
            self.clear_lvl()
      #Keyboard input
      elif event.type == pygame.KEYDOWN:
         if event.key == pygame.K_UP:
            self.selected_option = (self.selected_option - 1) % 2
         elif event.key == pygame.K_DOWN:
            self.selected_option = (self.selected_option + 1) % 2
         elif event.key == pygame.K_RETURN:
               #retry
            if self.selected_option == 0:
               self.clear_lvl()
               self.generate_lvl()
               #go back to menu
            elif self.selected_option == 1:
               self.in_menu = True
               self.clear_lvl()


   def execute(self):
      
      while(True):
         for event in pygame.event.get():
            self.on_event(event)

         if self.game_over:
               self.render()
         
         elif self.in_menu:
            self.menu.update()
            self.menu.draw(self._DISPLAYSURF)
            
         elif self.in_shop:
            self.shop.draw(self._DISPLAYSURF)
         
         else:
            self.game_loop()
            self.render()
            self.input_handler.handle_input()

            if len(self.game_objects) <= 1:
               self.generate_lvl()


         pygame.display.update()
         self._FramePerSec.tick(self._FPS)


if __name__ == "__main__" :
    game = Game()
    game.execute()
