import unittest
from board import Board


class BoardTest(unittest.TestCase):
    def setUp(self) -> None:
        self._board = Board(6, 7)

    def test_set_value__initial_board__one_set_element(self):
        self._board.set_value(0, 0, 1)
        self.assertEqual(self._board.get_cell_value(0, 0), 1)

    def test_get_row_values__initial_board__correct_list(self):
        self._board.set_value(0, 0, 1)
        self._board.set_value(0, 1, 2)
        self.assertEqual(self._board.get_row_values(0), [1, 2, 0, 0, 0, 0, 0])

    def test_get_column_value__initial_board__correct_list(self):
        self._board.set_value(0, 0, 1)
        self._board.set_value(1, 0, 2)
        self.assertEqual(self._board.get_column_values(0), [1, 2, 0, 0, 0, 0])

    def test_get_empty_cells__initial_board__41_element_list(self):
        self._board.set_value(0, 0, 1)
        self.assertEqual(len(self._board.get_empty_cells()), 41)

    def test_get_cell_value__initial_list__correct_value(self):
        self._board.set_value(0, 0, 1)
        self.assertEqual(self._board.get_cell_value(0, 0), 1)

    def test_get_main_diagonal__initial_board__correct_list(self):
        self._board.set_value(0, 0, 1)
        self._board.set_value(1, 1, 2)
        self.assertEqual(self._board.get_main_diagonal(0, 0), [1, 2, 0, 0])

    def test_get_secondary_diagonal__initial_board__correct_list(self):
        self._board.set_value(0, 3, 1)
        self._board.set_value(1, 2, 2)
        self.assertEqual(self._board.get_secondary_diagonal(0, 3), [1, 2, 0, 0])
