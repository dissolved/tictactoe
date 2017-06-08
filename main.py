from collections import namedtuple
from itertools import cycle

Player = namedtuple('Player', 'name, mark')
BOARD = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


def display(board):
    col_str = ' {} | {} | {} '
    row_str = '\n-----------\n'
    print(row_str.join([col_str.format(*row) for row in board]))


def print_header():
    print('------------------------------------------------------------------')
    print('--------------------- WELCOME TO TIC-TAC-TOE ---------------------')
    print('------------------------------------------------------------------')


def prompt_player(player):
    print('\n{}, where do you wish to put your {}?'.format(*player))
    display(BOARD)
    return input('Enter 0-8 or [Q]uit: ')


def get_players():
    x = Player(input("Who will play X's? "), 'X')
    o = Player(input("Who will play O's? "), 'O')
    return (x, o)


def play_tic_tac_toe():
    players = get_players()
    for player in cycle(players):
        choice = prompt_player(player)
        if choice.upper() == 'Q':
            break


if __name__ == '__main__':
    print_header()
    play_tic_tac_toe()
