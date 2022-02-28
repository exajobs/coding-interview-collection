'''
Date: 12/02/2018

Problem description:
===================
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'


Pseudo code:
============
1.  Construct the __init__ with self, val, left, right
2.  implement the Insert function
3.  implement the serialize(root), where root is the initialized node
4.  implement the deserialize(s) function where s is a string


The input for val has the format of 'root, 'root.left.right' or 'left.left.right.left'  
so, it is nicer to split the string
e.g.
	str = 'root.left.right'
	arr = str.split('.')


(*) Oh and this string should fail: 'left.left.right.left' because this is a rooted binary tree.
'''


class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def insert(self, val, left, right):
		if self.left is None:
			self.left = Node(val)
		else:
			self.left.insert(val)
		
		if self.right is None:
			self.right = Node(val)
		else:
			self.right.insert(val)

'''
serializes the tree (root) into a string (s)
treat root as a Node data structure.
'''
def serialize(root):
	# check edge case
	if root is None:
		return None
	
	# base case
	if root.val == 'root':
		arr.append(root.val)
		arr.append('.')

	# add root node
	arr.append(node.val)
	# add left node
	serialize(root.left, arr)
	# add right node
	serialize(root.right, arr)

'''
deserializes the string back into the tree
'''
def deserialize(s):
	# We use list.pop() and so we need to use this wrapper to 
	# first convert the string to an array and 
	# reverse the array before sending it to _deserialize()

	# check edge case
	if (len(s) == 0):
		return None

	# split the string into array
	arr = str(s).split('.')
	arr.reverse()
	print(arr)
	do_deserialize(arr) 

def do_deserialize(arr):
	if len(arr) > 0:
		val = arr.pop()
		
		# base case
		if val == 'root':
			# create a new node as the root node
			node = Node('root', None, None)	    	
		else:
			node = Node(arr)

	    # add root
		node.val = val

		# add left 
		node.left = do_deserialize(arr)

		# add right 
		node.right = do_deserialize(arr)

		# go up the node
		print(type(node))
		return node



if __name__ == "__main__":
	s = 'root.left.left'
	a = s.split('.')
	print(s)
	print(a)
	deserialize(s)	
	newstr = serialize(deserialize(s))	
	print(newstr)
'''
	tree = Node('root', Node('left', Node('left.left')), Node('right'))
	print(tree.val)
	print(tree.left)
	print(tree.right)
'''

'''
Run-time output:
===============
markn@raspberrypi3:~/devel/py-src/DailyCodeChallenge $ python codechallenge-03.py
root.left.left
['root', 'left', 'left']
['left', 'left', 'root']
<type 'instance'>
<type 'instance'>
<type 'instance'>
['left', 'left', 'root']
<type 'instance'>
<type 'instance'>
<type 'instance'>
None
'''
