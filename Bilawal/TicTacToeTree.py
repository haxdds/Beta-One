from Bilawal.MCTS import MonteCarloTree, WIN, LOSS, DRAW, NEITHER
import numpy as np

MOVES = ["TL", "TC", "TR", "CL", "CC", "CR", "BL", "BC", "BR"]
MOVES_INDEX = {move: index for (move, index) in zip(MOVES, range(MOVES.__len__()))}
MOVE_X = 1
MOVE_O = -1


class TicTacToeMCTS(MonteCarloTree):

    def __init__(self):
        super().__init__(MOVES)

    def set_board_value(self, board, x, y, value):
        board[x][y] = value

    def position_result(self, moves_played):
        board = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        [self.set_board_value(board, int(x/3), x%3, MOVE_X if index%2 is 0 else MOVE_O) for (x, index) in zip([MOVES_INDEX[k] for k in moves_played], range(moves_played.__len__()))]
        #print(board)
        row_sums = board.sum(axis=1)
        col_sums = board.transpose().sum(axis=1)
        diag_sums = np.array([board.diagonal().sum(), board[::-1].diagonal().sum()])
        all_sums = np.hstack((row_sums, col_sums, diag_sums)).ravel()
        if 3 in all_sums:
            return WIN
        elif -3 in all_sums:
            return LOSS
        elif moves_played.__len__() == 9:
            return DRAW
        else:
            return NEITHER

    def best_move(self, num_iterations, moves_played):
        self.search_from_node(num_iterations, moves_played)
        return self.choose_best_move(moves_played)






