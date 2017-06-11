from itertools import cycle
from board import Board
import player as plyr


def print_header():
    print('------------------------------------------------------------------')
    print('--------------------- WELCOME TO TIC-TAC-TOE ---------------------')
    print('------------------------------------------------------------------')


def get_players(board):
    x = plyr.Player(board, 'X', 'Human')
    o = plyr.Computer(board, 'O')
    return (x, o)


def play_tic_tac_toe():
    board = Board()
    players = get_players(board)
    for player in cycle(players):
        choice = player.prompt()
        if choice == 'Q':
            print("Are we quitting while we're ahead?")
            return
        else:
            board.play(choice, player.mark)

        winner = board.winner()
        if winner:
            board.display()
            print('{} wins! Congrats {}!!!'.format(winner, player.name))
            break

        if not board.choices():
            board.display()
            print('Nobody wins... The only winning move is not to play.')
            break


if __name__ == '__main__':
    print_header()
    play_tic_tac_toe()
