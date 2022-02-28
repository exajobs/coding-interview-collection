'''
Date:01/03/2019

Problem description:
===================
This problem was asked by Quora.

Given a string, find the palindrome that can be made by inserting the fewest number of characters 
as possible anywhere in the word. If there is more than one palindrome of minimum length that can 
be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters 
to it (which is the smallest amount to make a palindrome). There are seven other palindromes that 
can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.
As another example, given the string "google", you should return "elgoogle".


Algorithm:
==========
Input: A string
Output A palindrome string
Pseudo code:
1.  Check for valid input

2.  Check if the string has consecutively repeated chars
    If yes.  Handle the complex case of 'oo' in the word 'google' (step3 below).

    Else, make the smallest amount of work in making a palindrome.  i.e. 
	copy the string into another, reverse the order of the new string and pop the last item
	prepend the new string to the original string and we have ourselve a palindrome.

3.  Handling the complex case:
    3.1 Iterate the string from middle index toward the end
    3.2 compare the mirrored characters, prepend mirrored character if not a match. 
  	If not yet a palindrome, keep prependng a mirrored character to the beginning of the string and 
	go back to check it again.  This ahould be verry intuitive once you had pictured it in your head.


Further thoughts:
================
What happens if input is already a palindrome?
'''
import re

#
#  Check if the string has consecutively repeated chars
#  return True if there are repeated chars in instr
#
def isRepeatedChars(instr):
	# e.g. See the interactive python result here:
	'''
	>>> instr = 'google'
	>>> repchars = [s[1] + s[0] for s in re.findall(r'(.)(\1*)', instr)]
	>>> repchars
	['g', 'oo', 'g', 'l', 'e']
	'''
	repchars = [s[1] + s[0] for s in re.findall(r'(.)(\1*)', instr)]
	try:
		# locate the consecutively repeated characters
		midstr = [i for i in repchars if len(i) > 1][0]
		return (len(midstr) > 0)
	except IndexError:
		return False

#
# use re.findall() method to find middle index+offset
# this allows us to deal with words such as 'oo' in 'google'
# return start and end indices of the consecutively repeated characters substring: 
#    Starting index of the repeated character
#    Ending index of the repeated character
#    e.g. return  None, None
#         return 1, 2
#
def idxOfRepeatedChars(instr):
	# Find repeated chracters by converting string into an array of characters
	repchars = [s[1] + s[0] for s in re.findall(r'(.)(\1*)', instr)]

	try:
		# locate the consecutively repeated characters
		# it should be where length of item is greater than one
		# e.g. if instr='google', midstr should be 'oo'
		midstr = [i for i in repchars if len(i) > 1][0]

		if len(midstr) > 0:
			# find index of this midstr above and its offset
			mididx = instr.index(midstr)
			return int(mididx), int(mididx+len(midstr)-1)
		else:
			return None, None
	except IndexError:
		return None, None

#
# decorator function
#
def palindrome(func):
	def inner(*args):
		instr = args[0]
		mididx = len(instr)//2

		# iterate from edge toward middle
		ret = False
		for i in range(mididx):
			if instr[i] == instr[-1 + (i * -1)]:
				ret  = True
			else:
				return False
		return ret
	return inner
		
#
# validate that the string is a palindrome
#
@palindrome
def isValidPalindrome(instr):
	if len(instr) == 0:
		return False
	# remove any extra white space tat both ends
	instr.strip()

	return palindrome(instr)

#
# Create a palindrome string
#
def getPalindrome(instr):
	if not instr.isalpha():
		return "Invalid input.  Not an alphabetic string"

	# in case it is already a palindrome.  just return it!
	if isValidPalindrome(instr):
		return instr

	if isRepeatedChars(instr):
		# found consecutively repeated characters such as 'oo' in 'google'
		# deal with the offset index

		startidx, endidx = idxOfRepeatedChars(str(instr))
		#print("DBUG: instr:{} startidx:{} endidx:{}".format(instr, startidx, endidx))			
		# iterate from middle toward edge 
		# e.g.
		# 0  1  2  3  4  5
		# g  o  o  g  l  e
		# startidx:1, endidx:2
		count = 1
		for i in range(endidx+1, len(instr)+1, 1):
			if instr[i] == instr[startidx - count]:
				pass
			else:
				instr = instr[:0] + instr[i] + instr[0:]
			count+=1
	else: # remaining cases such as word 'race'
		halfidx = len(instr)//2

		# iterate from edge toward middle
		# e.g.
		# from 0 .. halfidx
		flipchars = list(instr)
		flipchars.reverse() 
		flipchars.pop()
		flipstr = ''.join(flipchars)
		instr = instr[:0] + flipstr + instr[0:]


	#print(instr)
	return instr
#
# unittest fucntion
#
def test_palindrome():
	A='google'
	assert getPalindrome(A) == 'elgoogle'
	A = 'race'
	assert getPalindrome(A) == 'ecarace'

#
# client function
#
if __name__ == '__main__':
	A='google'
	print("Test1:\nInput: {}".format(A))
	PalindStr = getPalindrome(A)
	print("Output: {}".format(PalindStr))
	print("Validate palindrome string: \'{}\' as {}.".format(PalindStr, isValidPalindrome(PalindStr)))

	A='race'
	print("\nTest2:\nInput: {}".format(A))
	PalindStr = getPalindrome(A)
	print("Output: {}".format(PalindStr))
	print("Validate palindrome string: \'{}\' as {}.".format(PalindStr, isValidPalindrome(PalindStr)))

	A='ABBA'
	print("\nTest3:\nInput: {}".format(A))
	PalindStr = getPalindrome(A)
	print("Output: {}".format(PalindStr))
	print("Validate palindrome string: \'{}\' as {}.".format(PalindStr, isValidPalindrome(PalindStr)))

	A='bananas'
	print("\nTest3:\nInput: {}".format(A))
	PalindStr = getPalindrome(A)
	print("Output: {}".format(PalindStr))
	print("Validate palindrome string: \'{}\' as {}.".format(PalindStr, isValidPalindrome(PalindStr)))
'''
Run-time output:
================
linux1@sles12sp3:/data/devel/py-src/DailyCodingChallenge> python codechallenge_019.py
Test1:
Input: google
Output: elgoogle
Validate palindrome string: 'elgoogle' as True.

Test2:
Input: race
Output: ecarace
Validate palindrome string: 'ecarace' as True.

Test3:
Input: ABBA
Output: ABBA
Validate palindrome string: 'ABBA' as True.

'''

