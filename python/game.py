"""Game module for setting and keeping track of the game-state."""
from player import Player


class Game(object):
    """Sets up and keeps track of the game-state."""
    def __init__(self, num_players=2, num_sticks=50, stick_range=(1,10)):
        self.players = []
        print ("Beginning a game with %i players." % num_players)
        for i in range(num_players):
            self.players.append(Player.register_player(self, i+1))
        self.num_sticks = num_sticks
        self.stick_range = stick_range

    def play_game(self):
        print(
            "Welcome to the wonderful world of pickup sticks! There are %i "\
            "sticks on the ground, you must pick up %i-%i sticks per turn. "\
            "Whoever picks up the last stick wins!" %
            (self.num_sticks, self.stick_range[0], self.stick_range[1])
        )

        while not self.game_over():
            for player in self.players:
                player.turn()
                if self.game_over():
                    break

        print ("Game over! Player %s wins!" % player)

    def game_over(self):
        return self.num_sticks <= 0

    def pickup(self, to_pickup):
        if self.stick_range[0] <= to_pickup <= self.stick_range[1]:
            self.num_sticks = max(0, self.num_sticks - to_pickup)
            return True
        return False

    def __str__(self):
        return "Total sticks: %s; Min sticks/turn: %s; Max sticks/turn: %s" % \
            (self.num_sticks, self.stick_range[0], self.stick_range[1])
