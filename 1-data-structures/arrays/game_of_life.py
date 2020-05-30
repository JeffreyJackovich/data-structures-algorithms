'''
4 rules to implement the 'game of life'

1. If a cell is alive and has either two or three live neighbors, the cell remains alive in the next generation.
    The neighbors are the eight cells immediately surrounding a cell: vertically, horizontally, and diagonally.

2. A living cell that has no live neighbors or a single live neighbor dies from isolation in the next generation.

3. A living cell that has four or more live neighbors dies from overpopulation in the next generation.

4. A dead cell with exactly three live neighbors results in a birth and becomes alive in the next generation.
    All other dead cells remain dead in the next generation.

The game uses an infinite-sized rectangular grid of cells in which each cell is either empty or occupied by an organism.
The occupied cells are said to be alive, whereas the empty ones are dead.

[
[None, None, None],
[1, 1, 1],
[None, None, None]
]

(col, row) -> (0, 1) , (1,1), (2, 1)
'''
# initial configuration
NUM_COLS = 3
NUM_ROWS = 3
# dead vs live cells vs blank
DEAD = "0"
LIVE = "1"
BLANK = None
# number of generations
NUM_GENERATIONS = 4

class GameOfLife:

    def __init__(self, num_cols, num_rows):
        '''creates the 2-d matrix'''
        self.matrix = []

        for j in range(num_rows):
            #create one first row
            row = []
            for i in range(num_cols):
                row.append(BLANK)
            self.matrix.append(row)

    def get_initial_setup(self):
        ''''''
        row = 1
        pass

    def set_cell(self, new_val):
        '''chaning the cell value'''
        cell = self.get_cell()
        pass

    def get_cell(self, col_idx, row_idx):
        '''returns a cell specific cell'''
        return self.matrix[col_idx][row_idx]

    def __repr__(self):
        return str(self.matrix)


gol = GameOfLife(NUM_COLS, NUM_ROWS)
print(gol)

'''
input:
  x = 9, n = 2

output:
  3


3^2 = 9


import math
def nth_root(num,root)
   answer = num ** (1/root) 
   return answer

if ans**n > x:
elif ans**n < x:

'''
import math


def nth_root(num, root):
    answer = num ** (1 / root)
    return answer


def root(x, n):
    # guess the result by checking and consider binary search
    approx_ans = (x + n) / 2.0

    while abs(approx_midpoint - root(x, n)) > 0.001:
        # maintain upper and lower boun
        upper = x
        lower = 0

        if approx_ans ** n > x:
            upper = approx_ans

        elif approx_ans ** n < x:
            lower = approx_ans