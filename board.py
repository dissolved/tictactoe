class Board():
    """A Tic-Tac-Toe board.

    Internal representation by 1-dimensional list visualized as:
     0 | 1 | 2
    -----------
     3 | 4 | 5
    -----------
     6 | 7 | 8
    """
    win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                  (0, 3, 6), (1, 4, 7), (2, 5, 8),
                  (0, 4, 8), (2, 4, 6))

    def __init__(self, state=None):
        if state:
            self.board = state
        else:
            self.board = list(range(1, 10))

    def display(self):
        """Display a text representation of the board."""
        representation = '-----------\n'.join([' {} | {} | {} \n']*3)
        return representation.format(*self.board)

    def winner(self):
        """Return mark of winner, if exists, otherwise return None."""
        for cells in Board.win_combos:
            if len(set([self.board[i] for i in cells])) == 1:
                return self.board[cells[0]]

    def choices(self):
        """Return a list of available plays."""
        return [str(i) for i in self.board if type(i) == int]

    def game_over(self):
        """Return True if game is over, otherwise False"""
        return self.winner() or self.choices() == []

    def play(self, cell, mark):
        """Place the mark in the specified cell."""
        self.board[self.board.index(int(cell))] = mark
