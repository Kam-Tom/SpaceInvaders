import pygame

from MovementLeftCommand import MovementLeftCommand
from MovementRightCommand import MovementRightCommand

class GameInputHandler:
    def __init__(self, player):
        self.player = player
        self.command = None

    def set_command(self, command):
        self.command = command
        self.command.execute()

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.set_command(MovementLeftCommand(self.player))
        if keys[pygame.K_RIGHT]:
            self.set_command(MovementRightCommand(self.player))
