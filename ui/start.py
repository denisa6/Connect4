from board_game.board import Board
from game.game import Game
from ui import Ui


if __name__ == '__main__':
    ui = Ui(Game(Board(6, 7)))
    ui.start_menu()
