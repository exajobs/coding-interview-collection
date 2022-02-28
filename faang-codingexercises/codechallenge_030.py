'''
Date: 01/12/2019

Problem description:
===================
This problem was asked by Google.

We can determine how "out of order" an array A is by counting the number of inversions it has. 
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller 
element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.
You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] 
has three inversions: (2, 1), (4, 1), and (4, 3). 
The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.

'''


import time
#
# O(N*2) time algorithm
#
def bruteforce_inversion_count(L=[]):
	if len(L) == 0:
		return None
	cnt = 0
	for i in range(len(L)):
		for j in range(i+1, len(L)):
			if L[i] > L[j]:
				cnt +=1
	return cnt


#
# Using list comprehension.
# This seems to incur additional run-time...
#
def fast_inversion_count(L=[]):
	if len(L) == 0:
		return None
	#print("DBUG-- L:{}".format(', '.join(str(i) for i in L)))

	inv_lst = [(j, k) for idx1, j in enumerate(L) for idx2, k in enumerate(L[1:]) if j > k and idx1 <= idx2]
	#print("DBUG-- inv_lst:{}".format(', '.join(str(i) for i in inv_lst)))
	return len(inv_lst)
	

def test_inversion_count():
	arr = [5,4,3,2,1]
	assert bruteforce_inversion_count(arr) == 10
	assert fast_inversion_count(arr) == 10

def main():
	arr = [2, 4, 1, 3, 5]
	print("Test1:\nGiven array: [{}]".format(', '.join(str(s) for s in arr)))
	s_time = time.time()
	print("The inversion count is {}".format(bruteforce_inversion_count(arr)))
	e_time = time.time()
	print("(slow method) Elapsed time: {} secs".format((e_time - s_time)*1000))

	print("\nTest2:\nGiven array: [{}]".format(', '.join(str(s) for s in arr)))
	s_time = time.time()
	print("The inversion count is {}".format(fast_inversion_count(arr)))
	e_time = time.time()
	print("(list_comprehension method) Elapsed time: {} secs".format((e_time - s_time)*1000))

	arr = [5,4,3,2,1]
	print("\nTest3:\nGiven array: [{}]".format(', '.join(str(s) for s in arr)))
	s_time = time.time()
	print("The inversion count is {}".format(bruteforce_inversion_count(arr)))
	e_time = time.time()
	print("(slow method) Elapsed time: {} secs".format((e_time - s_time)*1000))

	print("\nTest4:\nGiven array: [{}]".format(', '.join(str(s) for s in arr)))
	s_time = time.time()
	print("The inversion count is {}".format(fast_inversion_count(arr)))
	e_time = time.time()
	print("(list_comprehension method) Elapsed time: {} secs".format((e_time - s_time)*1000))

if __name__ == '__main__':
	main()

'''
Run-time output:
===============

(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_030.py
Test1:
Given array: [2, 4, 1, 3, 5]
The inversion count is 3
(slow method) Elapsed time: 0.07724761962890625 secs

Test2:
Given array: [2, 4, 1, 3, 5]
The inversion count is 3
(list_comprehension method) Elapsed time: 0.0858306884765625 secs

Test3:
Given array: [5, 4, 3, 2, 1]
The inversion count is 10
(slow method) Elapsed time: 0.06222724914550781 secs

Test4:
Given array: [5, 4, 3, 2, 1]
The inversion count is 10
(list_comprehension method) Elapsed time: 0.07343292236328125 secs


=============================== test session starts ===============================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_030.py .                                                      [100%]

============================ 1 passed in 0.06 seconds =============================
'''
