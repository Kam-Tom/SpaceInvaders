from Player.Command import Command

class ShootCommand(Command):
    def __init__(self, player):
        self.player = player
    def execute(self):
        self.player.shoot()
