import random


class Player:
    """A Tic Tac Toe player"""
    def __init__(self, board, mark, name=''):
        self.board = board
        self.mark = mark
        self.name = name

    def choose_play(self):
        choices = self.board.choices() + ['Q']
        prompt_str = 'Enter {}: '.format(', '.join(choices))
        choice = 'none'
        while choice not in choices:
            choice = input(prompt_str).upper()
        return choice

    def prompt(self):
        print('\n{}, where do you wish to put your {}?'.format(
            self.name, self.mark))
        print(self.board.display())
        return self.choose_play()


class Computer(Player):
    """An AI Tic Tac Toe player"""
    def __init__(self, board, mark, level="easy"):
        self.algo = getattr(self, '{}_algo'.format(level))
        super(Computer, self).__init__(board, mark, 'Computer')

    def choose_play(self):
        choice = self.algo()
        print('{} chooses {}'.format(self.name, choice))
        return choice

    def easy_algo(self):
        return str(random.choice(self.board.choices()))

    def hard_algo(self):
        pass
