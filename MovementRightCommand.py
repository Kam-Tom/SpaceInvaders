from Command import Command

class MovementRightCommand(Command):
    def __init__(self, player):
        self.player = player
    def execute(self):
        self.player.moveRight()

