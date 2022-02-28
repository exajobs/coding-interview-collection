'''
Date: 12/20/2018

Problem description:
===================
This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given 
A = 3 -> 7 -> 8 -> 10 and 
B = 99 -> 1 -> 8 -> 10, 
return the node with value 8.
In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

Algorithm:
=========
Input: two linked lists
Output: integer value
Psuedo code:
1.  Check edge cases
2.  Iterate in nested loops to determine the node where values matched
'''

from __future__ import print_function

class linkedlistNode:
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

# add a node to end of linked list
def insertNode(head, val):
	currNode = head
	while currNode is not None:
		if currNode.next is None:
			currNode.next = linkedlistNode(val)
			return head
		currNode = currNode.next

# remove a node from linked list, needs work on head
def deleteNode(head, value):
	currNode = head
	prevNode = None
	while currNode is not None:
		if currNode.val == value:
			if prevNode is None:
				newHead = currNode.next
				return newHead
			prevNode.next = currNode.next
			return head
		prevNode = currNode
		currNode = currNode.next
	return head

# print linked list in ilustrated mode
def printNodes(nodeA):
	S=[]
	while (nodeA is not None):
		S.append(str(nodeA.val))
		nodeA = nodeA.next
	print(' -> '.join(S))


# find the intersected node in lists a and B
def getIntersectedNode(headA, headB):
	curNodeA = headA
	while curNodeA is not None:
		curNodeB = headB
		while curNodeB is not None:
			#print("curA:{} curB:{}".format(curNodeA.val, curNodeB.val))
			if curNodeB.val == curNodeA.val:
				return curNodeB.val
			curNodeB = curNodeB.next
		curNodeA = curNodeA.next

# function written for pytest module	
def test_code():
	A = linkedlistNode(3)
	insertNode(A, 7)
	insertNode(A, 8)
	insertNode(A, 10)
	B = linkedlistNode(99)
	insertNode(B, 1)
	insertNode(B, 8)
	insertNode(B, 10)

	assert getIntersectedNode(A,B) == 8

# client driver
if __name__ == "__main__":
	print("Given\nA singly linked list A: ", end='')
	# A = 3 -> 7 -> 8 -> 10 
	A = linkedlistNode(3)
	insertNode(A, 7)
	insertNode(A, 8)
	insertNode(A, 10)
	printNodes(A)


	# B = 99 -> 1 -> 8 -> 10
	print("And a singly linked list B: ", end='')
	B = linkedlistNode(99)
	insertNode(B, 1)
	insertNode(B, 8)
	insertNode(B, 10)
	printNodes(B)

	print("The intersected node on A and B is {}".format(getIntersectedNode(A,B)))


'''
Run-time output:
===============
$ python codechallenge-09.py
Given
A singly linked list A: 3 -> 7 -> 8 -> 10
And a singly linked list B: 99 -> 1 -> 8 -> 10
The intersected node on A and B is 8


$ pytest codechallenge-09.py
=============================== test session starts ================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodeChallenge, inifile:
collected 1 item

codechallenge-09.py .                                                        [100%]

============================= 1 passed in 0.08 seconds =============================
'''
