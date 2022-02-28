'''
Date: 01/25/2019

Problem description:
====================
This problem was asked by Amazon.

Given a string s and an integer k, break up the string into multiple texts such that 
each text has a length of k or less. You must break it up so that words don't break 
across lines. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is 
exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, 
you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. 
No string in the list has a length of more than 10.


Algorithm:
==========
Input: A string, and an integer
Output: An array containing substrings

Psuedo code:

1.  Validate input
2.  Split the string into a list using white space as the delimiter
3.  While the list is not empty, pop item from its front and append to a substring until the substring is equal or grater than k
4.  If the length of the substring is less than k, yield it
	Else, remove the last item from the substring, insert it back to the top of the list, yield the substring.
5.  Return an array of substrings from the generator above.
'''

#
# generator that yields substring with length less than or equal to k
#
def gen_subString(instr, k):
	substrlst = instr.split(' ')
	tempstr = ""
	last_str = ""
	while len(substrlst) > 0:
		while len(tempstr) < k:
			try:
				last_str = substrlst.pop(0)
				tempstr += ' '
				tempstr += str(last_str)
			except IndexError:
				break

		#print("DBUG-- tempstr:{}".format(tempstr.strip()))
		if len(tempstr.strip()) > k:
			yield tempstr.rstrip(last_str).strip()
			substrlst.insert(0, last_str)
			tempstr = ""
		else:
			yield tempstr.strip()
			tempstr = ""		

#
# return array of subsrings having length <= k
#			
def scrape_string(instr, k):
	if len(instr) == 0 or type(k) is not int:
		return None
	if k > len(instr):
		return None

	iter_str = gen_subString(instr, k)
	return [item for item in iter_str]




#
# unittest
#
def test_clipped_strs():
	str = "Penny Lane is in my ears and in my eyes"
	k = 11
	expected_str = ['Penny Lane', 'is in my', 'ears and in', 'my eyes']
	assert scrape_string(str, k) == expected_str
	k = len(str)+1000
	assert scrape_string(str, k) == None
	str = ""
	assert scrape_string(str, k) == None


#
# client program
#
def main():
	str = "The not so smart fox jumped over the fence into the pond"
	k = 10
	print("Test1:\nGiven a string '{}' and k={}\nThe spliced string array with each element having length less than or equal to k is".format(str, k))
	print(scrape_string(str, k))

	str = "Penny Lane is in my ears and in my eyes"
	k = 11
	print("\nTest2:\nGiven a string '{}' and k={}\nThe spliced string array with each element having length less than or equal to k is".format(str, k))
	print(scrape_string(str, k))

	str = "Mary has a little lamb"
	k = len(str)
	print("\nTest3:\nGiven a string '{}' and k={}\nThe spliced string array with each element having length less than or equal to k is".format(str, k))
	print(scrape_string(str, k))

if __name__ == '__main__':
	main()


'''
Run-time output:
===============
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_038.py
Test1:
Given a string 'The not so smart fox jumped over the fence into the pond' and k=10
The spliced string array with each element having length less than or equal to k is
['The not so', 'smart fox', 'jumped', 'over the', 'fence into', 'the pond']

Test2:
Given a string 'Penny Lane is in my ears and in my eyes' and k=11
The spliced string array with each element having length less than or equal to k is
['Penny Lane', 'is in my', 'ears and in', 'my eyes']

Test3:
Given a string 'Mary has a little lamb' and k=22
The spliced string array with each element having length less than or equal to k is
['Mary has a little lamb']

(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ pytest codechallenge_038.py
======================================= test session starts ========================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_038.py .                                                                       [100%]

===================================== 1 passed in 0.07 seconds =====================================

'''
