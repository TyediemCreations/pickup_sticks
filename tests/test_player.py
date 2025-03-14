"""Test module for Player."""
import mock
import pytest

from pickup_sticks.player import AIPlayerEasy, AIPlayerHard, Player


class Test_PlayerBase(object):
    """Base test class for Player"""
    @mock.patch("game.Game")
    def set_up(self, mock_game):
        self.mock_game = mock_game


class Test_Player(Test_PlayerBase):
    """Test class for Player"""
    @pytest.fixture(autouse=True)
    def set_up(self):
        super(Test_Player, self).set_up()
        self.player = Player(self.mock_game, 1, "test_player")

    def test_register_player(self):
        """Test for class method register_player."""
        with mock.patch("builtins.input", return_value="foobar"):
            player = Player.register_player(self.mock_game, 5)
        assert player.game == self.mock_game
        assert player.player_no == 5
        assert player.player_name == "foobar"

    def test_turn_valid(self):
        """Test for turn, with valid input."""
        self.mock_game.pickup.return_value = True
        with mock.patch("builtins.input", return_value="10"):
            self.player.turn()
        self.mock_game.pickup.assert_called_once_with(10)

    @mock.patch("builtins.print")
    def test_turn_ValueError(self, mock_print):
        """Test for turn, with non-int input."""
        self.mock_game.pickup.return_value = True
        with mock.patch("builtins.input", side_effect=["non-int", "10"]):
            self.player.turn()
        mock_print.assert_has_calls([
            mock.call("Player#1:test_player's turn. Current game state: %s" % self.mock_game),
            mock.call("ERROR: you can't pick up 'non-int' sticks! Try a whole number."),
        ])

    @mock.patch("builtins.print")
    def test_turn_invalid_number(self, mock_print):
        """Test for turn, with invalid int input."""
        self.mock_game.pickup.side_effect = [False, True]
        with mock.patch("builtins.input", return_value="1"):
            self.player.turn()
        mock_print.assert_has_calls([
            mock.call("Player#1:test_player's turn. Current game state: %s" % self.mock_game),
            mock.call("ERROR: 1 is an invalid number of sticks. The current game state is: %s" % self.mock_game),
        ])


class Test_AIPlayerEasy(Test_PlayerBase):
    """Test class for AIPlayerEasy"""
    @pytest.fixture(autouse=True)
    def set_up(self):
        super(Test_AIPlayerEasy, self).set_up()
        self.player = AIPlayerEasy(self.mock_game, 1)

    @pytest.mark.parametrize(
        "game_state,expected",
        [
            ({"num_sticks":10, "stick_range":(1,10)}, "10"),
            ({"num_sticks":11, "stick_range":(1,10)}, "5"),
        ]
    )
    @mock.patch("pickup_sticks.player.randint", return_value=5)
    def test_get_player_input(self, mock_rand, game_state, expected):
        self.mock_game.get_game_state.return_value = game_state
        assert self.player.get_player_input("") == expected


class Test_AIPlayerHard(Test_PlayerBase):
    """Test class for AIPlayerHard"""
    @pytest.fixture(autouse=True)
    def set_up(self):
        super(Test_AIPlayerHard, self).set_up()
        self.player = AIPlayerHard(self.mock_game, 1)

    @pytest.mark.parametrize(
        "game_state,expected",
        [
            ({"num_sticks":10, "stick_range":(1,10), "total_players":2}, "10"),
            ({"num_sticks":11, "stick_range":(1,10), "total_players":2}, "1"),
            ({"num_sticks":15, "stick_range":(1,10), "total_players":2}, "4"),
        ]
    )
    @mock.patch("pickup_sticks.player.randint", return_value=5)
    def test_get_player_input(self, mock_rand, game_state, expected):
        self.mock_game.get_game_state.return_value = game_state
        assert self.player.get_player_input("") == expected
