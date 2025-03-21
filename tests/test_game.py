"""Test module for Game."""
import mock
import pytest

from pickup_sticks.game import Game


class Test_Game(object):
    """Test class for Game."""
    @pytest.fixture(autouse=True)
    @mock.patch("player.Player.register_player")
    def set_up(self, mock_register_player):
        self.mock_player = mock.Mock()
        mock_register_player.return_value = self.mock_player
        num_players = 1
        num_ai = 1
        num_sticks = 50
        stick_range = (1,10)
        self.game = Game(num_players, num_ai, num_sticks, stick_range)

    @mock.patch("pickup_sticks.game.Game.game_over")
    def test_play_game(self, mock_game_over):
        """Test for play_game, ending after one turn."""
        mock_game_over.side_effect = [False, True, True]
        self.game.play_game()
        self.mock_player.turn.assert_called_once()

    @pytest.mark.parametrize(
        "num_sticks,expected_return_value",
        [
            (1, False),
            (0, True),
            (-1, True),
        ]
    )
    def test_game_over(self, num_sticks, expected_return_value):
        """Test for game_over."""
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
        """Test for pickup."""
        return_value = self.game.pickup(to_pickup)
        assert return_value == expected_return_value
        assert self.game.num_sticks == expected_num_sticks

    def test_get_game_state(self):
        """Test for get_game_state."""
        game_state = self.game.get_game_state()
        assert game_state["num_sticks"] == 50
        assert game_state["stick_range"] == (1,10)
        assert game_state["total_players"] == 2

    def test_str(self):
        """Test for __str__."""
        assert str(self.game) == "Total sticks: 50; Min sticks/turn: 1; Max sticks/turn: 10"
