'''
Date: 12/22/2018

Problem description:
===================
This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board.
Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number
of steps required to reach the end coordinate from the start. If there is no possible path,
then return null. You can move up, left, down, and right. You cannot move through walls.
You cannot wrap around the edges of the board.

  Board = [[F,F,F,F], [T,T,F,F], [F,F,F,F], [F,F,F,F]]
    0   1   2   3
  +----------------
0 | F | F | F | F |
  +----------------
1 | T | T | F | F |
  +----------------
2 | F | F | F | F |
  +----------------
3 | F | F | F | F |
  +----------------

and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps
required to reach the end is 7, since we would need to go through (1, 2) because there
is a wall everywhere else on the second row.


Forethoughts:
============
1.  Construct a dictionary {"up":"?", "down":"?", "right":"?", "left":"?"} to determine
    possible moves from current position.
2.  Ask, is end_row above or below current row?
    is end_column right or left of current collumn?
    i.e. Priority move is alway toward the end coordinate, 
    secondary move is when priority move is blocked.
    example: end(x0, y0) - start(x1,y1) ==>
    x1 - x0 == (3 - 0) = 3 means 3 moves in the virtical direction
    y1 - y0 == (0 - 0) = 0 means 0 moves in the horizontal direction necessary.
    We deduce the virtical movement takes priority in finding the end point.

Algorithm:
==========
Input: matrix of integer
Output: an integer value
Pseudo code:
1.  Re-assign data meaning for better programming flow.  F == True. T  == False 
3.  Determine the direction toward end point.  Use it to go up/down, right/left 
    i.e. Virtical = (-1 if end_row - start_row < 0 else 1)
         Horizontal = (-1 if end_col - start_col < 0 else 1)
    If direction is zero, then use arbitrary move and keep track of back-track logic
2.  Write asubfunction to look two steps ahead in the specified derection.
3.  Write a main function gotoEndPoint()
    2 ways to move toward end point: virtical(row) or horizontal(column).
    Logically we seek virtical move first, if blocked, then try horizontal move, 
    then back to trying virtical move.
4.  Rule of movement: always seek to reduce distance from the end point.
'''


import pytest
# re-assign meaning of data so the logic can easily flow
F = True    # you can pass
T = False   # you shall not pass


#
# check if endpoint is not in the wall
#
def isEndpointApproachable(DBoard, endpos):
    try:
        return DBoard[endpos[0]][endpos[1]]
    except TypeError:
        return False
    except KeyError:
        return False
    except IndexError:
        return False

#
# check if specified row is not a complete wall    
#
def isPassableRow(DBoard, row):
    passingcnt=0
    for val in DBoard[row]:
        if val == T:            #val==True
            passingcnt+=1
    #print("DBUG: cnt:{} len:{}".format(passingcnt, len(DBoard[row])))
    if passingcnt == len(DBoard[row]):
        return False
    else:
        return True 


#
# looking ahead for two virtical moves via direction
#
def peekTwoVirticalSteps(Board, row, col, direction):
    one, two = False, False
    try: 
        one = Board[row+(1*direction)][col]
    except KeyError:
        pass
    except IndexError:
        pass
    except TypeError:
        pass
    try: 
        two = Board[row+(2*direction)][col]
    except KeyError:
        pass
    except IndexError:
        pass
    except TypeError:
        pass

    return one, two

#
# looking ahead for two horizonal moves vir direction
#
def peekTwoHorizontalSteps(Board, row, col, direction):
    one, two = False, False
    try: 
        one = Board[row][col+(1*direction)]
    except KeyError:
        pass
    except IndexError:
        pass
    except TypeError:
        pass
    try: 
        two = Board[row][col+(2*direction)]
    except KeyError:
        pass
    except IndexError:
        pass
    except TypeError:
        pass

    return one, two


