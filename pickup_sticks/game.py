"""Game module for setting and keeping track of the game-state."""
from player import AIPlayerHard, Player


class Game(object):
    """Sets up and keeps track of the game-state."""
    def __init__(
            self,
            num_players=2,
            num_ai=0,
            num_sticks=50,
            stick_range=(1,10)
        ):
        self.players = []
        human_greeting = "%i player%s" % (num_players, "s" if num_players > 1 else "")
        robot_greeting = "%i robot%s" % (num_ai, "s" if num_ai > 1 else "")
        print("Beginning a game with %s and %s" % (human_greeting, robot_greeting))
        for i in range(num_players):
            self.players.append(Player.register_player(self, i+1))
        for i in range(num_players, num_ai+num_players):
            self.players.append(AIPlayerHard(self, i+1))
        self.num_sticks = num_sticks
        self.stick_range = stick_range

    def play_game(self):
        """Alternate player turns until game is over."""
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

        print("Game over! Player %s wins!" % player)

    def game_over(self):
        """Returns True iff game is over."""
        return self.num_sticks <= 0

    def pickup(self, to_pickup):
        """Pickup to_pickup sticks and return True if valid, else False"""
        if self.stick_range[0] <= to_pickup <= self.stick_range[1]:
            self.num_sticks = max(0, self.num_sticks - to_pickup)
            return True
        return False

    def get_game_state(self):
        """Returns a dictionary of the current game state."""
        return {
            "num_sticks": self.num_sticks,
            "stick_range": self.stick_range,
            "total_players": len(self.players),
        }

    def __str__(self):
        return "Total sticks: %s; Min sticks/turn: %s; Max sticks/turn: %s" % \
            (self.num_sticks, self.stick_range[0], self.stick_range[1])
