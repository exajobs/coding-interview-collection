'''
Date: 12/28/2018

Problem description:
====================
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic 
idea is to represent repeated successive characters as a single count and character. 

For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
Implement run-length encoding and decoding. You can assume the string to be encoded 
have no digits and consists solely of alphabetic characters. You can assume the string 
to be decoded is valid.

Algorithm:
=========
Input: A string
Output: a string
Pseudo code:
1.  Check edge cases
2.  import re
3.  use list comprehension to concatinate second and first items from re.findall()
4.  append length of item with value of item for each item in the resulted list
5.  return the appended string 
'''

import re
def encode(instr):
	encoded_str = ""
	if len(instr) == 0:
		return None
	else:
		# given instr="AAAABBOORRWMSSS"
		# list comprehension [match[1] + match[0] for match in re.findall(r'(.)(\1*)', instr)]
		# should produce a list: ['AAA'+'A', 'B'+'B', 'O'+'O', 'R'+'R', 'W'+'', 'M'+'', 'SS'+'S']
		# which is ['AAAA', 'BB', 'OO', 'RR', 'W', 'M', 'SSS']

		matches = [match[1] + match[0] for match in re.findall(r'(.)(\1*)', instr)]
		for i, s in enumerate(matches):
			encoded_str += str(len(s))+s[0]
	return encoded_str

def decode(instr):
	decoded_str = ""
	if len(instr) == 0:
		return None
	else:
		for i in range(0, len(instr), 2):
			decoded_str += ''.join([str(instr[i+1]) for x in range(int(instr[i]))])
	return decoded_str

def test_code():
	S="AAAABBOORRWMSSS"
	EncodedS="4A2B2O2R1W1M3S"
	assert encode(S) == EncodedS

	S="2222000077DD999AAAABBOORRWMSSS"
	EncodedS="4240272D394A2B2O2R1W1M3S"
	assert encode(S) == EncodedS

	EncodedS="4A2B2O2R1W1M3S"
	S="AAAABBOORRWMSSS"
	assert decode(EncodedS) == S

if __name__ == "__main__":	
	STR = "99999000022222AAAA888FFTTPPPQQQSSSVVVZZZZZZZ"
	print("Text: {}\nEncode text: {}\nDecoded text: {}".format(STR, encode(STR), decode(encode(STR))))


'''
Run-time output:
===============
markn@raspberrypi3:~/devel/py-src/DailyCodeChallenge $ python codechallenge-13.py
Text: 99999000022222AAAA888FFTTPPPQQQSSSVVVZZZZZZZ
Encode text: 5940524A382F2T3P3Q3S3V7Z
Decoded text: 99999000022222AAAA888FFTTPPPQQQSSSVVVZZZZZZZ

markn@raspberrypi3:~/devel/py-src/DailyCodeChallenge $ pytest codechallenge-13.py
=================================== test session starts ====================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodeChallenge, inifile:
collected 1 item

codechallenge-13.py .                                                                [100%]

================================= 1 passed in 0.08 seconds =================================
markn@raspberrypi3:~/devel/py-src/DailyCodeChallenge $
'''
