import random
import math
from abc import abstractmethod

WIN = 1
LOSS = 2
DRAW = 3
NEITHER = 0

class Node:

    def __init__(self, move):
        self.move = move
        self.children = []
        self.score = 0
        self.total = 0
        self.parent = None

    def add_child(self, node):
        node.parent = self
        self.children.append(node)

    def __str__(self):
        return "({0}, {1}/{2}, numChild={3})".format(self.move, self.score, self.total, self.children.__len__())


class MonteCarloTree:

    def __init__(self, move_list):
        self.root = Node(None)
        self.move_list = move_list
        self.move_set = {move: False for move in move_list}
        self.move_order = []

    def __str__(self):
        temp_nodes = [self.root]
        string = ""
        while temp_nodes.__len__() is not 0:
            line = ""
            new_temp_nodes = []
            for child in temp_nodes:
                line += child.__str__() + " "
                new_temp_nodes += child.children
            temp_nodes = new_temp_nodes
            string += line + "\n"
        return string

    @abstractmethod
    def position_result(self, moves_played):
        # return 1 for win, -1 for loss, 0 for neither
        return 0

    def ucb1(self, child_node):
        parent_node = child_node.parent
        if child_node.total is 0:
            return math.inf
        return ((child_node.score * 1.0) / child_node.total) + 2.0 * math.sqrt(math.log(parent_node.total) / child_node.total)

    def selection(self, node):
        temp_node = node
        while True:
            if temp_node.children.__len__() is 0:
                break
            children_ucb1_values = [self.ucb1(x) for x in temp_node.children]
            temp_node = temp_node.children[children_ucb1_values.index(max(children_ucb1_values))]
            self.move_set[temp_node.move] = True
            self.move_order.append(temp_node.move)
        return temp_node

    def expansion(self, node, update_moves):
        if node.total is 0 and node is not self.root:
            return node
        elif node is self.root and node.total is not 0:
            return node
        else:
            [node.add_child(Node(move)) for move in [move for move in self.move_set.keys() if self.move_set[move] == False]]
            if node.children is None or node.children.__len__() is 0:
                return node
            selected_node = random.choice(node.children)
            if update_moves:
                self.move_set[selected_node.move] = True
                self.move_order.append(selected_node.move)
            return selected_node

    def simulation(self, node):
        # make copy of move order
        moves_list = self.move_order.copy()
        moves_played = self.move_set.copy()
        while True:
            res = self.position_result(moves_list)
            if res in (WIN, DRAW, LOSS):
                self.back_propagation(res, node)
                break
            else:
                # choose random move and continue
                moves_left_to_play = [move for move in moves_played.keys() if moves_played[move] == False]
                next_move = random.choice(moves_left_to_play)
                moves_list.append(next_move)
                moves_played[next_move] = True

    def back_propagation(self, res, node):
        temp_node = node
        while temp_node != None:
            temp_node.total += 1
            if res == WIN:
                temp_node.score += 10
            elif res == DRAW:
                temp_node.score += 0.5
            temp_node = temp_node.parent

    def search(self, num_iterations):
        for i in range(num_iterations):
            self.move_set = {move: False for move in self.move_list}
            self.move_order = []
            selected_node = self.selection(self.root)
            selected_node = self.expansion(selected_node, True)
            self.simulation(selected_node)

    def search_from_node(self, num_iterations, moves_played):
        # build tree to node from moves_played
        temp_node = self.root
        for move in moves_played:
            if temp_node.children.__len__() is 0:
                temp_node = self.expansion(temp_node, False)
            else:
                temp_node = (node for node in temp_node.children if node.move == move).__next__()

        for i in range(num_iterations):
            self.move_set = {move: False for move in self.move_list}
            for move in moves_played:
                self.move_set[move] = True
            self.move_order = moves_played.copy()
            selected_node = self.selection(temp_node)
            selected_node = self.expansion(selected_node, False)
            self.simulation(selected_node)

    def choose_best_move(self, moves_played):
        temp_node = self.root
        for move in moves_played:
            temp_node = (node for node in temp_node.children if node.move == move).__next__()
        children_win_over_plays = [x.score/x.total for x in temp_node.children]
        temp_node = temp_node.children[children_win_over_plays.index(max(children_win_over_plays))]
        return temp_node.move



