'''
Date: 02/07/2019

Task description:
================
This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.


Algorithm:
=========
Input: A list of numbers
Output: A numeric value

Psuedo code:
1.  Validate input
2.  Use while loop with incremental idex as a sentinel.  
    Calculate a cumulative product of 3 consecutive numbers.
3.  Return the largest of the cumulative products

(*) There should be better performance algorithm using numpy. (Will update later) 

'''
import numpy as np



#
# return largest product of any three elements in the list
#
def maxprod(F=[]):
	if len(F) == 0:
		return 0

	if min(F) > 0:
		# all positive numbers, let's sort and reverse
		F.sort()
		F=F[::-1]  # this is now in descending order
		return F[0] * F[1] * F[2]
	else:
		maxp,idx=0,0
		while idx < len(F)-1:
			try:
				prd = np.cumprod(F[idx:idx+3])[-1]
			except IndexError:
				prd = np.cumprod(F[len(F)-1:] + F[0:2])[-1]
			if prd > maxp:
				maxp = prd
			idx+=1
		return maxp


#
# unittest
#
def test_maxprod():
	Arr = [12,4,22,9,5,7,6]
	assert maxprod(Arr) == 2376

	Arr=[0,0,0,100]
	assert maxprod(Arr) == 0

	Arr=[]
	assert maxprod(Arr) == 0
#
# client programm
#
def main():
	Arr = [-10,-10,5,2]
	print("\nTest1:\nGiven a list of numbers: {}\nThe maximum cumulative product of any three numbers is {}.".format(np.array(Arr), maxprod(Arr)))

	Arr = [12,4,22,9,5,7,6]
	print("\nTest2:\nGiven a list of numbers: {}\nThe maximum cumulative product of any three numbers is {}.".format(np.array(Arr), maxprod(Arr)))

	Arr = np.random.random(10)
	print("\nTest3:\nGiven a list of numbers: {}\nThe maximum cumulative product of any three numbers is {}.".format(np.array(Arr), maxprod(Arr)))

if __name__ == '__main__':
	main()


'''
Run-time output:
===============

markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_044.py

Test1:
Given a list of numbers: [-10 -10   5   2]
The maximum cumulative product of any three numbers is 500.

Test2:
Given a list of numbers: [12  4 22  9  5  7  6]
The maximum cumulative product of any three numbers is 2376.

Test3:
Given a list of numbers: [ 0.04291723  0.06962555  0.89750419  0.89626548  0.78072078  0.63605299
  0.76757435  0.74719118  0.96412441  0.41235676]
The maximum cumulative product of any three numbers is 0.775543630866.
markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ pytest codechallenge_044.py
==================================== test session starts ====================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_044.py .                                                                [100%]

================================= 1 passed in 0.46 seconds ==================================

'''