#
# Let's walk the talk.
#
def gotoEndPoint(Board, startpos, endpos):
    minSteps = 0
    # Convert matrix into hash table so we can catch KeyError, IndexError 
    # when traversing the dictionary
    DBoard = dict()   # hash table for Board
    for i in range(len(Board[-1])):
        item = {i:Board[i]}
        DBoard.update(item)

    rows = len(Board[:])
    cols = len(Board[-1])
    cur_row = startpos[0]
    cur_col = startpos[1]
    end_row = endpos[0]
    end_col = endpos[1]
    debug_path = ""   
    virtical_direction = (-1 if (end_row - cur_row) < 0 else 1)
    horizontal_direction = (-1 if (end_col - cur_col) < 0 else 1)

    #print("DBUG: endpos is {}".format(DBoard[end_row][end_col]))
    #print("DBUG: virtical_direction={} horizontal_direction:{}".format(virtical_direction, horizontal_direction))

    # is there a blocking wall on the way?
    # i.e. all elements in the row are T's
    for row in range(cur_row-1, end_row-1, -1):
        if isPassableRow(DBoard, row) == False:
            print("Found impenetrable wall blocking endpoint.")
            return None

    # is endpos passable. ie. endpos in not blocked
    if isEndpointApproachable(DBoard,endpos) is not F: 
        print("Endpoint is in the wall.  Impassable!")
        return None
    else:
        # let's go.  We know we can get to the endpos  

        # First, virtical moves:
        while True:
            # sentry goes here
            if cur_row == end_row:
                #debug_path += " -> ({},{})".format(cur_row, cur_col)   
                break

            step_one, step_two = peekTwoVirticalSteps(DBoard, cur_row, cur_col, virtical_direction)
            #print("DBUG--Virtical Step_1:{} Step_2:{}".format(step_one, step_two))
            if step_one:
                debug_path += " -> ({},{})".format(cur_row, cur_col)   
                cur_row = cur_row + (1 * virtical_direction)
                minSteps+=1 
            else:
                side_step_one, side_step_two = peekTwoHorizontalSteps(DBoard, cur_row, cur_col, horizontal_direction)
                if side_step_one:
                    debug_path += " -> ({},{})".format(cur_row, cur_col)   
                    cur_col = cur_col + (1 * horizontal_direction)
                    minSteps+=1 

        # Second, Horizontal moves
        horizontal_direction = [-1 if (end_col - cur_col) < 0 else 1][0] 
        while True:
            # sentry goes here
            if cur_col == end_col:
                debug_path += " -> ({},{})".format(cur_row, cur_col)   
                break

            step_one, step_two = peekTwoHorizontalSteps(DBoard, cur_row, cur_col, horizontal_direction)
            #print("DBUG--Horizontal Step_1:{} Step_2:{}".format(step_one, step_two))
            if step_one:
                debug_path += " -> ({},{})".format(cur_row, cur_col)   
                cur_col = cur_col + (1 * horizontal_direction)
                minSteps+=1 


        print(debug_path)
        return minSteps


def test_code():
    Board = [[F,F,F,F], [T,T,F,F], [F,F,F,F], [F,F,F,F]]
    start = (3,0) #tuple start[3][0]
    end = (0,0)   #tuple end[0][0]
    rows = len(Board[:])
    cols = len(Board[-1])
    assert gotoEndPoint(Board, start, end) == 7
    end = (3,3)   #tuple end[3][3]
    assert gotoEndPoint(Board, start, end) == 3
    
if __name__ == '__main__':
    Board = [[F,F,F,F], [T,T,F,F], [F,F,F,F], [F,F,F,F]]
    start = (3,0) #tuple start[3][0]
    end = (3,3)   #tuple end[3][3]
    rows = len(Board[:])
    cols = len(Board[-1])


    print("Start pos:{}".format(start))
    print("End pos:{}".format(end))
    print("Board layout:")
    for i in range(rows):
        for j in range(cols):
            print("({}, {}):{}".format(i,j,Board[i][j]))

    minSteps = gotoEndPoint(Board, start, end)
    print("Minimum number of steps to reach the end position is {}".format(minSteps))


'''
Run-time output:
================
markn@raspberrypi3:~/devel/py-src/DailyCodeChallenge $ python codechallenge-11.py
Start pos:(3, 0)
End pos:(0, 0)
Board layout:
(0, 0):True
(0, 1):True
(0, 2):True
(0, 3):True
(1, 0):False
(1, 1):False
(1, 2):True
(1, 3):True
(2, 0):True
(2, 1):True
(2, 2):True
(2, 3):True
(3, 0):True
(3, 1):True
(3, 2):True
(3, 3):True
 -> (3,0) -> (2,0) -> (2,1) -> (2,2) -> (1,2) -> (0,2) -> (0,1) -> (0,0)
Minimum number of steps to reach the end position is 7

markn@raspberrypi3:~/devel/py-src/DailyCodeChallenge $ pytest codechallenge-11.py
=================================== test session starts ====================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodeChallenge, inifile:
collected 1 item

codechallenge-11.py .                                                                [100%]

================================= 1 passed in 0.03 seconds =================================
'''
