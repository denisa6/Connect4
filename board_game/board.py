from board_game.cell import Cell


class Board:
    def __init__(self, rows, columns, empty_value=0):
        self.__rows = rows
        self.__columns = columns
        self.__empty_value = empty_value

        self.__cells = self.__create_board()

    def __create_board(self):
        """
        This function creates the initial board_game.
        :return: the initial board_game
        """
        return [[Cell(row, column, self.__empty_value) for column in range(self.__columns)]
                for row in range(self.__rows)]

    def set_value(self, row, column, value):
        """
        This function sets the given value on the board_game at the given position (row, column).
        :param row: the row where we want to set the value
        :param column: the column where we want to set the value
        :param value: the value we want to set
        """
        self.__cells[row][column].value = value

    def get_row_values(self, row):
        """
        This function gets all the values on a specific row.
        :param row: the row whose values we want
        :return: the values on the given row
        """
        return [cell.value for cell in self.__cells[row]]

    def get_column_values(self, column):
        """
        This function gets all the values on a specific column.
        :param column: the column whose values we want
        :return: the values on the given column
        """
        return [row[column].value for row in self.__cells]

    def get_empty_cells(self):
        """
        This function gets all the empty cells on the board_game.
        :return: the list of all the empty cells
        """
        return [cell for cell in self.__get_all_cells_as_list() if cell.value == self.__empty_value]

    def __get_all_cells_as_list(self):
        """
        This function gets all the cells in the board_game as a list.
        :return: the list of all the cells
        """
        return [cell for row in self.__cells for cell in row]

    def get_cell_value(self, row, column):
        """
        This function gets a certain cells value.
        :param row: the row of the cell
        :param column: the column of the cell
        :return: the value of the cell
        """
        return self.__cells[row][column].value

    def get_main_diagonal(self, row, column):
        """
        This function gets a list of all the "main" diagonal values based on a specific cell.
        :param row: the row of the first cell
        :param column: the column of the first cell
        :return: the list of the "main" diagonal values
        """
        first_value = self.get_cell_value(row, column)
        second_value = self.get_cell_value(row + 1, column + 1)
        third_value = self.get_cell_value(row + 2, column + 2)
        forth_value = self.get_cell_value(row + 3, column + 3)
        main_diagonal = [first_value, second_value, third_value, forth_value]
        return main_diagonal

    def get_secondary_diagonal(self, row, column):
        """
        This function gets a list of all the "secondary" diagonal values based on a specific cell.
        :param row: the row of the first cell
        :param column: the column of the first cell
        :return: the list of the "secondary" diagonal values
        """
        first_value = self.get_cell_value(row, column)
        second_value = self.get_cell_value(row + 1, column - 1)
        third_value = self.get_cell_value(row + 2, column - 2)
        forth_value = self.get_cell_value(row + 3, column - 3)
        secondary_diagonal = [first_value, second_value, third_value, forth_value]
        return secondary_diagonal

    def __str__(self):
        """
        This function gets the board_game as a string.
        :return: the board_game in str form
        """
        board = ""
        for row in self.__cells:
            row = " ".join([str(cell.value) for cell in row]) + "\n"
            board += row
        return board
