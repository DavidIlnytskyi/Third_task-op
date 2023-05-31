'''Implements Binary Tree'''
from btnode import Node

class BinaryTree():
    def __init__(self, board=None):
        self.root = Node()
        self.board = board

    def build_tree(self, root, board):
        if root.board.get_status() == 'continue':
            return None
        elif root.board.get_status() != 'x' and root.board.get_status() != '0':
            self.root.left = Node(board.get_available_moves()[0])
            self.root.left.brd = board.clone_board()
            self.root.left.brd = self.root.left.brd.make_move(board.get_available_moves()[0])
            if len(board.get_available_moves()) != 1:
                self.root.right = Node(board.get_available_moves()[0])
                self.root.right.brd = board.clone_board()
                self.root.right.brd = self.root.left.brd.make_move(board.get_available_moves()[0])