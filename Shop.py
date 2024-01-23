import pygame
from pygame.locals import *
from constants import *


class Shop:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.SysFont('comicsans', 50)
        self.title_font = pygame.font.SysFont('comicsans', 80)
        shop_item_1 = pygame.image.load('Sprites/shop_item_1.png')
        shop_item_2 = pygame.image.load('Sprites/shop_item_2.png')
        shop_item_3 = pygame.image.load('Sprites/shop_item_3.png')
        resized_shop_item_1 = pygame.transform.scale(shop_item_1, (150, 150))
        resized_shop_item_2 = pygame.transform.scale(shop_item_2, (150, 150))
        resized_shop_item_3 = pygame.transform.scale(shop_item_3, (150, 150))
        self.options = [(resized_shop_item_1, ITEM_COST), (resized_shop_item_2, ITEM_COST), (resized_shop_item_3, ITEM_COST)]
        self.selected_option = 0
        self.game = game
        self._ship_history = []
        self.item_quantities = [game.player.get_ammo(),game.player.get_speed(),game.player.get_max_hp()]

    def draw(self, surface):
        surface.fill(BLACK)
        self.draw_title(surface)
        self.draw_balance(surface)
        self.draw_options(surface)
        self.draw_back_button(surface)
        self.draw_next_level_button(surface)

    def draw_title(self, surface):
        title = self.title_font.render("Shop", 5, (255,255,255))
        surface.blit(title, (SCREEN_WIDTH//2 - 30 - title.get_width()//2, SCREEN_HEIGHT//4 - 100))

    def draw_balance(self, surface):
        balance_text = self.font.render(f"Balance: {self.game.coins}", 1, (255,255,255))
        surface.blit(balance_text, (SCREEN_WIDTH//2 - 30 - balance_text.get_width()//2, 0))

    def draw_options(self, surface):
        cost_font = pygame.font.SysFont('comicsans', 30)
        x_start = SCREEN_WIDTH//4
        y = SCREEN_HEIGHT//2 - 100
        gap = 300

        for i, option in enumerate(self.options):
            x = x_start + i * gap
            if isinstance(option, tuple):
                self.draw_option(surface, option, i, x, y, cost_font)
            else:
                self.draw_text_option(surface, option, i, x, y)

    def draw_option(self, surface, option, i, x, y, cost_font):
        image, cost = option
        if i == self.selected_option:
            pygame.draw.rect(surface, (255,0,0), (x - 10, y - 10, image.get_width() + 20, image.get_height() + 20), 2)
        else:
            pygame.draw.rect(surface, (255,255,255), (x - 10, y - 10, image.get_width() + 20, image.get_height() + 20), 2)
        
        quantity_text = cost_font.render(f"Quantity: {self.item_quantities[i]}", 1, (255,255,255))
        surface.blit(quantity_text, (x + image.get_width()//2 - quantity_text.get_width()//2, y - quantity_text.get_height() - 10))
        surface.blit(image, (x, y))
        cost_text = cost_font.render(f"Cost: {cost}", 1, (255,255,255))
        surface.blit(cost_text, (x + image.get_width()//2 - cost_text.get_width()//2, y + image.get_height() + 10))

    def draw_text_option(self, surface, option, i, x, y):
        text = self.font.render(str(option), 1, (255,255,255))
        x = SCREEN_WIDTH//2 - text.get_width()//2
        y = SCREEN_HEIGHT//2 + 200
        if i == self.selected_option:
            pygame.draw.rect(surface, (255,255,255), (x + 150 - 10, y - 10, text.get_width() + 20, text.get_height() + 20), 2)
            text = self.font.render(option, 1, (255,0,0))
        surface.blit(text, (x + 150, y))

    def draw_back_button(self, surface):
        back_text = self.font.render("Back", 1, (255,255,255))
        x = SCREEN_WIDTH//2 - 30 - back_text.get_width()//2
        y = SCREEN_HEIGHT//2 + 200
        if self.selected_option == len(self.options):
            pygame.draw.rect(surface, (255,255,255), (x - 10, y - 10, back_text.get_width() + 20, back_text.get_height() + 20), 2)
            back_text = self.font.render("Back", 1, (255,0,0))
        surface.blit(back_text, (x, y))

    def draw_next_level_button(self, surface):
        next_level_text = self.font.render("Next level", 1, (255,255,255))
        back_text = self.font.render("Back", 1, (255,255,255))
        x = SCREEN_WIDTH//2 - 30 - next_level_text.get_width()//2
        y = SCREEN_HEIGHT//2 + 200 + back_text.get_height() + 20
        if self.selected_option == len(self.options) + 1:
            pygame.draw.rect(surface, (255,255,255), (x - 10, y - 10, next_level_text.get_width() + 20, next_level_text.get_height() + 20), 2)
            next_level_text = self.font.render("Next level", 1, (255,0,0))
        surface.blit(next_level_text, (x, y))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % (len(self.options) + 2)
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % (len(self.options) + 2)
            
            elif event.key == pygame.K_RETURN:

                #Not enough money
                if self.selected_option < 3 and self.game.coins < ITEM_COST:
                    return
                
                if self.selected_option == 0:
                    self.backup_ship()
                    self.game.player.add_max_ammo()
                    self.game.coins -= ITEM_COST
            
                if self.selected_option == 1:
                    self.backup_ship()
                    self.game.player.add_speed()
                    self.game.coins -= ITEM_COST

                if self.selected_option == 2:
                    self.backup_ship()
                    self.game.player.add_max_hp()
                    self.game.coins -= ITEM_COST

                if self.selected_option == 3:
                    self.undo_shopping()

                self.update_item_quantitis()


                if self.selected_option == 4:
                    self.game.exit_shop()
                    self.game.start_next_level()


    def update_item_quantitis(self):
        self.item_quantities = [self.game.player.get_ammo(),self.game.player.get_speed(),self.game.player.get_max_hp()]

    def undo_shopping(self):
        if len(self._ship_history) == 0:
            return
        snapshot = self._ship_history.pop()
        self.game.player.restore(snapshot)
        self.game.coins += ITEM_COST



    def backup_ship(self):
        self._ship_history.append(self.game.player.save())
