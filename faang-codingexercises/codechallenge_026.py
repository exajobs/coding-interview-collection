'''
Date: 01/08/2019

Problem description:
====================
This problem was asked by Dropbox.
Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, and at each tick, the following rules apply:
	Any live cell with less than two live neighbours dies.
	Any live cell with two or three live neighbours remains living.
	Any live cell with more than three live neighbours dies.
	Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.
Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.
You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).


Forethoughts:
============
Any puzzle having to do with matrix (i.e. board games) will require manually tracing
at first hand.  This gives you a chance to visually approach and stratezige a more 
clever algorithm.  You will find that adjacency can be grouped by identifying the 
squares surrounding the current coordinate.


Algorithm:
=========
Input: Rows, Columns, ticks
Output: Matrix at each sequence in 0 to nth tick
Psuedo code:
1.  Check for valid input
2.  Create a function to initilize the board with '*'
3.  Create function neighbor_life_signs()
    Check neighbors from cur_row-1 to cur_row+1 and cur_col-1 to cur_col+1
    return total number of alive cells      
4.  Create a function to return 1 if you're alive and 0 otherwise
5.  Create a generator that yields 
    - the initialized board,
    - the board after each tick (each loop)
6.  Create a function to print out the board
'''

from __future__ import print_function
import sys
#
# Initialize board with '*'
#
def init_board(rows, cols):
    return [ ['*'] * cols for _ in range(rows)]


#
# print board layout
#
def print_board(Board, tick_count):
    print("Board layout at tick count: {}.".format(tick_count))
    for i in range(len(Board)):
        for j in range(len(Board[i])):
            print(" {} ".format(Board[i][j]), end='|') 
        print("\n")


#
# Return count of life_signs from adjacent cells
#
def neighbor_life_signs(Board, row, col):
    life_cnt = 0

    start_row_idx = row-1
    end_row_idx = row+2
    start_col_idx = col-1
    end_col_idx = col+2

    for r in range(start_row_idx, end_row_idx, 1):
        for c in range(start_col_idx, end_col_idx, 1):
            try:
                if (r>=0 and r<=len(Board)) and(c>=0 and c<=len(Board)):
                    if Board[r][c] == '*':
                        #print("DBUG-- row,col:{},{}=={}".format(r,c, Board[r][c]))
                        life_cnt += 1
            except IndexError:
                continue
    return life_cnt


#
# feel my own pulse
# return 1 if alive 0 if dead
#
def my_life_sign(Board, row, col):
    return 1 if Board[row][col] == '*' else 0


#
# generate board at initialization
# and update board after each tick
#
def board_gen(*args):
    ticks = args[2]
    tick_count = 0
    Board = init_board(args[0], args[1])

    yield Board # yield the initialized board on the first iteration

    while tick_count < ticks:
        for i in range(len(Board)):
            for j in range(len(Board[i])):
                life_count = neighbor_life_signs(Board, i, j) - int(my_life_sign(Board, i, j))

                ##
                # Note: There might be a chicken-n-egg issue here
                ##
                if Board[i][j] == '*':
                    #Any live cell with less than 2 or more than three live neighbours dies.
                    if life_count < 2 or life_count > 3:
                        Board[i][j] = '.'
                    #Any live cell with 2 or 3 live neighbors remains alive.  
                    #Ahh, but we don't even need to check it here
                    if life_count == 3 or life_count == 2:
                        Board[i][j] = '*'

                #Any dead cell with exactly three live neighbours becomes a live cell.
                elif Board[i][j] == '.' and life_count == 3:
                    Board[i][j] = '*'

        yield Board  #yield the Board at each tick
        tick_count += 1

    
#
# Altogether now!
#
def determine_mortality(rows=5, cols=5, ticks=5):
	# validate input  
    try:
        rows = int(rows)
        cols = int(cols)
        ticks = int(ticks)
    except:
        rows = cols = ticks = 5
	
    if rows <= 0 or cols <= 0 or ticks < 0:
        print("Invalid input.  Please provide rows, coloumns and number of iterations")

    iterB = board_gen(rows,cols,ticks)
    print("Test1:\nGiven board with dimension of {} by {}, and number of ticks: {}.".format(rows, cols, ticks))
    for i,board in enumerate(iterB):
        print_board(board,i)

# 
# test neighbor's life sign
#
def neighbor_life_sign_test():
    Board = init_board(6,6)
	# test edge cases (four corners of the board)
    print("neighbor's lifesign count at (0,0) is {}".format(neighbor_life_signs(Board, 0,0)))
    print("neighbor's lifesign count at (5,5) is {}".format(neighbor_life_signs(Board, 5,5)))
    print("neighbor's lifesign count at (0,5) is {}".format(neighbor_life_signs(Board, 0,5)))
    print("neighbor's lifesign count at (5,0) is {}".format(neighbor_life_signs(Board, 5,0)))
	# and an arbitrary point
    print("neighbor's lifesign count at (2,2) is {}".format(neighbor_life_signs(Board, 2,2)))



if __name__ == '__main__':
    # run with commandline arguments.
    # e.g. python codechallenge_026.py 10 10 5
    # if nothing passed from commandline, the denerator will use defaults of 5 5 5
    determine_mortality(*sys.argv[1:])


'''
Run-time output:
===============
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_026.py
Test1:
Given board with dimension of 5 by 5, and number of ticks: 5.
Board layout at tick count: 0.
 * | * | * | * | * |

 * | * | * | * | * |

 * | * | * | * | * |

 * | * | * | * | * |

 * | * | * | * | * |

Board layout at tick count: 1.
 * | . | . | . | * |

 . | . | . | . | * |

 * | . | . | . | * |

 . | . | . | . | * |

 . | . | . | * | * |

Board layout at tick count: 2.
 . | . | . | . | . |

 . | . | . | . | . |

 . | . | . | . | . |

 . | . | . | * | * |

 . | . | . | * | * |

Board layout at tick count: 3.
 . | . | . | . | . |

 . | . | . | . | . |

 . | . | . | . | . |

 . | . | . | * | * |

 . | . | . | * | * |

Board layout at tick count: 4.
 . | . | . | . | . |

 . | . | . | . | . |

 . | . | . | . | . |

 . | . | . | * | * |

 . | . | . | * | * |

Board layout at tick count: 5.
 . | . | . | . | . |

 . | . | . | . | . |

 . | . | . | . | . |

 . | . | . | * | * |

 . | . | . | * | * |

'''
