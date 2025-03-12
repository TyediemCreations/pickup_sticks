"""Player module for receiving player input."""


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

    def turn(self):
        """Player turn."""
        print ("%s's turn. Current game state: %s" % (self, self.game))
        while True:
            to_pickup = int(input("How many sticks will you pick up? "))
            if not self.game.pickup(to_pickup):
                print(
                    "ERROR: %i is an invalid number of sticks. The current game state is: %s" % 
                    (to_pickup, self.game)
                )
            else:
                break


    def __str__(self):
        return "Player#%i:%s" % (self.player_no, self.player_name)
