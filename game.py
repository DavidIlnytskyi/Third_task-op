'''Implements tic tac toe game'''
from board import Board
move = None
game = Board()
print(game)
while True:
    print('Your turn')
    while True:
        try:
            move = input('Input two coordinates in format: x space y\n0<=x<=2\n0<=y<=2\n')
            if len(move) != 3 or not move[0].isnumeric() or not move[2].isnumeric() or move[1] != ' ':
                raise ValueError()
            game.make_move((int(move[0]), int(move[2])), 'x')
            break
        except (ValueError, KeyError) as e:
            print('Write coordinates as requested')
    if game.get_status() != 'continue':
        print(f'Winner is {game.get_status()}')
        print(game)
        break
    print(game)
    print('Computer\'s turn')
    game.computer_move()
    if game.get_status() != 'continue':
        print(f'Winner is {game.get_status()}')
        print(game)
        break
    print(game)
