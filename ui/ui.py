from game.game import Game


class Ui:
    def __init__(self, game: Game):
        self._game = game

    @staticmethod
    def print_menu():
        print("\nYou are player 1, your pieces will be displayed as '1' on the board_game.\n"
              "You are playing against the computer, whose moves will be displayed as '2' on the board_game.\n"
              "You must start on the last row of the board_game (row number 5), before making another move "
              "make sure that the place under your desired placing is occupied.\n"
              "The game started.\n")

    def print_board(self):
        board = self._game.get_board_as_string()
        print(board)

    def start_menu(self):
        winner = 0
        game_over = False
        full_board = False
        self.print_menu()
        while game_over is False and full_board is False:
            print("It's your turn! Enter the row and column where you want to place your piece")
            row = int(input("Enter row\n>"))
            column = int(input("Enter column\n>"))
            while self._game.verify_move_validity(row, column) is False:
                print("This place is not available")
                row = int(input("Enter row\n>"))
                column = int(input("Enter column\n>"))
            self._game.human_player_move(row, column)
            self._game.computer_move()
            self.print_board()
            if self._game.verify_if_someone_has_won() is not False:
                winner = self._game.verify_if_someone_has_won()
                game_over = True
            full_board = self._game.verify_if_board_is_full()

        if winner == 1:
            print("You won!")
        elif winner == 2:
            print("The computer won.")
        else:
            print("No one won.")
