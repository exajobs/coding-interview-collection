'''
Date: 01/31/2019

Task description:
=================
This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns 
whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:
[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. 
Similarly, given the target word 'MASS', you should return true, since it's the last row.



Algorithm:
==========
Input: A 2D matrix of single characters, and a string
Output: A booean value

Psuedo code:

1.  Validate input
2.  Choose the shorter dimension to traverse.  
    If row is shorter than column, go up-to-down
    Else if column is shorter, go left-to-right
3.  Join each sub-list to upper-case string.  
    Use the `in list` syntax to match with target string 
4.  For better performance, perhaps wrap step#3 in a insertion list search.

'''


import time

#
# sub function returns boolean on column search
# 
def search_up_to_down(Matrix, target):
	rows = len(Matrix)
	cols = len(Matrix[0])
	for c in range(cols):
		word = ""
		for r in Matrix:
			word += r[c]
		#print("DBUG-- word:{} target:{}".format(word, target))
		if word.upper() == target.upper():
			print("Result: \'{}\' is found in column {}".format(word, c))
			return True
	return False


#
# sub function returns boolean on row search
#
def search_right_to_left(Matrix, target):
	rows = len(Matrix)
	words = ""	
	for i in range(rows):
		word = ''.join(Matrix[i])
		#print("DBUG-- word:{} target:{}".format(word, target))
		if word.upper() == target.upper():
			print("Result: \'{}\' is found in row {}".format(word, i))
			return True
	return False


# 
# Solution1: return True if joined characters by row or column matches the target string
# O(n^2)
#
def matchWordInMatrix(Matrix, target):
	rows = len(Matrix)
	cols = len(Matrix[0])

	if rows < cols:
		# go up-to-down first
		if search_up_to_down(Matrix, target):
			return True
		# go right-to-left
		elif search_right_to_left(Matrix, target):
			return True
	else:
		# go right-to-left first
		if search_right_to_left(Matrix, target):
			return True
		elif search_up_to_down(Matrix, target):
			return True

	
	print("Result: \'{}\' is not found.".format(target))
	return False


#
# (binary search) split at middle and compare
# --not used--
#
def bin_search(L, target):
	start, end = 0, len(L)-1
	L.sort()
	while start <= end:
		mid_idx = (start + end) // 2
		if L[mid_idx] > target:
			end = mid_idx - 1
		elif L[mid_idx] < target:
			start = mid_idx + 1
		else:
			return L[mid_idx]
	return ''

#
# Solution2: Use pythonic method 'in' list, return boolean value on match in matrix
# O(n^2)
#
def findWordinMatrix(Matrix, target):
	rows = len(Matrix)
	cols = len(Matrix[0])

	# go up-to-down
	words_in_cols = []
	for c in range(cols):
		word = ""
		for r in Matrix:
			word += r[c]

		words_in_cols.append(word)

	print("DBUG--words_in_cols: {}".format(words_in_cols))
	if target in words_in_cols:
		print("Result: \'{}\' is found in column {}".format(target, words_in_cols.index(target))) 
		return True

	# go left-to-right
	words_in_rows = []	
	for i in range(rows):
		word = ''.join(Matrix[i])
		words_in_rows.append(word)	
	print("DBUG--words_in_rows: {}".format(words_in_rows))
	if target in words_in_rows:
		print("Result: \'{}\' is found in row {}".format(target, words_in_rows.index(target))) 
		return True
	
	return False
		

#
# unittest
#
def test_matchWordInMatrix():
	Matrix = [['j','a','k','e'],['m','a','n','y'],['r','u','t','h']]
	target = "ruth"
	assert matchWordInMatrix(Matrix, target) == True
	assert findWordinMatrix(Matrix, target) == True
	target = "omma"
	assert matchWordInMatrix(Matrix, target) == False
	assert findWordinMatrix(Matrix, target) == False
	target = "aau"
	assert matchWordInMatrix(Matrix, target) == True
	assert findWordinMatrix(Matrix, target) == True

#
# client program
#
def main():

	print("=== Validation tests ===")
	Matrix = [['m','a','r','k'],['s','h','a','e'],['j','a','n','e']]
	target = "mark"
	print("Test1:\nGiven 2D matrix: {}\nTarget word: \'{}\'".format(Matrix, target))
	matchWordInMatrix(Matrix, target)

	target = "jane"
	print("\nTest2:\nGiven 2D matrix: {}\nTarget word: \'{}\'".format(Matrix, target))
	matchWordInMatrix(Matrix, target)

	target = "polk"
	print("\nTest3:\nGiven 2D matrix: {}\nTarget word: \'{}\'".format(Matrix, target))
	matchWordInMatrix(Matrix, target)
	target = "kee"
	print("\nTest4:\nGiven 2D matrix: {}\nTarget word: \'{}\'".format(Matrix, target))
	matchWordInMatrix(Matrix, target)

	print("\n\n=== Timing tests ===")
	
	s_time = time.time()
	Matrix = [['m','a','r','k'],['s','h','a','e'],['j','a','n','e'],['b','e','a','n'],['j','i','l','l'],['r','o','m','b']]
	target = "romb"
	findWordinMatrix(Matrix, target)
	e_time = time.time()
	ElapsedT1 = e_time - s_time
	print("With (Solution2) findWordinMatrix(), Elapsed time:{} secs.".format(ElapsedT1*1000))
	s_time = time.time()
	target = "romb"
	matchWordInMatrix(Matrix, target)
	e_time = time.time()
	ElapsedT2 = e_time - s_time
	print("With (Solution1) matchWordInMatrix(), Elapsed time:{} secs.\n\nConclusion:".format(ElapsedT2*1000))

	if ElapsedT1 < ElapsedT2:
		print("Solution2 \'findWordinMatrix()\' has better performance!")
	else:
		print("Solution1 \'matchWordInMatrix()\' has better performance!")

	
if __name__ == '__main__':
	main()


'''
Run-time output:
================

(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_040.py

=== validation tests ===
Test1:
Given 2D matrix: [['m', 'a', 'r', 'k'], ['s', 'h', 'a', 'e'], ['j', 'a', 'n', 'e']]
Target word: 'mark'
Result: 'mark' is found in row 0

Test2:
Given 2D matrix: [['m', 'a', 'r', 'k'], ['s', 'h', 'a', 'e'], ['j', 'a', 'n', 'e']]
Target word: 'jane'
Result: 'jane' is found in row 2

Test3:
Given 2D matrix: [['m', 'a', 'r', 'k'], ['s', 'h', 'a', 'e'], ['j', 'a', 'n', 'e']]
Target word: 'polk'
Result: 'polk' is not found.

Test4:
Given 2D matrix: [['m', 'a', 'r', 'k'], ['s', 'h', 'a', 'e'], ['j', 'a', 'n', 'e']]
Target word: 'kee'
Result: 'kee' is found in column 3


=== Timing tests ===
DBUG--words_in_cols: ['msjbjr', 'ahaeio', 'ranalm', 'keenlb']
DBUG--words_in_rows: ['mark', 'shae', 'jane', 'bean', 'jill', 'romb']
Result: 'romb' is found in row 5
With (Solution2) findWordinMatrix(), Elapsed time:0.5400180816650391 secs.
Result: 'romb' is found in row 5
With (Solution1) matchWordInMatrix(), Elapsed time:0.7932186126708984 secs.

Conclusion:
Solution2 'findWordinMatrix()' has better performance!


(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ pytest codechallenge_040.py
=================================== test session starts ===================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_040.py .                                                              [100%]

================================ 1 passed in 0.08 seconds =================================
'''

