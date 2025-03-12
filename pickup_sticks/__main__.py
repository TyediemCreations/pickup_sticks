"""Main module for pickup_sticks."""
from game import Game
from player import Player


def main():
    game = Game()
    game.play_game()
    return 0


if __name__ == "__main__":
    main()
