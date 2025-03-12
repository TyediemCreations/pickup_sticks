"""Test module for Game."""
import unittest

import mock
import pytest

from pickup_sticks.game import Game


class Test_Game(object):
    """Test module for Game."""
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.num_players = 2
        self.num_sticks = 50
        self.stick_range = (1,10)
        with mock.patch("player.Player.register_player"):
            self.game = Game(self.num_players, self.num_sticks, self.stick_range)

    @pytest.mark.parametrize(
        "num_sticks,expected_return_value",
        [
            (1, False),
            (0, True),
            (-1, True),
        ]
    )
    def test_game_over(self, num_sticks, expected_return_value):
        self.game.num_sticks = num_sticks
        assert self.game.game_over() == expected_return_value

    @pytest.mark.parametrize(
        "to_pickup,expected_num_sticks,expected_return_value",
        [
            (1, 49, True),
            (10, 40, True),
            (0, 50, False),
            (11, 50, False),
        ]
    )
    def test_pickup(self, to_pickup, expected_num_sticks, expected_return_value):
        return_value = self.game.pickup(to_pickup)
        assert return_value == expected_return_value
        assert self.game.num_sticks == expected_num_sticks
