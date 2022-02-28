#!/usr/bin/python3
'''
Date: 12/27/2-18

Problem description:
===================
This problem was asked by Palantir.

Write an algorithm to justify text. Given a sequence of words and an integer 
line length k, return a list of strings which represents each line, fully justified.
More specifically, you should have as many words as possible in each line. There 
should be at least one space between each word. Pad extra spaces when necessary so 
that each line has exactly length k. Spaces should be distributed as equally as 
possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.
Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:
["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly


Algorithm:
==========
Input: a list of words
Output: left aligned pretty printed text
Pseudo code:
for i in range(len(word_list)):
	add lengths of words to be less than or equal k-(word_count-1)
	string up the words separated by 
	separator_len = (k - words_length - word_count)//word_count
	word[i] + ' ' * separator_len
'''

import unittest
def justifyWords(wordlist, k):
	justified_blob = ""
	wordslength = 0
	start_idx = end_idx = 0

	if len(wordlist) == 0:
		raise Exception("Empty wordlist")

	# clone the wordlist (only work in python3.3 or newer!)
	words = wordlist.copy()
	while words:
		if wordslength < k - (end_idx - start_idx) -1:
			try:
				wordslength += len(words.pop(0))
				end_idx+=1
			except IndexError:
				# should be close to end of wordslist
				if wordslength > 0:
					sepa_length = (k - wordslength) // (end_idx - start_idx)
					separator = ' ' * sepa_length
					sentence = separator.join([wordlist[i] for i in range(start_idx, end_idx)])
					if (len(sentence)) < k:
						extra_space = k - wordslength - sepa_length 		
						extras = ' ' * extra_space
						sentence = sentence.replace(' ', extras, 1)
					justified_blob += sentence + '\n'	
					print(sentence)

				break #exit while loop
		else:
			# process the k length of words
			if (k - wordslength) == (end_idx - start_idx)-1:
				sepa_length = 1
			else:
				sepa_length = (k - wordslength) // (end_idx - start_idx)

			separator = ' ' * sepa_length
			sentence = separator.join([wordlist[i] for i in range(start_idx, end_idx)])
			if (len(sentence)) < k:
				extra_space = k - wordslength - sepa_length 		
				extras = ' ' * extra_space
				sentence = sentence.replace(' ', extras, 1)

			justified_blob += sentence + '\n'	
			print(sentence)

			# reset variables
			wordslength = 0
			start_idx = end_idx

	# last few words in the dangling pipe
	if wordslength > 0:
		sepa_length = (k - wordslength) // (end_idx - start_idx)
		separator = ' ' * sepa_length
		sentence = separator.join([wordlist[i] for i in range(start_idx, end_idx)])
		if (len(sentence)) < k:
			extra_space = k - wordslength - sepa_length -1 		
			if extra_space%(end_idx - start_idx) == 1:
				sentence = sentence.replace(' ', '  ', extra_space)
			else:
				extras = ' ' * extra_space
				sentence = sentence.replace(' ', extras, 1)
			
		justified_blob += sentence
		print(sentence)

	return justified_blob

#
# Note: unittest needs  pip3 install pytest
#
class TestJustifier(unittest.TestCase):
	def test_code(self):
		wordlist = []
		k = 16
		justified_blob = '''
the  quick brown
fox   jumps over
the    lazy  dog
'''
		with self.assertRaises(Exception):
			justifyWords(wordlist, k)
   
		#self.assertEqual(justifyWords(wordlist, k), justified_blob)

if __name__ == "__main__":

	wordlist = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
	k = 16
	justifyWords(wordlist, k) 

	print("\n")
	wordlist = ["we", "were", "fools", "to", "make", "war", "against", "our", "brothers", "in" , "arms"]
	k = 16
	justifyWords(wordlist, k) 
 
	unittest.main()

'''
Run-time output:
===============
markn@raspberrypi3:~/devel/py-src/DailyCodeChallenge $ python3 codechallenge-12.py
the  quick brown
fox   jumps over
the    lazy  dog


we were fools to
make war against
our  brothers in
arms
'''
