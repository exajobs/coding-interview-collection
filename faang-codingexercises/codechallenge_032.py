'''
Date: 01/14/2019

Problem description:
===================
This problem was asked by Amazon.
Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.
For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".

Algorithm:
---------
Input: A string
Output: A string representing the longest substring which is a palindrome

Pseudo code:
===========
1.  Check for valid input
2.  change to lower case string
3.  Write a function to validate a palindrome
4.  Write a function to extract all possible substrings that could be a palindrom and feed it to the validating function above.
'''

import unittest
import HtmlTestRunner
import os, time
from unittest.runner import TextTestResult

#
# Check a string for palindrome
# this covers the case of single character.
#
def isPalindrome(instr):
    rev_str = reversed(instr)  # the same as (slice/step) instr[::-1]
    if list(instr) == list(rev_str):
        return True
    else:
        return False

#
# return all possible palindrome strings
#
def all_palindromes(instr):
    start,end=0,len(instr)
    j=end
    results=[]

    while start < end-1:
        temp = instr[start:j] #Time complexity O(k)
        #print("DBUG-- {}".format(temp))
        j-=1

        if isPalindrome(temp):
            results.append(temp)

        if j<start+2:
            start+=1
            j=end

    return list(set(results))


#
# Choose the longest palindrome
#
def longest_palindrome(plist=[]):
    if len(plist) == 0:
        return None
    else:
        return max(plist, key = len)

#
# unittest
#
class Test_isPalindrome(unittest.TestCase):
    def test_longest_palindrome(self):
        self.assertEqual(longest_palindrome(all_palindromes("aabcdcb")), 'bcdcb')
        self.assertEqual(longest_palindrome(all_palindromes("maddashcat")), 'adda')
        self.assertEqual(longest_palindrome(all_palindromes("bananas")), 'anana')
        self.assertEqual(longest_palindrome(all_palindromes("google")), 'goog')
        self.assertEqual(longest_palindrome(all_palindromes("")), None)

#
# client program
#
def main():
    STRINGS = ["aabcdcb", "bananas", "google", "maddashcat", "roleimimi"]
    
    for str in STRINGS:
        print("Given '{}', the longest palindrome is '{}'".format(str, longest_palindrome(all_palindromes(str))))


    STRINGS = ["aabcdcb", "bananas", "google", "maddashcat", "roleimimi"]
    EXPECTED = ["bcdcb", "anana", "goog", "adda", "imimi"] 
    PLINDS = []
    for word in STRINGS:
        PLINDS.append(longest_palindrome(all_palindromes(word)))
    print(PLINDS)    

if __name__ == '__main__':
    if os.environ.get('UNITTEST_ONLY') != 'True':
        main()
    else:
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_reports'))



'''
Run-time output:
===============
$ pipenv run python ./codechallenge_032.py 
Loading .env environment variables...
Given 'aabcdcb', the longest palindrome is 'bcdcb'
Given 'bananas', the longest palindrome is 'anana'
Given 'google', the longest palindrome is 'goog'
Given 'maddashcat', the longest palindrome is 'adda'
Given 'roleimimi', the longest palindrome is 'imimi'
['bcdcb', 'anana', 'goog', 'adda', 'imimi']
...
$ pipenv run python ./codechallenge_032.py 
Loading .env environment variables...

Running tests... 
----------------------------------------------------------------------
 test_longest_palindrome (__main__.Test_isPalindrome) ... OK (0.000000)s
----------------------------------------------------------------------
Ran 1 test in 0:00:00

OK

Generating HTML reports...
test_reports\TestResults___main__.Test_isPalindrome_2022-01-19_17-45-24.html
...

(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_032.py
Given 'aabcdcb', the longest palindrome is 'bcdcb'
Given 'bananas', the longest palindrome is 'anana'
Given 'google', the longest palindrome is 'goog'
Given 'maddashcat', the longest palindrome is 'adda'
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ pytest codechallenge_032.py
=============================== test session starts ===============================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_032.py .                                                      [100%]

============================ 1 passed in 0.11 seconds =============================
'''
