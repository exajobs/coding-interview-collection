'''
Date: 01/27/2019

Problem description:
===================
This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.
Given such an array, find the index of the element in the array in 
faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, 
return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.


Algorithm:
==========
Input: An array of rotated, sorted integers, and an element x
Output: Index of element X in the array

Pseudo code:

1.  Validate input
2.  Split the array at the min value.
3.  Determine where the element is likely located to eliminate half of the original array
4.  For the remaining half, search the enumerated array or do recursive binary search.

Note: Pythonic has list.index() method.  We could simply use it.   
e.g. Arr = [13, 18, 25, 2, 8, 10]
	 Arr.index(8)
However, the purpose of this exercise is to programmatically describe what's under the hood.
'''


#
# return the index where max value starts in the array
#
def max_idx(Arr=[]):
	max_val = 0
	idx = 0
	for item, element in enumerate(Arr):
		if element > max_val:
			max_val = element
			idx = item
	return idx


#
# return index of k in Arr
#
def get_index(Arr, k):
	if len(Arr) == 0:
		return None

	# Split the array into two 
	# The two halfs are now sorted
	RightArr = Arr[:max_idx(Arr)+1]
	LeftArr = Arr[max_idx(Arr)+1:]

	#print("DBUG--RightArr: {}".format(RightArr))
	#print("DBUG--LeftArr: {}".format(LeftArr))	

	# look in RightArr. Alternately, we could use recursive calls in a subfunction here.
	if len(RightArr) > 0 and RightArr[0] <= k:
		for idx, elem in enumerate(RightArr):
			if elem == k:  
				return idx

	# look in LeftArr
	elif len(LeftArr) > 0 and LeftArr[0] <= k:
		for idx, elem in enumerate(LeftArr):
			if elem == k:  
				return idx + len(RightArr)
	else:
		return None
		 

#
# unittest
#
def test_searchindex():
	Arr = [21,23,25,5,6,10,13,17,20]
	elem = 25
	assert get_index(Arr, elem) == 2
	Arr = []
	elem = 100000
	assert get_index(Arr, elem) == None

#
# client program
#	
def main():
	Arr = [21,23,25,5,6,10,13,17,20]
	elem = 13
	print("\nTest 1:\nGiven an array [{}]\nThe index of element {} is {}".format(', '.join(str(i) for i in Arr), elem, get_index(Arr, elem)))

	Arr = [21,23,25,88,103,1000,-900,0,3,4,5,6,10,13,17,20]
	elem = 1000
	print("\nTest 2:\nGiven an array [{}]\nThe index of element {} is {}".format(', '.join(str(i) for i in Arr), elem, get_index(Arr, elem)))
	Arr = []
	elem = 1000
	print("\nTest 3:\nGiven an array [{}]\nThe index of element {} is {}".format(', '.join(str(i) for i in Arr), elem, get_index(Arr, elem)))

if __name__ == '__main__':
	main()


'''
Run-time output:
===============
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_039.py

Test 1:
Given an array [21, 23, 25, 5, 6, 10, 13, 17, 20]
The index of element 13 is 6

Test 2:
Given an array [21, 23, 25, 88, 103, 1000, -900, 0, 3, 4, 5, 6, 10, 13, 17, 20]
The index of element 1000 is 5

Test 3:
Given an array []
The index of element 1000 is None
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ pytest codechallenge_039.py
================================= test session starts ==================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_039.py .                                                           [100%]

=============================== 1 passed in 0.06 seconds ===============================
'''
