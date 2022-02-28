'''
Date: 01/08/2019

Problem description:
===================
This problem was asked by Google.

Given an array of integers where every integer occurs three times 
except for one integer, which only occurs once, find and return the 
non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. 
Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.

Algorithm:
==========
Input: A list of numbers
Output: An integer represeting the non-duplicate value
Psuedo code:
1.  Check for valid input
2.  Rerurn value from set(list-comprehension) where element 
    count equals to one

Note:  This is why I love Python!!!
'''

def find_non_dup(A=[]):
	if len(A) == 0:
		return None
	non_dup = list(set([x for x in A if A.count(x) == 1]))
	return non_dup[-1]

def test_code():
	A = [7,3,3,3,7,8,7]
	assert find_non_dup(A) == 8

if __name__ == '__main__':
	Array = [9,5,5,5,8,9,8,9,3,4,4,4]
	non_dup = find_non_dup(Array)
	print("Test1:\nGiven a list [{}]\nThe non-duplicate value is {}".format(', '.join(str(i) for i in Array), non_dup))

'''
Run-time output:
===============
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_025.py
Test1:
Given a list [9, 5, 5, 5, 8, 9, 8, 9, 3, 4, 4, 4]
The non-duplicate value is 3

(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ pytest codechallenge_025.py
================================ test session starts =================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_025.py .                                                         [100%]

============================== 1 passed in 0.03 seconds ==============================

'''

