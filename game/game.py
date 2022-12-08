from board_game.board import Board
import random


class Game:
    def __init__(self, board: Board):
        self._board = board

    def verify_move_validity(self, row, column):
        """
        This function verifies whether a move is valid or not.
        :param row: the row of the said move
        :param column: the column of the move
        :return: True if the move is valid, False if it isn't
        """
        if self._board.get_cell_value(row, column):
            return False
        if row < 0 or column < 0 or row >= 6 or column >= 7:
            return False
        if row != 5 and self._board.get_cell_value(row + 1, column) == 0:
            return False
        return True

    def verify_if_board_is_full(self):
        """
        This function verifies whether the board_game is full or not.
        :return: True if the board_game is full, False if it isn't
        """
        empty_cells = self._board.get_empty_cells()
        if len(empty_cells) == 0:
            return True
        return False

    def human_player_move(self, row, column):
        """
        This function assigns the human player move.
        :param row: the row of the move
        :param column: the column of the move
        """
        player_symbol = 1
        self._board.set_value(row, column, player_symbol)

    def computer_move(self):
        """
        This function assigns the computer move.
        """
        player_symbol = 2
        if self.horizontal_possible_win() is not False:
            row, column = self.horizontal_possible_win()
        elif self.vertical_possible_win() is not False:
            row, column = self.vertical_possible_win()
        elif self.oblique_possible_win() is not False:
            row, column = self.oblique_possible_win()
        else:
            row = random.randint(0, 5)
            column = random.randint(0, 6)
        while self.verify_move_validity(row, column) is False:
            row = random.randint(0, 5)
            column = random.randint(0, 5)
        self._board.set_value(row, column, player_symbol)

    def verify_if_someone_has_won(self):
        """
        This function verifies whether someone has won
        :return: False if no one won or the player symbol of the winner
        """
        if self.horizontal_win() is not False:
            return self.horizontal_win()
        if self.vertical_win() is not False:
            return self.vertical_win()
        if self.oblique_win() is not False:
            return self.oblique_win()
        return False

    def horizontal_possible_win(self):
        """
        This function verifies if a horizontal win is about to happen.
        :return: the coordinates of the empty cell if a win is about to happen or False if it isn't
        """
        for i in range(6):
            row = self._board.get_row_values(i)
            for j in range(4):
                if row[j] == 0 and row[j+1] == row[j+2] == row[j+3] and row[j+1] != 0:
                    return i, j
                if row[j+1] == 0 and row[j] == row[j+2] == row[j+3] and row[j] != 0:
                    return i, j+1
                if row[j+2] == 0 and row[j] == row[j+1] == row[j+3] and row[j] != 0:
                    return i, j+2
                if row[j+3] == 0 and row[j] == row[j+1] == row[j+2] and row[j] != 0:
                    return i, j+3
        return False

    def vertical_possible_win(self):
        """
            This function verifies if a vertical win is about to happen.
            :return: the coordinates of the empty cell if a win is about to happen or False if it isn't
        """
        for j in range(7):
            column = self._board.get_column_values(j)
            for i in range(3):
                if column[i] == 0 and column[i + 1] == column[i + 2] == column[i + 3] and column[i + 1] != 0:
                    return i, j
                if column[i + 1] == 0 and column[i] == column[i + 2] == column[i + 3] and column[i] != 0:
                    return i+1, j
                if column[i + 2] == 0 and column[i] == column[i + 1] == column[i + 3] and column[i] != 0:
                    return i+2, j
                if column[i + 3] == 0 and column[i] == column[i + 1] == column[i + 2] and column[i] != 0:
                    return i+3, j
        return False

    def oblique_possible_win(self):
        """
            This function verifies if a diagonal win is about to happen.
            :return: the coordinates of the empty cell if a win is about to happen or False if it isn't
        """
        for i in range(3):
            for j in range(4):
                left_diagonal = self._board.get_main_diagonal(i, j)
                if left_diagonal[0] == 0 and left_diagonal[1] == left_diagonal[2] == left_diagonal[3] and \
                   left_diagonal[1] != 0:
                    return i, j
                if left_diagonal[1] == 0 and left_diagonal[0] == left_diagonal[2] == left_diagonal[3] and \
                   left_diagonal[0] != 0:
                    return i+1, j+1
                if left_diagonal[2] == 0 and left_diagonal[0] == left_diagonal[1] == left_diagonal[3] and \
                   left_diagonal[0] != 0:
                    return i+2, j+2
                if left_diagonal[3] == 0 and left_diagonal[0] == left_diagonal[1] == left_diagonal[2] and \
                   left_diagonal[0] != 0:
                    return i+3, j+3
            for j in range(3, 7):
                right_diagonal = self._board.get_secondary_diagonal(i, j)
                if right_diagonal[0] == 0 and right_diagonal[1] == right_diagonal[2] == right_diagonal[3] and \
                   right_diagonal[1] != 0:
                    return i, j
                if right_diagonal[1] == 0 and right_diagonal[0] == right_diagonal[2] == right_diagonal[3] and \
                   right_diagonal[0] != 0:
                    return i+1, j-1
                if right_diagonal[2] == 0 and right_diagonal[0] == right_diagonal[1] == right_diagonal[3] and \
                   right_diagonal[0] != 0:
                    return i+2, j-2
                if right_diagonal[3] == 0 and right_diagonal[0] == right_diagonal[1] == right_diagonal[2] and \
                   right_diagonal[0] != 0:
                    return i+3, j-3
        return False

    def horizontal_win(self):
        """
            This function verifies if a horizontal win has happened.
            :return: the player symbol of the winner or False if there isn't one
        """
        for i in range(6):
            row = self._board.get_row_values(i)
            for j in range(4):
                if row[j] == row[j + 1] == row[j + 2] == row[j + 3] and row[j] != 0:
                    return self._board.get_cell_value(i, j)
        return False

    def vertical_win(self):
        """
            This function verifies if a vertical win has happened.
            :return: the player symbol of the winner or False if there isn't one
        """
        for j in range(7):
            column = self._board.get_column_values(j)
            for i in range(3):
                if column[i] == column[i+1] == column[i+2] == column[i+3] and column[i+1] != 0:
                    return self._board.get_cell_value(i, j)
        return False

    def oblique_win(self):
        """
            This function verifies if a diagonal win has happened.
            :return: the player symbol of the winner or False if there isn't one
        """
        for i in range(3):
            for j in range(4):
                left_diagonal = self._board.get_main_diagonal(i, j)
                if left_diagonal[0] == left_diagonal[1] == left_diagonal[2] == left_diagonal[3] and \
                   left_diagonal[0] != 0:
                    return self._board.get_cell_value(i, j)
            for j in range(3, 7):
                right_diagonal = self._board.get_secondary_diagonal(i, j)
                if right_diagonal[0] == right_diagonal[1] == right_diagonal[2] == right_diagonal[3] and \
                   right_diagonal[0] != 0:
                    return self._board.get_cell_value(i, j)
        return False

    def get_board_as_string(self):
        """
            This function gets the board_game as a string.
            :return: the board_game in str form
        """
        return self._board.__str__()
