import pygame
from pygame.locals import *
from constants import *

class Memento:
    def __init__(self, bought_items, balance):
        self._state = bought_items.copy()
        self._balance = balance

    def get_state(self):
        return self._state

    def get_balance(self):
        return self._balance

class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_last_memento(self):
        if self._mementos:
            return self._mementos.pop()
        return None

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
        self.bought_items_history = []
        self.caretaker = Caretaker()
        self.game = game

    def draw(self, surface):
        surface.fill(BLACK)
        title = self.title_font.render("Shop", 5, (255,255,255))
        surface.blit(title, (SCREEN_WIDTH//2 - 30 - title.get_width()//2, SCREEN_HEIGHT//4 - 100))
        balance_text = self.font.render(f"Balance: {self.game.get_player_balance()}", 1, (255,255,255))
        surface.blit(balance_text, (SCREEN_WIDTH//2 - 30 - balance_text.get_width()//2, 0))

        cost_font = pygame.font.SysFont('comicsans', 30)
        x_start = SCREEN_WIDTH//4
        y = SCREEN_HEIGHT//2 - 100
        gap = 300

        for i, option in enumerate(self.options):
            x = x_start + i * gap
            if isinstance(option, tuple):
                image, cost = option
                if i == self.selected_option:
                    pygame.draw.rect(surface, (255,0,0), (x - 10, y - 10, image.get_width() + 20, image.get_height() + 20), 2)
                elif option in self.bought_items:
                    pygame.draw.rect(surface, (0,255,0), (x - 10, y - 10, image.get_width() + 20, image.get_height() + 20), 2)
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

        back_text = self.font.render("Back", 1, (255,255,255))
        x = SCREEN_WIDTH//2 - 30 - back_text.get_width()//2
        y = SCREEN_HEIGHT//2 + 200
        if self.selected_option == len(self.options):
            pygame.draw.rect(surface, (255,255,255), (x - 10, y - 10, back_text.get_width() + 20, back_text.get_height() + 20), 2)
            back_text = self.font.render("Back", 1, (255,0,0))
        surface.blit(back_text, (x, y))

        next_level_text = self.font.render("Next level", 1, (255,255,255))
        x = SCREEN_WIDTH//2 - 30 - next_level_text.get_width()//2
        y += back_text.get_height() + 20
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
                if self.selected_option == len(self.options):
                    if self.bought_items_history:
                        last_bought_item = self.bought_items_history.pop()
                        self.bought_items.remove(last_bought_item)
                        self.game.add_balance(last_bought_item[1])
                elif self.selected_option == len(self.options) + 1:
                    self.game.exit_shop()
                    self.game.start_next_level()
                else:
                    selected_item = self.options[self.selected_option]
                    if selected_item not in self.bought_items and self.game.get_player_balance() >= selected_item[1]:
                        self.bought_items.append(selected_item)
                        self.bought_items_history.append(selected_item)
                        self.game.deduct_balance(selected_item[1])
                    elif selected_item in self.bought_items:
                        self.bought_items.remove(selected_item)
                        self.game.add_balance(selected_item[1])

    def update(self):
        pass