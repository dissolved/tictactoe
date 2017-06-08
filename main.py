from collections import namedtuple
from itertools import cycle
from board import Board

Player = namedtuple('Player', 'name, mark')


def print_header():
    print('------------------------------------------------------------------')
    print('--------------------- WELCOME TO TIC-TAC-TOE ---------------------')
    print('------------------------------------------------------------------')


def prompt_player(player, board):
    print('\n{}, where do you wish to put your {}?'.format(*player))
    board.display()
    choice = 'none'
    valid_choices = board.open_cells() + ['Q']
    prompt_str = 'Enter {}: '.format(', '.join(valid_choices))
    while choice not in valid_choices:
        choice = input(prompt_str).upper()
    return choice


def get_players():
    x = Player(input("Who will play X's? "), 'X')
    o = Player(input("Who will play O's? "), 'O')
    return (x, o)


def play_tic_tac_toe():
    players = get_players()
    board = Board()
    for player in cycle(players):
        choice = prompt_player(player, board)
        if choice == 'Q':
            break
        else:
            board.play(choice, player.mark)

        winner = board.winner()
        if winner:
            board.display()
            print('{} wins! Congratulations!!!'.format(winner))
            break

        if not board.open_cells():
            board.display()
            print('Nobody wins... The only winning move is not to play.')
            break


if __name__ == '__main__':
    print_header()
    play_tic_tac_toe()
