from random import randint


class Board:

    def __init__(self):
        self.board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

    def print(self):
        print("\n")
        for i in range(0, 3):
            print(self.board[3*i] + " " + self.board[3*i+1] + " " + self.board[3*i+2])

    def place(self, pos, val):
        if pos < 0 or pos > 8:
            print("\ninvalid position")
            return
        if val != 'X' and val != 'O':
            print("\ninvalid value")
            return
        if not self.can_place(pos):
            print("\nalready placed here")
            return
        self.board[pos] = val

    def can_place(self, pos):
        return not (self.board[pos] == 'X' or self.board[pos] == 'O')

    def clone(self):
        b = Board()
        for i in range(0,9):
            b.board[i] = self.board[i]
        return b


class Game:

    def __init__(self):
        self.board = Board()
        self.winner = 'null'
        self.running = True
        self.xturn = True
        self.moves = 0

    def run(self):
        while self.running:
            if self.xturn:
                pos = Engine().choice(self.board)
                self.board.place(int(pos), 'X')
                self.xturn = False
                self.moves += 1
            else:
                pos = Engine().choice(self.board)
                self.board.place(int(pos), 'O')
                self.xturn = True
                self.moves += 1
            self.check_winner()
            self.board.print()
        print("\nmoves: \b")
        print(self.moves)

    def check_winner(self):
        if self.win('X'):
            self.winner = 'X'
            print("\nX WINS!")
            self.running = False
        if self.win('O'):
            self.winner = 'O'
            print("\nO WINS!")
            self.running = False
        if self.moves >= 9:
            if self.winner == 'null':
                print("\nTIE!")
                self.running = False

    def win(self, char):
        cell = self.board.board
        return cell[0] == cell[1] == cell[2] == char or \
               cell[3] == cell[4] == cell[5] == char or \
               cell[6] == cell[7] == cell[8] == char or \
               cell[0] == cell[3] == cell[6] == char or \
               cell[1] == cell[4] == cell[7] == char or \
               cell[2] == cell[5] == cell[8] == char or \
               cell[0] == cell[4] == cell[8] == char or \
               cell[2] == cell[4] == cell[6] == char


class Engine:

    @staticmethod
    def choice(board):
        done = False
        while not done:
            choice = randint(0, 8);
            if board.can_place(choice):
                done = True

        return choice


g = Game()
g.run()

print("\n\nCLONE\n\n")
g.board.clone().print()




