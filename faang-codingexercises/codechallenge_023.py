'''
Date: 01/06/2019

Problem description:
===================
This problem was asked by Microsoft.

You have an N by N board. Write a function that, given N, returns 
the number of possible arrangements of the board where N queens can 
be placed on the board without threatening each other, i.e. no two 
queens share the same row, column, or diagonal.


Algorithm:
=========
Input: N rows (where N rows = N columns)
Output: Integer representing the number of Queens
Psuedo code:
To maximize the use of real-estate, we want to go extra by placing 
the most number of queens on the given square NxN board.
1.  Check for valid input

2.  Placing the first Queen at (0, N-2) will guarantee each row has a 
    queen.  See the illustration below.

3.  By deviding the board into lower half and upper half, we can place
    queens as follow:

    # bottom half of the board:
    cur_row = 0
    bottom_Queens = [(cur_row, N-2), (cur_row+1, N-2-2), (cur_row+2, N-2-2-2), ...]

    # top half of the board (excluding the top most row):
    cur_row = N//2
    top_queens = [(cur_row, N-1), (cur_row+1, N-1-2), (cur_row+1+1, N-1-2-2),...]

4.  Return number of queens == len(top_queens.append(bottom_queens))
 
    -------------------------
  5 |   | Q |   |   |   |   |
    -------------------------
  4 |   |   |   | Q |   |   |
    -------------------------
  3 |   |   |   |   |   | Q |
================================ 
  2 | Q |   |   |   |   |   |
    -------------------------
  1 |   |   | Q |   |   |   |
    -------------------------
  0 |   |   |   |   | Q |   |
    -------------------------
      0   1   2   3   4   5
'''

from __future__ import print_function
def place_queens(N): 
	queens = list()

	# bottom half of the board
	cur_col = N-2
	for row in range(N//2):
		if cur_col >= 0:
			queens.append((row, cur_col))
			print("(bottom_half)-- row,col:({}, {})".format(row,cur_col))
		cur_col = cur_col - 2	

	# top half of the board
	cur_col = N-1
	for row in range(N//2, N, 1):
		if cur_col >= 0:
			queens.append((row,cur_col))
			print("(top_half)-- row,col:({}, {})".format(row,cur_col))
		cur_col = cur_col - 2	

	Qs = ', '.join(str(q) for q in queens)
	print("Queen_positions = [{}]".format(Qs))
	return len(queens) 

def test_code():
	N = 100
	assert place_queens(N) == N

if __name__ == '__main__':
	N=15
	print("For a {}-by-{} board, we can place queens as follow:".format(N,N))
	number_of_queens = place_queens(N)
	print("Total number of queens:{}".format(number_of_queens))



'''
Run-time output:
===============
For a 15-by-15 board, we can place queens as follow:
(bottom_half)-- row,col:(0, 13)
(bottom_half)-- row,col:(1, 11)
(bottom_half)-- row,col:(2, 9)
(bottom_half)-- row,col:(3, 7)
(bottom_half)-- row,col:(4, 5)
(bottom_half)-- row,col:(5, 3)
(bottom_half)-- row,col:(6, 1)
(top_half)-- row,col:(7, 14)
(top_half)-- row,col:(8, 12)
(top_half)-- row,col:(9, 10)
(top_half)-- row,col:(10, 8)
(top_half)-- row,col:(11, 6)
(top_half)-- row,col:(12, 4)
(top_half)-- row,col:(13, 2)
(top_half)-- row,col:(14, 0)
Queen_positions = [(0, 13), (1, 11), (2, 9), (3, 7), (4, 5), (5, 3), (6, 1), (7, 14), (8, 12), (9, 10), (10, 8), (11, 6), (12, 4), (13, 2), (14, 0)]
Total number of queens:15

======================================= test session starts ========================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_023.py .                                                                       [100%]

===================================== 1 passed in 0.06 seconds =====================================
'''

