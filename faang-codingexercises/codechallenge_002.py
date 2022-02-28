'''
Date: 12/01/2018

Problem description:
===================
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?

Algorithm: prodArray()
======================
Input: A list of integers
Output: A list of integers
Psuedo code:
1. Check edge cases for empty input
2. Initialize an empty list 
3. In a for loop, if product equals product time item in list except current item
4. Append product into the initialized array above
'''



#
# This implementation uses nested loop and the manipulation of slicing index 
# Not a good performance code because the entire range gets traversed.
# Note that I don't use division.
#
def prodArray(a):
	p=[]
	# edge case
	if len(a) == 0:
		return p

	# have data, let's go
	for i in range(len(a)):
		prod=1
		#for x, n in enumerate(range(0, len(a))):
		for x in range(0, len(a)):
			if x != i:
				prod=prod*a[x]
			#print("i={} x={} n={} prod={}".format(i,x,a[x], prod))
		#print(prod)
		p.append(prod)
		pro=1
	print(p)
	return p

# unittest func written for pytest module
def test_code():
	nums=[3, 2, 1]
	assert prodArray(nums) == [2,3,6]
	nums=list(range(1,6))
	assert prodArray(nums) == [120,60,40,30,24]

if __name__ == "__main__":
	test_code()


'''
Runt-time output:
================
$ python codechallenge-02.py
[2, 3, 6]
[120, 60, 40, 30, 24]


$ pytest codechallenge-02.py
========================================= test session starts ==========================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodeChallenge, inifile:
collected 1 item

codechallenge-02.py .                                                                            [100%]

======================================= 1 passed in 0.03 seconds =======================================
'''
