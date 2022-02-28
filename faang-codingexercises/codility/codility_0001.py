'''
Task description:
----------------

Given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..2,147,483,647].


Algorithm:
==========
Input: An integer
Output: An integer

Pseudo code:

1.  Check for valid input
2.  Convert integer into binary string
3.  Trim both ends of the string of any 0's
4.  Count the number of '1'
	if count('1') is 2, return count('0')
	else, split the binary string into groups of 0's
	and return the greater count(group('0'))
'''

from __future__ import print_function
def solution(N):
	b = bin(N)[2:]
	for i in range(len(b)):
		if b[0]=='0': b=b[1:]
		if b[-1]=='0': b=b[:len(b)-1]
	if b.count('1') > 2:
		gap_cnt=0
		temp_b = b.split('1')
		for i in temp_b:
			if gap_cnt < len(i):
				gap_cnt = len(i)
		
		return gap_cnt
	else:
			
		return b.count('0')

def test_solution():
	N = [1, 5, 101, 2147488647]
	GAPS = [0, 1, 2, 18]
	#[GAPS.append(solution(n) for n in N]
	for i,n in enumerate(N):
		assert solution(n) == GAPS[i]

	assert solution(11) == solution(20)

def main():
	A = [1,6,1401,39,55]
	B = []
	print("Test1:\nGiven number N in {}".format(', '.join(str(i) for i in A)))
	print("The binary gaps are: ", end='')
	[B.append(solution(i)) for i in A]
	print(', '.join(str(g) for g in B))

if __name__ == '__main__':
	main()


''' 
Run-time output:
---------------
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge/codility $ python codility_0001.py
Test1:
Given number N in 1, 6, 1401, 39, 55
The binary gaps are: 0, 0, 2, 2, 1

(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge/codility $ pytest codility_0001.py
=============================== test session starts ===============================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge/codility, inifile:
collected 1 item

codility_0001.py .                                                          [100%]

============================ 1 passed in 0.06 seconds =============================
'''
