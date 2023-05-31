'''Implements tic tac toe game'''
from board import Board

game = Board()
print(game)
while game.get_status() not in ('x', '0', 'draw'):
    print('Your turn')
    move = input('Input two coordinates in format: x space y\n0<=x<=2\n0<=y<=2\n')
    game.make_move((int(move[0]), int(move[2])), 'x')
    print(game)
    print('Computer\'s turn')
    game.computer_move()
    print(game)
print(f'Winner is {game.get_status()}')
