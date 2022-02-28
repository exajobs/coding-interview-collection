'''
Date: 02/08/2019

Task description:
================
This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.
Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.


Algorithm:
==========
Task: Given an integer value n, find out the n-th positive integer whose sum is 10.
Input: An integer N
Output: An integer representing the n-th perfect number.

Psuedo code:

1.  Validate input
2.  Start the counter until all digits summed up to ten.  Up the perfect count by one until perfect count equals N

(*) Note, a number is perfect if the sum of its proper factors is equal to the number.
And, all multiples of 9 are present in arithmetic progression 19, 28, 37, 46, 55, 64, 73, 82, 91, 100, 109,...

'''

import itertools

def findNthFactor(N):  
	if N <= 0:
		return -1

	count = 0 
	n_fact = 19 
	while (True):  
  
		# Find sum of digits in 
		# n_fact no.  
		sum = 0 
		x = n_fact 
		while (x > 0): 
			sum = sum + x % 10 
			x = int(x / 10) 
  
		# If sum is 10, we increment 
		# count  
		if (sum == 10):  
			count+=1  
  
		# If count becomes N, we return  
		# n_fact number.  
		if (count == N):  
			return n_fact 
          
		n_fact += 9 
  
	return -1


def test_findNthFactor():
	assert findNthFactor(0) == -1
	assert findNthFactor(1) == 19
	assert findNthFactor(2) == 28


def main():
	print("\nTest1:")
	A = [i+1 for i in range(10)]
	B = [findNthFactor(A[i]) for i in range(len(A))]
	for i,n in enumerate(B):
		print("n:{}, perfect n-th:{}".format(i+1,n))	
	print("\nTest2:")
	A = [i+1 for i in range(10,20,1)]
	B = [findNthFactor(A[i]) for i in range(len(A))]
	for i,n in enumerate(B):
		print("n:{}, perfect n-th:{}".format(i+11,n))	

if __name__ == '__main__':
	main()

'''
Run-time output:
===============

(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_045.py

Test1:
n:1, perfect n-th:19
n:2, perfect n-th:28
n:3, perfect n-th:37
n:4, perfect n-th:46
n:5, perfect n-th:55
n:6, perfect n-th:64
n:7, perfect n-th:73
n:8, perfect n-th:82
n:9, perfect n-th:91
n:10, perfect n-th:109

Test2:
n:11, perfect n-th:118
n:12, perfect n-th:127
n:13, perfect n-th:136
n:14, perfect n-th:145
n:15, perfect n-th:154
n:16, perfect n-th:163
n:17, perfect n-th:172
n:18, perfect n-th:181
n:19, perfect n-th:190
n:20, perfect n-th:208
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ pytest codechallenge_045.py
==================================== test session starts ====================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_045.py .                                                                [100%]

================================= 1 passed in 0.06 seconds ==================================
'''
