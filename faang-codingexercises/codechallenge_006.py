'''
Date: 12-17-2018
Problem description:
===================
This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, 
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, 
we should get: [10, 7, 8, 8], since:
	10 = max(10, 5, 2)
	7 = max(5, 2, 7)
	8 = max(2, 7, 8)
	8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place 
and you do not need to store the results. 
You can simply print them out as you compute them.


Algorithm:
=========
Input: list of integers and int k
Output: integer value
Psuedo code:
1.  Check edge cases
2.  Iterate the len of list, find max value using built-in function int.max() 

'''


import time

#
# brute force
#
def maxValInArray(arr, k):
	''' check edge case '''
	assert k >= 1
	assert k <= len(arr)

	if k == 1:
		#print( arr )
		return arr
	else:
		subarr = list()
		listofmax = list()

		while (len(arr) >= k):
			x = 0
			for x in range(x, (k+x)):
				subarr.append(arr[x])
			#listofmax.append(sorted(subarr, reverse=True)[:1])
			listofmax.append(max(subarr))
			subarr = []
			arr.pop(0)

		#print (listofmax)
		return listofmax
			

#
# O(n) time and O(k) space
#
def maxValsList(arr, k):
	''' check edge case '''
	assert k >= 1
	assert k <= len(arr)

	if k == 1:
		#print( arr )
		return arr
	else:
		retarr = list()
		while len(arr) >= k:
			#print(max([a[i] for i in range(k)]))
			retarr.append(max([arr[i] for i in range(k)]))
			arr.pop(0)

		return retarr


def test_code():
	A = [10, 5, 2, 7, 8, 7]
	K = 3
	assert maxValInArray(A, K) == [10, 7, 8, 8] 

	A = [10, 5, 2, 7, 8, 7]
	assert maxValsList(A, K) == [10, 7, 8, 8]

	A = [10, 5, 2, 7, 8, 7]
	K = 1
	assert maxValsList(A, K) == [10, 5, 2, 7, 8, 7]
if __name__ == "__main__":
	A = [10, 5, 2, 7, 8, 7]
	K = 3

	print ("Original array: {}".format(A))
	starttime = time.time()
	print( maxValInArray(A, K)) 
	endtime = time.time()
	print("Elapsed time in brute force methob: {} secs".format(endtime - starttime))

	A = [10, 5, 2, 7, 8, 7]
	starttime = time.time()
	print( maxValsList(A, K))
	endtime = time.time()
	print("Elapsed time in O(n) method: {} secs".format(endtime - starttime))
	

'''
Run-time output:
===============
$ python codechallenge-06.py
Original array: [10, 5, 2, 7, 8, 7]
[10, 7, 8, 8]
Elapsed time in brute force methob: 0.000123023986816 secs
[10, 7, 8, 8]
Elapsed time in O(n) method: 0.000108003616333 secs


$ pytest codechallenge-06.py
========================================= test session starts ==========================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodeChallenge, inifile:
collected 1 item

codechallenge-06.py .                                                                            [100%]

======================================= 1 passed in 0.06 seconds =======================================
'''
