import random
import math


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


class MonteCarloTree:

    def __init__(self, move_list):
        self.root = Node(None)
        self.move_list = move_list
        self.move_set = {move: True for move in move_list}
        self.move_order = []

    def ucb1(self, parent_node, child_node):
        if child_node.total is 0:
            return math.inf
        return ((child_node.score * 1.0) / child_node.total) + 2.0 * math.sqrt(math.log(parent_node.total) / child_node.total)

    def selection(self):
        temp_node = self.root
        while True:
            if temp_node.children.__len__() is 0:
                break
            children_ucb1_values = [self.ucb1(x) for x in temp_node.children]
            temp_node = temp_node.children[children_ucb1_values.index(max(children_ucb1_values))]
            self.move_set[temp_node.move] = False
            self.move_order.append(temp_node.move)
        return temp_node

    def expansion(self, node):
        if node.total is 0:
            return node
        else:
            [node.add_child(Node(move)) for move in [yfuyfyuself.move_set]]
            return random.choice(node.children)

    def simulation(self, node):
        pass

    def back_propagation(self):
        pass

    def search(self, num_iterations):
        for i in range(num_iterations):
            self.move_set = {move: True for move in self.move_list}
            self.move_order = []
            selected_node = self.selection()
            selected_node = self.expansion(selected_node)

        pass



