import pickle

TREE_FILE = "TicTacToeTree.bin"


def write_tree(tree):
    with open(TREE_FILE, "wb") as f:
        dump = pickle.dump(tree, f, pickle.HIGHEST_PROTOCOL)


def read_tree():
    try:
        with open(TREE_FILE, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None


def fetch():
    tree = read_tree()
    return tree


def persist(tree):
    write_tree(tree)