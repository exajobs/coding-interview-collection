'''
Date: 01/03/2019

Problem description:
====================
This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of 
the array so that all the Rs come first, the Gs come second, and the Bs come last. 
You can only swap elements of the array.

Do this in linear time and in-place.
For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], 
it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].


(*) Wow! google asked an easy question for a chance...

Algorithm:
==========
Input: An list of 'R's, 'G's, and 'B's
Output: Segregated Rs, Gs, Bs in that order
Psuedo code:
1.  Check for valid input
2.  return the grouped R's + grouped G's + grouped B's
'''

def segListOfRGB(arr):
	return [r for r in arr if r == 'R'] + [g for g in arr if g == 'G'] + [b for b in arr if b == 'B']

def test_code():
	A = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
	assert segListOfRGB(A) == ['R', 'R', 'R', 'G', 'G', 'B', 'B']

if __name__ == '__main__':
	A = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
	print("Test1\nInput: {}".format(A))
	print("Output: {}".format(segListOfRGB(A)))
	

'''
Run-time output:
===============

linux1@sles12sp3:/data/devel/py-src/DailyCodingChallenge> python codechallenge_020.py
Test1
Input: ['G', 'B', 'R', 'R', 'B', 'R', 'G']
Output: ['R', 'R', 'R', 'G', 'G', 'B', 'B']
'''
