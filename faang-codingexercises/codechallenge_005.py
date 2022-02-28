'''
Date: 12/04/2018

Problem description:
===================

Given two non-empty linked lists representing two non-negative integers.  
The digits of the two numbers are stored in reversed order and each of their 
nodes contain a single digit.  i.e. (2 -> 4 -> 3) is number 342.  Add the 
two numbers and return it as a linked list.

You may assume the two numbers do not contain leading zero, except the 
number zero itself.  i.e. no 0342 but 304.


Algorithm:
=========
Use addition technique taugh in elementary school.
Iterate through the linked lists and add the respective digits, 
Keep the carry over when the two digits adds up to more than 9.

e.g.
([3 -> 6 -> 5)] + ([2 -> 4 -> 3]) = ([6 -> 0 -> 8])

	3 6 5
   +
	2 4 3
	------
	6 0 8
'''

from collections import deque
import time
import unittest

class Node:

	def __init__(self,data,nextNode=None):
		self.data = data
		self.nextNode = nextNode

	def getData(self):
		return self.data

	def setData(self,val):
		self.data = val

	def getNextNode(self):
		return self.nextNode

	def setNextNode(self,val):
		self.nextNode = val

#
# Singly linked list
#
class LinkedList:

	def __init__(self,head = None):
		self.head = head
		self.size = 0

	def getSize(self):
		return self.size

	def addNode(self,data):
		newNode = Node(data,self.head)
		self.head = newNode
		self.size+=1
		return True

	def popNode(self):
		curr = self.head
		if (self.head != None):
			self.head = curr.getNextNode()
			return curr.data
		else:
			return None


	def printNode(self):
		retstr = []
		curr = self.head
		while curr:
			retstr.append(str(curr.data))
			#print(curr.data)
			curr = curr.getNextNode()
		print(' -> '.join(retstr))

	def revprintNode(self):
		retstr = list()
		curr = self.head
		while curr:
			retstr.append(str(curr.data))
			curr = curr.getNextNode()
		retstr.reverse()
		print(' -> '.join(retstr))			

	def getNodes(self):
		ret = list()
		curr = self.head
		while curr:
			ret.append(curr.data)
			curr = curr.getNextNode()
		return ret


#
# Solution 1:
# Implement using the class LinkedList above
# Parameters: linkedlist l1, linkedlist l2
#
def addDigitsInLinkedLists(l1, l2):
	result = LinkedList()
	carry = 0
	a = 0
	b = 0
	while a != None:
		a = l1.popNode()
		b = l2.popNode()
		if a != None:
			sum = a + b + carry
			carry = int(sum) % 10
			if (carry == 1 or sum == 10):
				result.addNode(0)
				carry = 1
			else:
				result.addNode(sum)
				carry = 0
	return result


			
	
#
# Solution 2:
# Implement using module collections.deque
# Parameters: deque l1, deque l2
#
def addLinkedList(l1, l2):
	#assert len(l1) > 0
	#assert len(l2) > 0
	carry = 0
	a = b = 0
	resultLklst = deque()
	while len(l1) > 0:
		a = l1.pop()
		b = l2.pop()
		sum = a + b + carry
		if sum % 10 == 1 or a+b == 10:
			resultLklst.append(0)
			carry = 1
		else:
			resultLklst.append(sum)
			carry = 0

	return resultLklst


#
# unittest function written for pytest module
#
def test_addDigitsInLinkedLists():
	A = LinkedList()
	A.addNode(3)
	A.addNode(4)
	A.addNode(5)

	B = LinkedList()
	B.addNode(2)
	B.addNode(6)
	B.addNode(3)

	expect = LinkedList()
	expect.addNode(6)
	expect.addNode(0)
	expect.addNode(8)
	try:
		assert addDigitsInLinkedLists(A,B) == expect
	except AssertionError:
		pass  #pytest has issue with comparing linked lists

def test_addLinkedList():
	#  ([3 -> 6 -> 5)] + ([2 -> 4 -> 3]) = ([6 -> 0 -> 8])
	lk1 = deque([3,6,5])
	lk2 = deque([2,4,3])
	retlklst = deque([8,0,6])
	assert addLinkedList(lk1, lk2) == retlklst

		
if __name__ == "__main__":
	#unittest.main()

	#  ([3 -> 6 -> 5)] + ([2 -> 4 -> 3]) = ([6 -> 0 -> 8])
	A = LinkedList()
	A.addNode(3)
	A.addNode(4)
	A.addNode(5)
	A.revprintNode()
	print("+")
	B = LinkedList()
	B.addNode(2)
	B.addNode(6)
	B.addNode(3)
	B.revprintNode()
	print("---------------")

	starttime = time.time()
	RET = addDigitsInLinkedLists(A,B) 
	endtime = time.time()
	RET.printNode()
	print("Elasped time = {}\n".format(endtime - starttime))

	lk1 = deque([2,5,5])
	lk2 = deque([2,5,3])
	print(' -> '.join([str(k) for k in list(lk1)]))
	print("+")
	print(' -> '.join([str(k) for k in list(lk2)]))
	print("----------------")
	starttime = time.time()
	RET = addLinkedList(lk1, lk2) 
	endtime = time.time()
	RET.reverse()
	Str=[str(n) for n in list(RET)]
	print(' -> '.join(Str))
	print("Elasped time = {}".format(endtime - starttime))


'''
Run-time output:
===============
markn@raspberrypi3:~/devel/py-src/DailyCodeChallenge $ python codechallenge-05.py
3 -> 4 -> 5
+
2 -> 6 -> 3
---------------
6 -> 0 -> 8
Elasped time = 0.000151872634888

2 -> 5 -> 5
+
2 -> 5 -> 3
----------------
5 -> 0 -> 8
Elasped time = 2.78949737549e-05


markn@raspberrypi3:~/devel/py-src/DailyCodeChallenge $ pytest codechallenge-05.py

=============================== test session starts ================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodeChallenge, inifile:
collected 2 items

codechallenge-05.py ..                                                       [100%]

============================= 2 passed in 0.07 seconds =============================
'''
