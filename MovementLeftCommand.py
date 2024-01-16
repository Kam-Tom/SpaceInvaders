from Command import Command

class MovementLeftCommand(Command):
    def __init__(self, player):
        self.player = player
    def execute(self):
        self.player.moveLeft()
