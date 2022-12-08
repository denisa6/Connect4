import unittest
from game import Game
from board_game.board import Board


class GameTest(unittest.TestCase):
    def setUp(self) -> None:
        self._game = Game(Board(6, 7))

    def test_verify_move_validity__valid_move__True(self):
        self.assertTrue(self._game.verify_move_validity(5, 0))

    def test_verify_move_validity__invalid_move__False(self):
        self.assertFalse(self._game.verify_move_validity(4, 3))

    def test_verify_if_board_is_full__full_board__True(self):
        for i in range(6):
            for j in range(7):
                self._game.human_player_move(i, j)
        self.assertTrue(self._game.verify_if_board_is_full())

    def test_verify_if_board_is_full__board_not_full__False(self):
        self._game.human_player_move(0, 0)
        self.assertFalse(self._game.verify_if_board_is_full())

    def test_human_player_move__empty_board__value_placed_correctly(self):
        self._game.human_player_move(0, 0)
        self.assertEqual(self._game._board.get_cell_value(0, 0), 1)

    def test_computer_move__human_player_about_to_win__blocked_human_player_win(self):
        self._game.human_player_move(5, 0)
        self._game.human_player_move(5, 1)
        self._game.human_player_move(5, 2)
        self._game.computer_move()
        self.assertEqual(self._game._board.get_cell_value(5, 3), 2)

    def test_verify_if_someone_has_won__human_player_won__human_player_symbol(self):
        self._game.human_player_move(0, 0)
        self._game.human_player_move(0, 1)
        self._game.human_player_move(0, 2)
        self._game.human_player_move(0, 3)
        self.assertEqual(self._game.verify_if_someone_has_won(), 1)

    def test_verify_if_someone_has_won__computer_won__computer_symbol(self):
        self._game._board.set_value(0, 0, 2)
        self._game._board.set_value(0, 1, 2)
        self._game._board.set_value(0, 2, 2)
        self._game._board.set_value(0, 3, 2)
        self.assertEqual(self._game.verify_if_someone_has_won(), 2)

    def test_verify_if_someone_has_won__nobody_won__False(self):
        self._game.human_player_move(0, 0)
        self._game.computer_move()
        self._game.human_player_move(0, 2)
        self._game.human_player_move(0, 3)
        self.assertFalse(self._game.verify_if_someone_has_won())

    def test_horizontal_possible_win__human_player_is_about_to_win__correct_coordinates(self):
        self._game.human_player_move(0, 0)
        self._game.human_player_move(0, 1)
        self._game.human_player_move(0, 2)
        self.assertEqual(self._game.horizontal_possible_win(), (0, 3))

    def test_horizontal_possible_win__computer_is_about_to_win__correct_coordinates(self):
        self._game._board.set_value(0, 0, 2)
        self._game._board.set_value(0, 1, 2)
        self._game._board.set_value(0, 2, 2)
        self.assertEqual(self._game.horizontal_possible_win(), (0, 3))

    def test_horizontal_possible_win__nobody_is_about_to_win__False(self):
        self._game.human_player_move(0, 0)
        self._game.computer_move()
        self._game.human_player_move(0, 2)
        self.assertFalse(self._game.horizontal_possible_win())

    def test_vertical_possible_win__human_player_is_about_to_win__correct_coordinates(self):
        self._game.human_player_move(0, 0)
        self._game.human_player_move(1, 0)
        self._game.human_player_move(2, 0)
        self.assertEqual(self._game.vertical_possible_win(), (3, 0))

    def test_vertical_possible_win__computer_is_about_to_win__correct_coordinates(self):
        self._game._board.set_value(0, 0, 2)
        self._game._board.set_value(1, 0, 2)
        self._game._board.set_value(2, 0, 2)
        self.assertEqual(self._game.vertical_possible_win(), (3, 0))

    def test_vertical_possible_win__nobody_is_about_to_win__False(self):
        self._game.human_player_move(0, 0)
        self._game.computer_move()
        self.assertFalse(self._game.vertical_possible_win())

    def test_oblique_possible_win__human_player_is_about_to_win__correct_coordinates(self):
        self._game.human_player_move(0, 0)
        self._game.human_player_move(1, 1)
        self._game.human_player_move(2, 2)
        self.assertEqual(self._game.oblique_possible_win(), (3, 3))

    def test_oblique_possible_win__computer_is_about_to_win__correct_coordinates(self):
        self._game._board.set_value(0, 0, 2)
        self._game._board.set_value(1, 1, 2)
        self._game._board.set_value(2, 2, 2)
        self.assertEqual(self._game.oblique_possible_win(), (3, 3))

    def test_oblique_possible_win__nobody_is_about_to_win__False(self):
        self._game.human_player_move(0, 0)
        self._game.computer_move()
        self.assertFalse(self._game.oblique_possible_win())

    def test_horizontal_win__human_player_won__human_player_symbol(self):
        self._game.human_player_move(0, 0)
        self._game.human_player_move(0, 1)
        self._game.human_player_move(0, 2)
        self._game.human_player_move(0, 3)
        self.assertEqual(self._game.horizontal_win(), 1)

    def test_horizontal_win__computer_won__computer_symbol(self):
        self._game._board.set_value(0, 0, 2)
        self._game._board.set_value(0, 1, 2)
        self._game._board.set_value(0, 2, 2)
        self._game._board.set_value(0, 3, 2)
        self.assertEqual(self._game.horizontal_win(), 2)

    def test_horizontal_win__nobody_won__False(self):
        self._game.human_player_move(0, 0)
        self._game.computer_move()
        self.assertFalse(self._game.horizontal_win())

    def test_vertical_win__human_player_won__human_player_symbol(self):
        self._game.human_player_move(0, 0)
        self._game.human_player_move(1, 0)
        self._game.human_player_move(2, 0)
        self._game.human_player_move(3, 0)
        self.assertEqual(self._game.vertical_win(), 1)

    def test_vertical_win__computer_won__computer_symbol(self):
        self._game._board.set_value(0, 0, 2)
        self._game._board.set_value(1, 0, 2)
        self._game._board.set_value(2, 0, 2)
        self._game._board.set_value(3, 0, 2)
        self.assertEqual(self._game.vertical_win(), 2)

    def test_vertical_win__nobody_won__False(self):
        self._game.human_player_move(0, 0)
        self._game.computer_move()
        self.assertFalse(self._game.vertical_win())

    def test_oblique_win__human_player_won__human_player_symbol(self):
        self._game.human_player_move(0, 0)
        self._game.human_player_move(1, 1)
        self._game.human_player_move(2, 2)
        self._game.human_player_move(3, 3)
        self.assertEqual(self._game.oblique_win(), 1)

    def test_oblique_win__computer_won__computer_symbol(self):
        self._game._board.set_value(0, 0, 2)
        self._game._board.set_value(1, 1, 2)
        self._game._board.set_value(2, 2, 2)
        self._game._board.set_value(3, 3, 2)
        self.assertEqual(self._game.oblique_win(), 2)

    def test_oblique_win__nobody_won__False(self):
        self._game.human_player_move(0, 0)
        self._game.computer_move()
        self.assertFalse(self._game.oblique_win())
