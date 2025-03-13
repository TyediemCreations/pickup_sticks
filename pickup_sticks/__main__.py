"""Main module for pickup_sticks."""
import argparse
import sys

from game import Game


def setup_arguments():
    parser = argparse.ArgumentParser(
        prog="Pickup Sticks",
        description="Someone dropped all these sticks, and it's your job to pick 'em up!",
    )
    parser.add_argument(
        "-p", "--players",
        type=int,
        default=2,
        help="Number of human players.",
    )
    parser.add_argument(
        "-n", "--numsticks",
        type=int,
        default=50,
        help="Number of sticks.",
    )
    parser.add_argument(
        "-r", "--range",
        nargs=2,
        type=int,
        default=(1,10),
        help="Min/Max sticks that can be picked up per turn.",
    )
    args = parser.parse_args()
    args.range = tuple(args.range)
    return args


def main():
    args = setup_arguments()
    game = Game(
        num_players=args.players,
        num_sticks=args.numsticks,
        stick_range=args.range,
    )
    game.play_game()
    return 0


if __name__ == "__main__":
    main()
