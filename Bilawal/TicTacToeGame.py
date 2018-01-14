from Bilawal.MCTS import MonteCarloTree, WIN, LOSS, DRAW, NEITHER
from Bilawal.TicTacToeTree import TicTacToeMCTS
from Bilawal.Utils import fetch, persist
from Bilawal.TicTacToeTree import MOVES, MOVES_INDEX
import random

class TicTacToeGame:

    def __init__(self):
        self.tree = fetch()
        if self.tree is None:
            self.tree = TicTacToeMCTS()

    def print_board(self, board):
        string = " {0} | {1} | {2} \n".format(*board[0])
        string += " {0} | {1} | {2} \n".format(*board[1])
        string += " {0} | {1} | {2} \n".format(*board[2])
        print(string)

    def loop(self):
        while True:
            print("PRESS N TO START NEW GAME OF TICTACTOE\nPress X TO EXIT THE GAME")
            new_game = input()
            if new_game == 'X':
                break
            elif new_game == 'N':
                self.start_game()

    def start_game(self):
        move_number = 1
        moves_played = []
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        first_move = random.choice(range(1))
        while move_number <= 9:
            self.print_board(board)
            if move_number % 2 == first_move:
                move = self.tree.best_move(100, moves_played)
                moves_played.append(move)
            else:
                while True:
                    print("ENTER A MOVE (TL, TC, TR, CL, CC, CR, BL, BC, BR)")
                    move = input()
                    if move in self.tree.move_list:
                        moves_played.append(move)
                        break
                    else:
                        print("INVALID MOVE. TRY AGAIN.")
            move_number += 1

    def play(self):
        self.loop()
