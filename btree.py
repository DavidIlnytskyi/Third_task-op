'''Implements Binary Tree'''
from btnode import Node

class BinaryTree():
    '''Binary tree'''
    def __init__(self):
        self.root = Node()
        self.result_left = 0
        self.result_right = 0


    def build_tree(self, root, board):
        '''Builds a tree'''
        if board.get_status() == 'x':
            pass
        elif board.get_status() == '0':
            pass
        elif board.get_status() == 'draw':
            pass
        else:
            if len(board.get_available_moves()) < 2:
                return
            if len(board.get_available_moves()) > 2:
                root.left = Node(board.get_available_moves()[0])
                root.left.brd = board.clone_board()
                if root.left.brd.previous_player == 'x':
                    root.left.brd.make_move(root.left.turn_cord, 'o')
                else:
                    root.left.brd.make_move(root.left.turn_cord, 'x')

                if len(board.get_available_moves()) != 2:
                    self.build_tree(root.left, root.left.brd)

                root.right = Node(board.get_available_moves()[1])
                root.right.brd = board.clone_board()
                if root.right.brd.previous_player == 'x':
                    root.right.brd.make_move(root.right.turn_cord, 'o')
                else:
                    root.right.brd.make_move(root.right.turn_cord, 'x')

                if len(board.get_available_moves()) != 2:
                    self.build_tree(root.right, root.right.brd)

    def check(self, root):
        '''Checks better move'''
        def recursive(self, root):
            if root.left is not None:
                if root.left.brd.get_status() == 'x':
                    if left:
                        self.result_left += 1
                    else:
                        self.result_left += 1
                elif root.left.brd.get_status() == '0':
                    if left:
                        self.result_left -= 1
                    else:
                        self.result_right -= 1
                elif root.left.brd.get_status() == 'draw':
                    pass
                else:
                    recursive(self, root.left)
            if root.right is not None:
                if root.right.brd.get_status() == 'x':
                    if left:
                        self.result_left += 1
                    else:
                        self.result_right += 1
                elif root.right.brd.get_status() == '0':
                    if left:
                        self.result_left -= 1
                    else:
                        self.result_right -= 1
                elif root.right.brd.get_status() == 'draw':
                    pass
                else:
                    recursive(self, root.right)

        left = True
        recursive(self, root)
        left = False
        recursive(self, root)
