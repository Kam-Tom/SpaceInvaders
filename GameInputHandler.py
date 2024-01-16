import pygame

from MovementLeftCommand import MovementLeftCommand
from MovementRightCommand import MovementRightCommand
from ShootCommand import ShootCommand

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
        if keys[pygame.K_SPACE]:
            self.set_command(ShootCommand(self.player))
