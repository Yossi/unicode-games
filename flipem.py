#!/usr/bin/python

#import readline # Allow command-line style user input in *nix. windows doesnt have this module.
from operator import and_ # Useful and operator.
import copy
from functools import reduce

# Default maximum board size.
MAX_SIZE = 40

# Presentation.
OFF_CHAR = 'o'
ON_CHAR  = 'x'
GET_CHAR = lambda b: b and ON_CHAR or OFF_CHAR

# Messages.
SIZE_MSG  = 'Board size'
ROW_MSG   = 'Row'
COL_MSG   = 'Column'
PROMPT    = lambda s: s + ' > '

SCORE_MSG = 'Score:'
WIN_MSG   = 'You Win!'
BYE_MSG   = 'Goodbye'

HIGH_MSG  = 'You\'ve gone a little too far.'
NEG_MSG   = 'You need to be a more positive person.'
DEC_MSG   = 'Decimal numbers only.'
VALID_MSG = lambda i: 'Valid range: 1 .. ' + str(i)
NOT_VALID = lambda s, i: s + ' ' + VALID_MSG(i)

# Exit keywords.
EXITS = ('quit', 'exit', 'q')
MOVES = ('moves', 'm', 'show')

class Game(object):
    def __init__(self):
        self.aborted = False

    def run(self):
        while not (self.aborted or self.win()):
            self.display()
            self.flip(*self.get())
        self.end()

    def quit(self):
        self.aborted = True

class Flipem(Game):
    def __init__(self):
        Game.__init__(self)
        self.size = self.__in(SIZE_MSG, MAX_SIZE)
        self.span = range(self.size)
        self.board = [[False for x in self.span] for y in self.span]
        self.moves = copy.deepcopy(self.board)
        self.score = 0

    def win(self):
        return reduce(and_, (reduce(and_, row) for row in self.board))

    def display(self):
        for line in (' '.join(map(GET_CHAR, row)) for row in self.board):
            print(line)
        print(SCORE_MSG, str(self.score))
        
    def displayMoves(self):
        for line in (' '.join(map(GET_CHAR, row)) for row in self.moves):
            print(line)
        print(SCORE_MSG, str(self.score))

    def get(self):
        return [self.__in(s, self.size) - 1 for s in (ROW_MSG, COL_MSG)]

    def flip(self, x, y):
        for a, b in (x, y), (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
            if reduce(and_, [i >= 0 and i < self.size for i in (a, b)]):
                self.board[a][b] = not self.board[a][b]
        self.score += 1
        self.moves[x][y] = not self.moves[x][y]

    def end(self):
        if self.aborted:
            print(BYE_MSG)
        else:
            self.display()
            print(WIN_MSG)

    def __in(self, msg, maxsize):
        while not self.aborted:
            try:
                input_ = input(PROMPT(msg))
                size = int(input_)
                if size < 1:
                    print(NOT_VALID(NEG_MSG, maxsize))
                elif size > maxsize:
                    print(NOT_VALID(HIGH_MSG, maxsize))
                else:
                    return size
            except (KeyboardInterrupt, EOFError):
                print()
                self.quit()
            except ValueError as e:
                input_ = input_.strip().lower()
                if input_ in EXITS:
                    self.quit()
                elif input_ in MOVES:
                    self.displayMoves()
                else:
                    print(NOT_VALID(DEC_MSG, maxsize))
        return 0

if __name__ == '__main__':
    Flipem().run()
