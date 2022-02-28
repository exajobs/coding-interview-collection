'''
Date: 01/01/2019

Problem description:
===================
This problem was asked by Microsoft.
Compute the running median of a sequence of numbers. That is, given a stream of numbers, 
print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.
For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
2
1.5
2
3.5
2
2
2


Algorithm:
=========
Input: A list of numbers
Output: a sequnce of numbers
Pseudo code:
1.  Check for valid input
2.  Traverse the list,
    for each new element, sort the traversed elements to find the median
3.  print out the middle element if odd-numbered list
    else print the average of the two middle elements if it is an even-numbered list
'''


from __future__ import division
def runningMedian(nums=[]):
	retstr = []  # return string for unittest purpose
	if len(nums) == 0:
		return None

	growinglist = []
	for n in nums:
		growinglist.append(n)
		growinglist.sort()
		mid_idx = len(growinglist)//2
		median = 0 

		'''
		dbugstr = ','.join(str(n) for n in growinglist)
		print("DBUG-- Array:{}  mid_idx:{}".format(dbugstr, mid_idx))
		'''

		if len(growinglist) == 1:
			median = growinglist[0]
		elif len(growinglist) % 2 == 0:
			#even-numbered list
			median = (growinglist[mid_idx] + growinglist[mid_idx-1]) / 2
		else:
			#odd-numbered list
			median = growinglist[mid_idx]	

		retstr.append(median)
		print(median)
	return(retstr)

def test_code():
	Arr = [2, 1, 5, 7, 2, 0, 5]
	assert runningMedian(Arr) == [2,1.5,2,3.5,2,2.0,2]

if __name__ == '__main__':
	Arr = [2, 1, 5, 7, 2, 0, 5]
	runningMedian(Arr)



'''
Run-time output:
===============
markn@raspberrypi3:~/devel/py-src/DailyCodeChallenge $ python codechallenge_018.py
2
1.5
2
3.5
2
2.0
2

markn@raspberrypi3:~/devel/py-src/DailyCodeChallenge $ pytest codechallenge_018.py
=================================== test session starts ===================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodeChallenge, inifile:
collected 1 item

codechallenge_018.py .                                                              [100%]

================================ 1 passed in 0.03 seconds =================================

'''
