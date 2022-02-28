'''
Date: 01/05/2019

Problem description:
===================
This problem was asked by Google.

The power set of a set is the set of all its subsets. 
Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return 
{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
You may also use a list or array to represent a set.


Algorithm:
=========
Input: A set of numbers
Output: A power set of numbers
Psuedo code:
1.  Check for valid input
2.  Create an generator yielding the following sequence:
	yield an empty set
	yield individual sets in the original set
	yield iterative sets with one-to-many 
	yield original set
3.  Assign an iterator to the generator and append
	items to a list.  
4.	Return the list. 

'''
from __future__ import print_function
#
# generator for powerset
#
def iterlist(s1):
	yield {}
	for i in s1:
		yield {i}

	#s2 = s1[:]
	s2 = list(s1)
	for i in s1:
		s2.pop(0)
		for j in s2:
			yield {i,j}
	yield set(s1)

#
# iterate the powerset to
# retrieve a list 
#
def powerlist(s1):
	if len(s1) == 0:
		return None

	powerset = []
	for i in iterlist(s1):
		powerset.append(i)

	return powerset


#
# unittest
# 
def test_code():
	s1 = [1,2,3,4,5]
	assert powerlist(s1) == [{}, {1}, {2}, {3}, {4}, {5}, {1, 2}, {1, 3}, {1, 4}, {1, 5}, {2, 3}, {2, 4}, {2, 5}, {3, 4}, {3, 5}, {4, 5}, {1, 2, 3, 4, 5}]


#
# one-liner output
#
def print_formatted_set(ps):
	for p in ps:
		print ('{{{}}},  '.format(', '.join(str(e) for e in p)), end='')
	print("\n")
	

if __name__ == '__main__':
	s1 = [1,2,3]
	print("\nTest1\n-----\nGiven a set:")
	print(s1)

	ps = powerlist(s1)
	print("Its powerset:")
	print_formatted_set(ps)

	str = 'mark'
	sstr = list(str)
	print("Test2\n-----\nGiven a set:")
	print(sstr)
	psstr = powerlist(sstr)
	print("Its powerset:")
	for item in psstr:
		print(list(item), end=', ')
	print("\n")

'''
Run-time output:
===============

(interactive python)
>>> import codechallenge_022
>>> str = 'mark'
>>> codechallenge_022.powerlist(list(str))
[{}, {'m'}, {'a'}, {'r'}, {'k'}, {'m', 'a'}, {'m', 'r'}, {'m', 'k'}, {'a', 'r'}, {'k', 'a'}, {'k', 'r'}, {'m', 'k', 'a', 'r'}]
>>>
>>> s1 = [1,2,3,4,5]
>>> ps = codechallenge_022.powerlist(s1)
>>> ps
[{}, {1}, {2}, {3}, {4}, {5}, {1, 2}, {1, 3}, {1, 4}, {1, 5}, {2, 3}, {2, 4}, {2, 5}, {3, 4}, {3, 5}, {4, 5}, {1, 2, 3, 4, 5}]



(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_022.py

Test1
-----
Given a set:
[1, 2, 3]
Its powerset:
{},  {1},  {2},  {3},  {1, 2},  {1, 3},  {2, 3},  {1, 2, 3},

Test2
-----
Given a set:
['m', 'a', 'r', 'k']
Its powerset:
[], ['m'], ['a'], ['r'], ['k'], ['m', 'a'], ['r', 'm'], ['k', 'm'], ['r', 'a'], ['k', 'a'], ['r', 'k'], ['r', 'k', 'm', 'a'],

(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ pytest codechallenge_022.py
======================================= test session starts ========================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_022.py .                                                                       [100%]

===================================== 1 passed in 0.06 seconds =====================================
'''
