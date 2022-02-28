'''
Date: 12/03/2018

Problem description:
==================
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.

Pseudo code:
===========
1.  Sort the array and remove duplicates
2.  Shorten the array by eliminate elements having negative value.
    Note, zero is neither negative nor positive, so in step two, eliminate element with value zero as well.
3.  Traverse the array comparing index to its value.  The missing number should be last value+1.  Return the first missing number.
    
    Altenatively, the array can be converted into a dictionary, then determine the firt pair that key != value.


Performance wise, there is no appreciative difference between the three functions since it is in the order O(n)

Ways to shave on performance:
- split the array and search first half, then second half
- hashmap?
'''

import time
def findFirstMissing(arr):
	if len(arr) == 0:
		return None
	else:
		# sort, remove duplicates
		arr = list(set(arr))
		# remove negative values from the array 	
		arr = [n for n in arr if n > 0] 

		# use list comprehesion to get the first missing number
		# this yields a list instead of sing number. Hmmm...
		missing = [arr[i-1]+1 for i, val in enumerate(arr) if val > arr[i-1]+1]
		return missing[0]

def firstMissingValA(arr):
	if len(arr) == 0:
		return None
	else:
		# sort, remove duplicates
		arr = list(set(arr))
		# remove negative values from the array 	
		arr = [n for n in arr if n > 0] 

		# use iterative loop
		for i,n in enumerate(arr):
			if (n > arr[i-1]+1):
				missing = arr[i-1]+1
				break
	return missing

def firstMissingValB(arr):
	if len(arr) == 0:
		return None
	else:
		# sort, remove duplicates
		arr = list(set(arr))
		# remove negative values from the array 	
		arr = [n for n in arr if n > 0] 

		# use ditionary to get to the missing number
		dArr = { i+1 : arr[i] for i in range(0, len(arr) ) }
		for k,v in dArr.items():
			if k != v:
				missing = k
				#print("k:{} v:{}  missing:{}".format(k, v, missing))
				break
	return missing


'''
unittest func written for pytest module  i.e. pytest codechalleng-04.py
'''
def test_code():
	missing = 13
	A = list(range(-20, missing))
	A.append(missing+2)
	A.append(missing+20)

	starttime = time.time()
	assert findFirstMissing(A) == missing 
	endtime = time.time()
	print("Elasped time running firstFirstMissing() is {}".format(endtime - starttime))

	starttime = time.time()
	assert firstMissingValA(A) == missing 
	endtime = time.time()
	print("Elasped time running firstMissingValA() is {}".format(endtime - starttime))

	starttime = time.time()
	assert firstMissingValB(A) == missing 
	endtime = time.time()
	print("Elasped time running firstMissingValB() is {}".format(endtime - starttime))


'''
main driver, run using python
'''
if __name__ == "__main__":
	test_code()


'''
Runt-time output:
================
$ python codechallenge-04.py
Elasped time running firstFirstMissing() is 8.08238983154e-05
Elasped time running firstMissingValA() is 6.19888305664e-05
Elasped time running firstMissingValB() is 8.89301300049e-05

 
$ pytest codechallenge-04.py
========================================= test session starts ==========================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodeChallenge, inifile:
collected 1 item

codechallenge-04.py .                                                                            [100%]

======================================= 1 passed in 0.06 seconds =======================================
'''
