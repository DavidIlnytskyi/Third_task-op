'''Represents board for tic-tac-toe game'''
from btree import BinaryTree
from btnode import Node


class Board():
    '''Represents a board in tic-tac-toe'''
    def __init__(self):
        self.board = [['' for i in range(3)] for i in range(3)]
        self.previous_player = None

    def make_move(self, position, turn):
        '''Takes user move'''
        if self.board[position[0]][position[1]] != '':
            raise KeyError('This position is already used')
        self.board[position[0]][position[1]] = turn
        self.previous_player = turn

    def __str__(self):
        '''Returns str representation of a board'''
        return (f'{self.board[0]}\n{self.board[1]}\n{self.board[2]}')

    def computer_move(self):
        '''Computes move by a tree'''
        pass

    def get_status(self):
        '''Returns status of a board'''
        for row in self.board:
            if row[0] == row[1] == row[2] != '':
                return row[0]

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                return self.board[0][col]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return self.board[0][2]

        if len([turn for lst in self.board for turn in lst if turn != '']) == 9:
            return 'draw'
        return 'continue'

    def get_available_moves(self):
        '''Returns available moves on a board'''
        return sorted([(row, col) for row in range(3) \
                       for col in range(3) if self.board[row][col] == ''], \
                        key = lambda cord: (cord[0], cord[1]))

    def clone_board(self):
        '''clones board'''
        res = Board()
        for cord in [(row, col, self.board[row][col]) \
                     for row in range(3) for col in range(3) if self.board[row][col] != '']:
            res.board[cord[0]][cord[1]] = cord[2]
        res.previous_player = self.previous_player
        return res

if __name__ == "__main__":
    brd = Board()
    brd.make_move((1, 1), 'x')
    tree = BinaryTree()
    tree.build_tree(tree.root, brd)
    tree.check()
    print(brd)
    print(brd.get_status())
    print(brd.clone_board())
