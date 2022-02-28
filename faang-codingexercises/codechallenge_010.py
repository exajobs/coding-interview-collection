'''
Date: 12/20/2018

Problem description:
====================
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), 
return the original sentence in a list. If there is more than one possible 
reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the 
string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the 
string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] 
or ['bedbath', 'and', 'beyond'].


Assumption:
(*) The first sentence threw me off a bit because I was thinking python.  
Dictionary and list in the same sentence makes me deduce it is a given list of words.

(**) The words are ASCII format...  But will look into utf-8 implementation later.

Algorithm:
=========
Input: list of words
Output: rearanged list of words
Psuedo code:
1.  Check edge cases
2.  Iterate the length of list, use string.find() for locate index of matches
3.  Write indecies into a dictionary. 
4.  Return the sorted values in the dictionary
'''

import collections


def findWord(wordsList, wordString):
	# edge case
	if len(wordsList) == 0 or len(wordString) == 0:
		return None

	dictRetString = {}
	lastpos = 0 #start index of wordString
	for word in wordsList:
		if word in wordString:
			pos = wordString.find(word)  #index position of begining match

			if lastpos > 0:
				if dictRetString[lastpos] in word:
					# strip out any value a substring of another in the list
					# i.e. strip out 'bedbath' in ['bed', 'bedbath', 'bath', 'and', 'beyond']
					pass
				else:
					dictRetString[int(pos)] = str(word)
			else:
				# first match word, take it.
				dictRetString[int(pos)] = str(word)

			lastpos = pos

	# sort the keys 
	sortedDList = collections.OrderedDict(sorted(dictRetString.items()))

	return list(sortedDList.values())



def test_code():
	# test1:
	wList =[ 'quick', 'brown', 'the', 'fox' ] 
	wStr = "thequickbrownfox"
	expected = ['the', 'quick', 'brown', 'fox']
	assert findWord(wList, wStr) == expected

	#test2:  
	words = ['bed', 'bath', 'bedbath', 'and', 'beyond'] 
	string = "bedbathandbeyond"
	expected = ['bed', 'bath', 'and', 'beyond'] 
	assert findWord(words, string) == expected


if __name__ == "__main__":
	wList =[ 'quick', 'brown', 'the', 'fox' ] 
	wStr = "thequickbrownfox"
	expected = ['the', 'quick', 'brown', 'fox']
	print("Given\nA word list: {} and a string: {}".format(wList, wStr))
	print("Words reconstruction: {}\n".format(findWord(wList, wStr)))

	words = ['bed', 'bath', 'bedbath', 'and', 'beyond'] 
	string = "bedbathandbeyond"
	expected = ['bed', 'bath', 'and', 'beyond'] 
	print("Given\nA word list: {} and a string: {}".format(words, string))
	print("Words reconstruction: {}\n".format(findWord(words, string)))


'''
Run-time output:
===============
$ python codechallenge-10.py                       
Given
A word list: ['quick', 'brown', 'the', 'fox'] and a string: thequickbrownfox
Words reconstruction: ['the', 'quick', 'brown', 'fox']

Given
A word list: ['bed', 'bath', 'bedbath', 'and', 'beyond'] and a string: bedbathandbeyond
Words reconstruction: ['bed', 'bath', 'and', 'beyond']


$ pytest codechallenge-10.py                       
========================================= test session starts ==========================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodeChallenge, inifile:
collected 1 item

codechallenge-10.py .                                                                            [100%]

======================================= 1 passed in 0.08 seconds =======================================
'''
