import pygame
from pygame.locals import *
from constants import *

class Shop:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.SysFont('comicsans', 50)
        self.title_font = pygame.font.SysFont('comicsans', 80)
        explosion_image = pygame.image.load('Sprites/explosion.png')
        resized_explosion_image = pygame.transform.scale(explosion_image, (150, 150))
        self.options = [(resized_explosion_image, 100), (resized_explosion_image, 200), (resized_explosion_image, 300)]
        self.selected_option = 0
        self.bought_items = []
        self.buy_items_rect = pygame.Rect(0, 0, 0, 0)
        self.game = game

    def draw(self, surface):
        surface.fill(BLACK)
        title = self.title_font.render("Shop", 5, (255,255,255))
        surface.blit(title, (SCREEN_WIDTH//2 - 10 - title.get_width()//2, SCREEN_HEIGHT//4 - 100))
        balance_text = self.font.render(f"Balance: {self.game.get_player_balance()}", 1, (255,255,255))
        surface.blit(balance_text, (SCREEN_WIDTH//2 - balance_text.get_width()//2, 0))

        cost_font = pygame.font.SysFont('comicsans', 30)
        x_start = SCREEN_WIDTH//4
        y = SCREEN_HEIGHT//2 - 100
        gap = 300

        for i, option in enumerate(self.options):
            x = x_start + i * gap
            if isinstance(option, tuple):
                image, cost = option
                if option in self.bought_items and i != self.selected_option:
                    pygame.draw.rect(surface, (0,255,0), (x - 10, y - 10, image.get_width() + 20, image.get_height() + 20), 2)
                elif i == self.selected_option:
                    pygame.draw.rect(surface, (255,0,0), (x - 10, y - 10, image.get_width() + 20, image.get_height() + 20), 2)
                else:
                    pygame.draw.rect(surface, (255,255,255), (x - 10, y - 10, image.get_width() + 20, image.get_height() + 20), 2)
                surface.blit(image, (x, y))
                cost_text = cost_font.render(f"Cost: {cost}", 1, (255,255,255))
                surface.blit(cost_text, (x, y + image.get_height() + 10))
            else:
                text = self.font.render(option, 1, (255,255,255))
                x = SCREEN_WIDTH//2 - text.get_width()//2
                y = SCREEN_HEIGHT//2 + 200
                if i == self.selected_option:
                    pygame.draw.rect(surface, (255,255,255), (x + 150 - 10, y - 10, text.get_width() + 20, text.get_height() + 20), 2)
                    text = self.font.render(option, 1, (255,0,0))
                surface.blit(text, (x + 150, y))

        total_cost = sum(item[1] for item in self.bought_items)
        buy_items_text = self.font.render(f"Buy items: {total_cost}", 1, (255,255,255))
        x = SCREEN_WIDTH//2 - buy_items_text.get_width()//2 - 200
        y = SCREEN_HEIGHT//2 + 200
        if self.selected_option == len(self.options):
            pygame.draw.rect(surface, (255,255,255), (x - 10, y - 10, buy_items_text.get_width() + 20, buy_items_text.get_height() + 20), 2)
            buy_items_text = self.font.render(f"Buy items: {total_cost}", 1, (255,0,0))
        surface.blit(buy_items_text, (x, y))
        self.buy_items_rect = pygame.Rect(x, y, buy_items_text.get_width(), buy_items_text.get_height())

        exit_shop_text = self.font.render("Exit shop", 1, (255,255,255))
        x = SCREEN_WIDTH//2 - exit_shop_text.get_width()//2 + 200
        if self.selected_option == len(self.options) + 1:
            pygame.draw.rect(surface, (255,255,255), (x - 10, y - 10, exit_shop_text.get_width() + 20, exit_shop_text.get_height() + 20), 2)
            exit_shop_text = self.font.render("Exit shop", 1, (255,0,0))
        surface.blit(exit_shop_text, (x, y))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % (len(self.options) + 2)
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % (len(self.options) + 2)
            elif event.key == pygame.K_RETURN:
                if self.selected_option == len(self.options):
                    self.buy_items()
                elif self.selected_option == len(self.options) + 1:
                    self.game.exit_shop()
                else:
                    selected_item = self.options[self.selected_option]
                    if selected_item in self.bought_items:
                        self.bought_items.remove(selected_item)
                    else:
                        self.bought_items.append(selected_item)

    def buy_items(self):
        total_cost = sum(item[1] for item in self.bought_items)
        if self.game.get_player_balance() >= total_cost:
            self.game.deduct_balance(total_cost)
            self.bought_items = []
        else:
            print("Not enough balance to buy items")

    def update(self):
        pass