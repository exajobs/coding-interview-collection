'''
Date: 01/13/2019

Problem description:
===================
This problem was asked by Two Sigma.

Using a function rand5() that returns an integer from 1 to 5 (inclusive) 
with uniform probability, implement a function rand7() that returns an 
integer from 1 to 7 (inclusive).


Algorithm:
=========
Input: None
Output: An integer

Psuedo code:

1.  Import random
2.  Create a funtion to return an integer from 1 to 5 inclusive
3.  Use the above function to create a funtion that returns
	an integer from 1 to 7 inclusively.

'''

from __future__ import print_function
import random

def rand5(): return random.randint(1, 5)

def rand7(): return rand5() + random.randint(0, 2)

def test_random7():
	assert rand7() <= 7

def main():
	nums = []
	for i in range(6):
		nums.append(rand7())
	
	print("Test1:\nGenerate 10 random numbers (1,..,7) using rand7:  {}\n".format(", ".join(str(i) for i in nums)))

	print("Test2:\nRepeatedly generate numbers using rand7() until a 7 is procuded... ", end='')
	while True:
		if rand7() == 7:
			print("got a 7")
			break
if __name__ == '__main__':
	main()


'''
Run-time output:
===============
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_031.py
Test1:
Generate 10 random numbers (1,..,7) using rand7:  2, 5, 5, 3, 1, 2

Test2:
Repeatedly generate numbers using rand7() until a 7 is procuded... got a 7


(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_031.py
Test1:
Generate 10 random numbers (1,..,7) using rand7:  3, 5, 6, 3, 5, 7

Test2:
Repeatedly generate numbers using rand7() until a 7 is procuded... got a 7


(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ pytest codechallenge_031.py
=============================== test session starts ===============================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_031.py .                                                      [100%]

============================ 1 passed in 0.05 seconds =============================
'''
