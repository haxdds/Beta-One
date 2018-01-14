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

    def print_board(self, moves_played):
        board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        [self.tree.set_board_value(board, int(x/3), x%3, "X" if index%2 is 0 else "O") for (x, index) in zip([MOVES_INDEX[k] for k in moves_played], range(moves_played.__len__()))]
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
        first_move = 1
        while move_number <= 9:
            self.print_board(moves_played)
            if move_number % 2 == first_move:
                print("BETA ONE's TURN")
                move = self.tree.best_move(5000, moves_played)
                moves_played.append(move)
            else:
                while True:
                    print("YOUR TURN\nENTER A MOVE (TL, TC, TR, CL, CC, CR, BL, BC, BR)")
                    move = input()
                    if move in self.tree.move_list:
                        moves_played.append(move)
                        break
                    else:
                        print("INVALID MOVE. TRY AGAIN.")
            res = self.tree.position_result(moves_played)
            if res in (WIN, LOSS, DRAW):
                if res == WIN:
                    print("YOU WON\n\n\n")
                elif res == LOSS:
                    print("YOU SUCK BOI\n\n\n")
                else:
                    print("DRAW!\n\n\n")
                break
            move_number += 1

    def play(self):
        self.loop()
