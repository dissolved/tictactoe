import random


class Player():
    """docstring for Player"""
    def __init__(self, name, mark, computer=False):
        self.name = name
        self.mark = mark
        self.computer = computer

    def choose_play(self, choices):
        choice = 'none'
        if self.computer:
            choice = str(random.choice(choices))
            print('{} chooses {}'.format(self.name, choice))
        else:
            human_choices = choices + ['Q']
            prompt_str = 'Enter {}: '.format(', '.join(human_choices))
            choice = 'none'
            while choice not in human_choices:
                choice = input(prompt_str).upper()
        return choice

    def prompt(self, board):
        print('\n{}, where do you wish to put your {}?'.format(
            self.name, self.mark))
        print(board.display())
        return self.choose_play(board.open_cells())
