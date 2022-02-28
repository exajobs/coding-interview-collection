'''
Date: 01/28/2019

Task description:
=================
This problem was asked by Facebook.

Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, 
since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it 
up into two subsets that add up to the same sum.



Algorithm:
==========
Input: A set of integers
Output: A boolean

Psuedo code:

1.  Validate input
2.  Since set does not allow dupplicates, we will represent multiset using list for simplicity.
3.  Sort the list.  Iterate list index from both ends to yield every posible sublists of the given list
4.  For each subset, calculate sum and compare to half sum of the total list.
5.  Return True if sum of sublist equals half-sum, else False


'''


#
# return True if the multiset can be broken up into subsets
#
def isSub_able(R1, L2, halfTotal):
	l_total=0
	r_total=0
	for r_elem, l_elem in zip(R1, L2):
		r_total += r_elem
		l_total += l_elem
		#print("DBUG-- r_elem:{} l_elem:{}".format(r_elem, l_elem))
		if l_total == halfTotal or r_total == halfTotal:
			print("DBUG-- R_Total:{} L_Total:{} Half:{}".format(r_total, l_total, halfTotal))
			return True
	return False

#
# process list by disecting it incrementally
#
def get_sublist(L=[]):
	if len(L) == 0:
		return False

	halfSum = sum(L)//2
	L.sort()
	start, end = 0, len(L)
	x_end = end

	while start < end -1:
		sub_listA = L[start:x_end]
		x_end -= 1
		sub_listB = L[x_end+1:end] + L[:start]

		if isSub_able(sub_listA, sub_listB, halfSum):
			return True

		if x_end < start + 1:
			start += 1
			x_end = end
	return False

#
# unittest
#
def test_sublisting():
	myMSet = [15, 5, 20, 10, 35, 15, 10]
	assert get_sublist(myMSet) == True
	myMSet = [15, 5, 20, 10, 35]
	assert get_sublist(myMSet) == False

#
# client program
#
def main():
	myMSet = [15, 5, 20, 10, 35, 15, 10]
	print("\nTest1:\nGiven multiset {}".format(myMSet))
	print("Can it be broken into subsets?: {}".format(get_sublist(myMSet)))

	myMSet = [15, 5, 20, 10, 35]
	print("\nTest2:\nGiven multiset {}".format(myMSet))
	print("Can it be broken into subsets?: {}".format(get_sublist(myMSet)))

	myMSet = []
	print("\nTest3:\nGiven multiset {}".format(myMSet))
	print("Can it be broken into subsets?: {}".format(get_sublist(myMSet)))

if __name__ == '__main__':
	main()


'''
Run-time output:
================
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_041.py

Test1:
Given multiset [15, 5, 20, 10, 35, 15, 10]
DBUG-- R_Total:15 L_Total:55 Half:55
Can it be broken into subsets?: True

Test2:
Given multiset [15, 5, 20, 10, 35]
Can it be broken into subsets?: False

Test3:
Given multiset []
Can it be broken into subsets?: False
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ pytest codechallenge_041.py
=================================== test session starts ===================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_041.py .                                                              [100%]

================================ 1 passed in 0.13 seconds =================================

'''
