import pygame
from pygame.locals import *
from constants import *

class Menu:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.SysFont('comicsans', 50)
        self.title_font = pygame.font.SysFont('comicsans', 80)
        self.options = ["Play", "Shop", "Exit"]
        self.selected_option = 0

    def draw(self, surface):
        surface.fill(BLACK)
        title = self.title_font.render("Chicken Invaders", 1, (255,255,255))
        surface.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, SCREEN_HEIGHT//4))

        for i, option in enumerate(self.options):
            text = self.font.render(option, 1, (255,255,255))
            y = SCREEN_HEIGHT//2 + i * 90
            if i == self.selected_option:
                pygame.draw.rect(surface, (255,255,255), (SCREEN_WIDTH//2 - text.get_width()//2 - 10, y - 10, text.get_width() + 20, text.get_height() + 20), 2)
                text = self.font.render(option, 1, (255,0,0))
            surface.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, y))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                if self.selected_option == 0:
                    self.game.start_game()
                elif self.selected_option == 1:
                    self.game.enter_shop()
                elif self.selected_option == 2:
                    pygame.quit()

    def update(self):
        pass