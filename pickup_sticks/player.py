"""Player module for receiving player input."""
import math
from random import randint as rand


class Player(object):
    """Keeps track of player-state and receives player input."""
    def __init__(self, game, player_no, player_name):
        self.game = game
        self.player_no = player_no
        self.player_name = player_name

    @classmethod
    def register_player(cls, game, player_no):
        """Request player name and initialize player."""
        player_name = input("Welcome Player#%i. What is your name? " % player_no)
        return cls(game, player_no, player_name)

    def get_player_input(self, prompt):
        return input(prompt)

    def turn(self):
        """Player turn."""
        print ("%s's turn. Current game state: %s" % (self, self.game))
        while True:
            player_input = self.get_player_input(
                "How many sticks will you pick up? ")
            try:
                to_pickup = int(player_input)
            except ValueError:
                print(
                    "ERROR: you can't pick up %r sticks! Try a whole number." %
                    player_input
                )
                continue
            if not self.game.pickup(to_pickup):
                print(
                    "ERROR: %i is an invalid number of sticks. The current game state is: %s" % 
                    (to_pickup, self.game)
                )
            else:
                print("%s picked up %i sticks" % (self, to_pickup))
                break


    def __str__(self):
        return "Player#%i:%s" % (self.player_no, self.player_name)


class AIPlayerEasy(Player):
    """Automated player.
    Picks up a random number each turn (unless they can win on their turn).
    """
    def __init__(self, game, player_no):
        super(AIPlayerEasy, self).__init__(game, player_no, "ROBOT")

    def get_player_input(self, prompt):
        """Pick a random number, unless able to win this turn.
        (Returns a str, as this is replacing the functionality of `input`)
        """
        game_state = self.game.get_game_state()
        num_sticks = game_state["num_sticks"]
        stick_range = game_state["stick_range"]
        if num_sticks <= stick_range[1]:
            return str(max(num_sticks, stick_range[0]))
        else:
            return str(rand(stick_range[0], stick_range[1]))


class AIPlayerHard(Player):
    """Automated player.
    Always make the optimal choice, if able.
    """
    def __init__(self, game, player_no):
        super(AIPlayerHard, self).__init__(game, player_no, "ROBOT")

    def get_player_input(self, prompt):
        """Always try to choose the optimal option, otherwise choose the lower range.
        This method is optimal if there are 2 players and the lower range is 1,
        there may be better strategies otherwise.
        """
        game_state = self.game.get_game_state()
        num_sticks = game_state["num_sticks"]
        stick_range = game_state["stick_range"]
        total_players = game_state["total_players"]
        if num_sticks <= stick_range[1]:
            return str(max(num_sticks, stick_range[0]))
        optimal_pick = num_sticks % (stick_range[1] + (total_players - 1))
        if stick_range[0] <= optimal_pick <= stick_range[1]:
            return str(optimal_pick)
        else:
            return str(stick_range[0])
