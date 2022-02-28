'''
Date: 02/04/2019

Task description:
================
This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
For example, given the following matrix:
[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:
1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12



Forethought:
===========
The spiralling elements in the 2D matrix could be devided into four quadrants.  
Keep the order of the vertex and assemble rows, columns from each quadrant as tuples.
Mind the overlappping elements at each corner/edge.

^------->
| \ F  /|
|  \  / |
|U  \/ D|
|   /\  | 
|  /  \ |
| / B  \|
<-------v 

F == Forward quadrant
D == Downward quadrant
B == Backward quadrant
U == Upward quadrant

Algorithm:
=========
1.  Validate input
2.  Write sub functions to return elements for each quadrant
3.  Assemble all four quadrants in the clockwise direction
4.  Return elements.

'''

def forward_elems(Arr=[]):
    rows = len(Arr)
    cols = len(Arr[0])
    idx = 0
    forwardquadrant = []
    for i in range(cols):
        try:
            f_list = Arr[i][slice(i, cols-i,1)]
            forwardquadrant.append((idx, f_list))
            idx +=4
            print(f_list)
        except IndexError:
            pass
    return forwardquadrant

def downward_elems(Arr=[]):
    rows = len(Arr)
    cols = len(Arr[0])
    idx = 1
    downquadrant = []
    while len(Arr[0]) > 0:
        d_list=[]
        for i in range(rows):
            try:
                d_list.append(Arr[i].pop())
            except IndexError:
                pass
        downquadrant.append((idx, d_list))
        idx +=4
    return downquadrant

def backward_elems(Arr=[]):
    rows = len(Arr)
    cols = len(Arr[0])
    idx = 2
    cnt = 0
    backwardquadrant = []
    for i in range(rows-1, rows//2 - 1, -1):
        try:
            b_list = [elem for j,elem in enumerate(Arr[i]) if j>=cnt and j< cols-cnt]
            cnt +=1
        except IndexError:
            pass
        backwardquadrant.append((idx,b_list[::-1]))
        idx += 4
    return backwardquadrant


def upward_elems(Arr=[]):
    pass

def main():
    Arr = [[1,2,3,4,5,6,7,8],
           [9,10,11,12,13,14,15,16],
           [17,18,19,20,21,22,23,24],
           [25,26,27,28,29,30,31,32],
           [33,34,35,36,37,38,39,40]]
    print(Arr)
    quadrants = list()
    
    #quadrants = forward_elems(Arr) + downward_elems(Arr) + backward_elems(Arr)
    #quadrants = forward_elems(Arr)
    quadrants = downward_elems(Arr) 
    #quadrants = backward_elems(Arr)
    quadrants.sort()
    print(quadrants)

if __name__ == '__main__':
    main()
