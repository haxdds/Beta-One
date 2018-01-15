from Bilawal.TicTacToeTree import TicTacToeMCTS
from Bilawal.Utils import fetch, persist
from Bilawal.TicTacToeGame import TicTacToeGame


def create_tree():
    tree = TicTacToeMCTS()
    tree.search(50000)
    print(tree)
    persist(tree)

def play_game():
    game = TicTacToeGame()
    game.play()

if __name__ == '__main__':
    play_game()
    #create_tree()


