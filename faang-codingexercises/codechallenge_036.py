'''
Date: 01/21/2019

Problem description:
===================
This problem was asked by Apple.

Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) 
data structure with the following methods: enqueue, which inserts an element into the 
queue, and dequeue, which removes it.

Algorithm:
==========

Input: A single variable (could be number or string)
Output: Same variable from the dequeue() function

Psuedo Code:
1. Write the constructor for Stack with methods pop_at_start() and pop_at_end() 
1. Write a constructor for Queue consists of dual stacks.  New data will be enqueued onto the inStack, and dequeued from the outStack.
2. Write the enqueue() function to push the item onto the inStack 
3. Write the dequeue() function using the pop_at_end from inStack and push 
element onto outStack
4. Return each element from the outStack using pop_at_start()

Note: 
(*) If it wasn't for the premise in which we need to demonstrate the use of dual-stack in Queue,
we could have easily accomplished the task by reversing the list.
	
(**) A practical application for dual-stack queue would be something like the email inbox/outbox.
'''

#
# Stack implementation using list
# LIFO or variation of it.
#
class Stack:
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop_at_start(self):
		return self.items.pop(0)

	def pop_at_end(self):
		return self.items.pop(len(self.items)-1)

	def size(self):
		return len(self.items)  


#
# Queue consists of two stacks
# FIFO
#
class Queue:
	def __init__(self):
		self.inStack = Stack()
		self.outStack = Stack()

	def enqueue(self, item):
		self.inStack.push(item)

	def queue_size(self):
		return self.inStack.size() + self.outStack.size()

	def dequeue(self):
		if self.outStack.isEmpty():
			# pop item from bottom of inStack and push onto the top of outStack
			for i in range(self.inStack.size()):
				self.outStack.push(self.inStack.pop_at_end())

		# get the top item of the outStack
		return self.outStack.pop_at_start()


#
# unittest
#
def test_dualstack_queue():
	testQ = Queue()
	items = ['Make', 'code', 'not', 'war']
	[testQ.enqueue(item) for item in items]  # push all items onto the inStack

	for item in reversed(items):
		assert testQ.dequeue() == item


#
# client programm
#
def main():
	myQ = Queue()
	items = ['I', 'am', 'groot']
	[myQ.enqueue(item) for item in items]  # push all items onto the inStack

	print("\nTest1:\nGiven items: [{}]\nEnqueue all items into a dual-stack queue then dequeue all will output (order FIFO):".format(', '.join(str(i) for i in items)))
	for i in range(myQ.queue_size()):
		print(myQ.dequeue())


	items = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
	[myQ.enqueue(item) for item in items]  # push all items onto the inStack

	print("\nTest2:\nGiven items: [{}]\nEnqueue all items into a dual-stack queue then dequeue all will output (order FIFO):".format(', '.join(str(i) for i in items)))
	for i in range(myQ.queue_size()):
		print(myQ.dequeue())

	
if __name__ == '__main__':
	main()	

''' 
Run-time output:
===============
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_036.py

Test1:
Given items: [I, am, groot]
Enqueue all items into a dual-stack queue then dequeue all will output (order FIFO):
groot
am
I

Test2:
Given items: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
Enqueue all items into a dual-stack queue then dequeue all will output (order FIFO):
34
21
13
8
5
3
2
1
1
0
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ pytest codechallenge_036.py
=================================== test session starts ====================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_036.py .                                                               [100%]

================================= 1 passed in 0.03 seconds =================================
'''
