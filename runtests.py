"""Run using: py.test runtests.py"""
from board import Board
import player as plyr


def test_board_displays_new_game():
    b = Board()
    display = b.display()
    expected = ' 1 | 2 | 3 \n'\
               '-----------\n'\
               ' 4 | 5 | 6 \n'\
               '-----------\n'\
               ' 7 | 8 | 9 \n'
    assert display == expected


def test_board_displays_correct_state():
    b = Board(['X', 'O', 3, 'O', 'X', 6, 7, 'X', 'O'])
    display = b.display()
    expected = ' X | O | 3 \n'\
               '-----------\n'\
               ' O | X | 6 \n'\
               '-----------\n'\
               ' 7 | X | O \n'
    assert display == expected


def test_computer_makes_selection():
    b = Board(['X', 'O', 3, 'O', 'X', 6, 7, 'X', 'O'])
    choice = plyr.Computer(b, 'X').choose_play()
    assert choice in ['3', '6', '7']


def test_board_game_not_over():
    b = Board()
    assert b.game_over() is False
