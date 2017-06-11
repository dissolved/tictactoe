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


def test_computer_makes_selection():
    choice = plyr.Computer('X').choose_play([1, 5, 9])
    assert choice in ['1', '5', '9']
