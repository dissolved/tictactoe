import random


class Player:
    """A Tic Tac Toe player"""
    def __init__(self, mark, name=''):
        self.name = name
        self.mark = mark

    def choose_play(self, choices):
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


class Computer(Player):
    """An AI Tic Tac Toe player"""
    def __init__(self, mark, level="easy"):
        self.algo = getattr(self, '{}_algo'.format(level))
        super(Computer, self).__init__(mark, 'Computer')

    def choose_play(self, choices):
        choice = self.algo(choices)
        print('{} chooses {}'.format(self.name, choice))
        return choice

    def easy_algo(self, choices):
        return str(random.choice(choices))
