"""Test module for Player."""
import mock
import pytest

from pickup_sticks.player import Player


class Test_Player(object):
    """Test class for Player"""
    @pytest.fixture(autouse=True)
    @mock.patch("game.Game")
    def set_up(self, mock_game):
        self.mock_game = mock_game
        self.player = Player(self.mock_game, 1, "test_player")

    def test_register_player(self):
        """Test for class method register_player."""
        with mock.patch("builtins.input", return_value="foobar"):
            player = Player.register_player(self.mock_game, 5)
        assert player.game == self.mock_game
        assert player.player_no == 5
        assert player.player_name == "foobar"

    def test_turn_valid(self):
        self.mock_game.pickup.return_value = True
        with mock.patch("builtins.input", return_value="10"):
            self.player.turn()
        self.mock_game.pickup.assert_called_once_with(10)

    @mock.patch("builtins.print")
    def test_turn_ValueError(self, mock_print):
        self.mock_game.pickup.return_value = True
        with mock.patch("builtins.input", side_effect=["non-int", "10"]):
            self.player.turn()
        mock_print.assert_has_calls([
            mock.call("Player#1:test_player's turn. Current game state: %s" % self.mock_game),
            mock.call("ERROR: you can't pick up 'non-int' sticks! Try a whole number."),
        ])

    @mock.patch("builtins.print")
    def test_turn_invalid_number(self, mock_print):
        self.mock_game.pickup.side_effect = [False, True]
        with mock.patch("builtins.input", return_value="1"):
            self.player.turn()
        mock_print.assert_has_calls([
            mock.call("Player#1:test_player's turn. Current game state: %s" % self.mock_game),
            mock.call("ERROR: 1 is an invalid number of sticks. The current game state is: %s" % self.mock_game),
        ])
        
