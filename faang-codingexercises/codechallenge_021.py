'''
Date: 01/04/2019

Problem description:
===================
This problem was asked by Dropbox.
Given the root to a binary search tree, find the second largest node in the tree.


       [6]      [6]      [6] 
       / \        \      / \
     [5] [7]      [9]  [5] [8]
                  / \        \
                [8] [10]    [10]

Algorithm:
=========
Input: Root of a binary search tree
Output: Node of second to right most.
Psuedo code:
	Binary Search Tree inherently contains sorted data.
1.	Write the BST constructor, add function, print function
2.	We will search for two cases 
	2.1  If root is None return None
	2.2  If root->right->right is None, return root->data


After thoughts:
==============
(*) Try to assign and return an array of values in a recursive function
and you will be surprised what will come out.  For example, if you initialized
a list in the print_tree(self) function and append data to it.  The index of
your list may be recursively retro to zero each time the function called itself.
Haha!
(**) When root.data is None.  Is data literally equal to 'None' or null?
'''
from __future__ import print_function
class BSTNode:
	def __init__(self, data, right=None, left=None):
		self.data = data
		self.right = right
		self.left = left

	def add(self, data):
		if self.data:
			if data < self.data:
				# left branches
				if self.left is None:
					self.left = BSTNode(data)
				else:
					self.left.add(data)
			elif data > self.data:
				# right branches
				if self.right is None:
					self.right = BSTNode(data)
				else:
					self.right.add(data)
		else:
			# root
			self.data = data


	#
	# in-order traversal print
	#
	def print_tree(self):
		# in-order traversal: left-root-right
		if self.left:
			self.left.print_tree()
		print ("{} ".format(self.data), end=''),
		if self.right:
			self.right.print_tree()

	#
	# breadth first traversal
	#
	def get_second_last_right(self):
		if self.data is None:
			print(None)
			return None
		if self.right:
			# traverse only the right sub tree
			if self.right.right is None:
				print(self.data)
				return self.data
			# recursively calling itself to move down the right branch
			self.right.get_second_last_right()


	#
	# list generator for BST data
	#
	def tree_data(self):
		datalist = []
		node = self
		while datalist or node:
			if node:
				datalist.append(node)
				node = node.left
			else:
				node = datalist.pop()
				yield node.data
				node = node.right			
#
# This way of getting the second largest data is 
# a deviation from the scope of BST question but 
# it demonstrates the use of generator 
def test_code():
	tnode = BSTNode(2)
	tnode.add(3)
	tnode.add(4)
	tnode.add(9)
	tnode.add(7)
	data = list(tnode.tree_data())
	if len(data) > 1:
		assert data[-2] == 7	


def run_test(root, testnum):
	print("\nTest{}:\nGiven a binaray search tree having data:".format(testnum))
	root.print_tree()	
	print("\nSecond largest value in the BST is:")
	root.get_second_last_right()
	
if __name__ == '__main__':
	t1node = BSTNode(3)
	values = [2,4,19,7,9]
	for num in values:
		t1node.add(num)
	print("Test1:\nGiven a binaray search tree having data:")
	t1node.print_tree()	
	data = list(t1node.tree_data())
	print("\nSecond largest value in the BST is: {}".format(data[-2]))	

	t2node = BSTNode(8)
	values = [5,7,17,9,10,19]
	for num in values:
		t2node.add(num)
	run_test(t2node, 2)

	t3node = BSTNode(None)
	run_test(t3node,3)






'''
Run-time output:
===============
markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_021.py

Test1:
Given a binaray search tree having data:
2  3  4  7  9  19  
Second largest value in the BST is: 9

Test2:
Given a binaray search tree having data:
5  7  8  9  10  17  19  
Second largest value in the BST is:
17

Test3:
Given a binaray search tree having data:
None  
Second largest value in the BST is:
None


markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ pytest codechallenge_021.py
====================================== test session starts ======================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_021.py .                                                                    [100%]

=================================== 1 passed in 0.08 seconds ====================================
'''

