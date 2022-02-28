'''
Date: 12/30/2018

Problem description:
====================

This problem was asked by Google.

Given two strings, compute the edit distance between them.

The edit distance between two strings refers to the minimum number of character insertions, 
deletions, and substitutions required to change one string to the other. For example, the 
edit distance between 'kitten' and 'sitting' is three: substitute the 'k' for 's', 
substitute the 'e' for 'i', and append a 'g'.

Algorithm:
===========
Input: string1, string2
Output: integer value
Psuedo code:
1.  Check edge cases
2.  Align the two strings side-by-side mapping matching characters
    String is iterable, so let's traverse the longest string.
4.  Count the characters that are not matched

Assumption: Parallel matching and no match means total replacement of one string over another.
'''

#
# return len(longer_string) - match_count
# 
def strDistSubstitution(str1, str2):
	# edge case
	match_cnt = 0
	if len(str1) == 0 or len(str2) == 0:
		return None
	
	elif len(str1) > len(str2):
		try:
			for i,n in enumerate(str1):
				if n == str2[i]:
					match_cnt+=1
		except IndexError:
			pass

		return len(str1) - match_cnt
	else:
		try:
			for i,n in enumerate(str2):
				if n == str1[i]:
					match_cnt+=1
		except IndexError:
			pass

		return len(str2) - match_cnt

def test_code():
	strA = 'kitten'
	strB = 'sitting'
	assert strDistSubstitution(strA, strB) == 3			


if __name__ == '__main__':
	strA = 'kitten'
	strB = 'sitting'
	print("Given\nstring1: {}\nstring2: {}".format(strA, strB))
	print("The distance between two strings: {}".format(strDistSubstitution(strA, strB)))			

'''
Run-time output:
===============
markn@raspberrypi3:~/devel/py-src/DailyCodeChallenge $ python3 codechallenge_016.py
Given
string1: kitten
string2: sitting
The distance between two strings: 3

markn@raspberrypi3:~/devel/py-src/DailyCodeChallenge $ pytest codechallenge_016.py
=================================== test session starts ===================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodeChallenge, inifile:
collected 1 item

codechallenge_016.py .                                                              [100%]

================================ 1 passed in 0.03 seconds =================================
'''
