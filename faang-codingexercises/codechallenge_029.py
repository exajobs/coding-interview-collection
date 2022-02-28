'''
Date: 01/11/2019

Problem dscription:
==================
This problem was asked by Amazon.

Implement a stack that has the following methods:
-	push(val), which pushes an element onto the stack
-	pop(), which pops off and returns the topmost element of the stack. 
If there are no elements in the stack, then it should throw an error or return null.
-	max(), which returns the maximum value in the stack currently. 
If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.

Algorithm:
=========
Input:  Initialized stack, then add elements
Output:  Printout the content, size, top, and max element(s)

Psuedo code:
Implement stack methods using list.
1.  Create a class called Stack and initialize with empty "list"
2.  Implement push method to "prepend" element onto the stack
3.  Implement pop method to pop element from the "list"
4.  Implement method to return max value in the stack 
	-  Check if stack is not empty, try, except - raise
	-  For stack size, loop the iterable until max value is found
	-  Return max value
To achieve constant time, the max method would make use of max(list) function.


After thoughts:
==============
(*) Note that the difference between stack and queue is when decide
the order (LIFO or FIFO) in which items are push/enqueue and pop/dequeue.  
Really, the only method needs to be differentiated is push/enqueue 
in O(1)/O(n) complexity.
i.e.
	#LIFO 
	def push(self, item): self.items.append(item)

	#FIFO
	def enqueue(self, item): self.items.insert(0, item)
If you could picture standing up an array, you'd see a stack.  Leave it lying
horizontally, you'd see a queue.


(**) Remember the trick question on reversing the string?
We automatically thought of the reversed(list) method.  
Now, think of how the stack s applied in solving it.
e.g.  
s = Stack()
s.push('I')
s.push('am'
s.push('groot')
while not s.isEmpty():
	print(s.pop())

The output would be the reversed string: 'groot am I'.
Hmm, someone should build a master Yoda speech function:
s.push('groot')
s.push('are')
s.push('you')

'''


import time
class Stack:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def push(self, item):
		self.items.append(item) # use the convention of end means top
	def pop(self):
		try:
			return self.items.pop()
		except IndexError:
			return None
	def size(self):
		return len(self.items)
	def peek(self):
		return self.items[len(self.items)-1]
	def peek_top(self):
		return self.items[0]
	def print_stack(self):
		return ', '.join(str(val) for val in self.items)

	# return max value in constant time
	def max(self):
		try:
			return max(self.items)
		except:
			raise ValueError("null data")
			return None	

	# return max value in O(n), N time	 
	def mad_max(self):
		# generate an iterable
		iteritems = iter(self.items)

		try:
			max_val = next(iteritems) # assign the first value as the max value
		except StopIteration:
			raise ValueError("max() called with no value")
			return None

		for val in iteritems:
			if val > max_val:
				max_val = val
		return max_val	

#
# unittest module
#
def test_stack():
	#init
	S = Stack()
	assert S.isEmpty() == True
	A = [11,19,100]
	[S.push(i) for i in A] # push items in the array A onto stack S
	assert S.size() == 3
	S.pop()
	assert S.print_stack() == "11, 19"
	A = [100, 3, 21]
	[S.push(i) for i in A] # push items in the array A onto stack S
	assert S.peek() == 21
	assert S.max() == 100


#
# generate a stack containing fibonacci sequence for testing
#
def fibon(n):
	if n <= 1:
		return n
	else:
		return fibon(n-1) + fibon(n-2)
def gen_stack(n):
	S = Stack()
	for i in range(n):
		S.push(fibon(i))  # push the fibo value onto the stack
	return S



#
# direct client program
#
def main():
	print("The followings print the stack content with starting line as bottom and ending line as top of the stack.\n")
	s = Stack()
	lst = [9, 10, 23, 5]
	[s.push(i) for i in lst] # push values in array lst onto the stack s

	print("Test1:\nContent of the stack is {}".format(s.print_stack()))
	s.pop()
	print("After poping once, the content of the stack is {}".format(s.print_stack()))
	print("The size of the stack is {}".format(s.size()))
	print("The top element in the stack is {}".format(s.peek()))
	print("Max value is {}".format(s.max()))
	s.pop()
	lst = [99, 55, 1]
	[s.push(i) for i in lst] # push values in array lst onto the stack s

	print("\n\nTest2:\nContent of the stack now is {}".format(s.print_stack()))
	[s.pop() for _ in range(2)] # do two popings
	lst = [1000, 231, 88]
	[s.push(i) for i in lst] # push values in array lst onto the stack s
	print("After poping twice, pushing thrice, the content of the stack is {}".format(s.print_stack()))
	print("The size of the stack now is {}".format(s.size()))
	print("The top element in the stack now is {}".format(s.peek()))
	print("Max value now is {}".format(s.max()))

	# timing test between constant time max() and variable time mad_max() 
	s = gen_stack(15)
	print("\nTest3:(run-time test)\nContent of the stack is {}".format(s.print_stack()))
	s_time = time.time()
	print("Using max() method, max value is {}".format(s.max()))
	e_time = time.time()
	print("Elapsed time is {} secs".format((e_time - s_time)*1000))

	s_time = time.time()
	print("\nUsing mad_max() method, max value is {}".format(s.mad_max()))
	e_time = time.time()
	print("Elapsed time is {} secs".format((e_time - s_time)*1000))



if __name__ == '__main__':
	main()

'''
Run-time output:
===============
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_029.py
The followings print the stack content with starting line as bottom and ending line as top of the stack.

Test1:
Content of the stack is 9, 10, 23, 5
After poping once, the content of the stack is 9, 10, 23
The size of the stack is 3
The top element in the stack is 23
Max value is 23


Test2:
Content of the stack now is 9, 10, 99, 55, 1
After poping twice, pushing thrice, the content of the stack is 9, 10, 99, 1000, 231, 88
The size of the stack now is 6
The top element in the stack now is 88
Max value now is 1000

Test3:(run-time test)
Content of the stack is 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377
Using max() method, max value is 377
Elapsed time is 0.03933906555175781 secs

Using mad_max() method, max value is 377
Elapsed time is 0.05364418029785156 secs


(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ pytest codechallenge_029.py
==================================== test session starts =====================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_029.py .                                                                 [100%]

================================== 1 passed in 0.09 seconds ==================================

'''
