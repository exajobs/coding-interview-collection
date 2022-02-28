'''
Problem statemtent:
===================
Given two strings s1 and s2, check if they are anagrams.
Two strings are named anagrams if they contain the same 
characters with the same frequencies, but not necessarily 
in the same order.  Case does matter.

Exapmle:
S1 = "danger"
S2 = "garden"
Output: True

Frequency of each character in s1 == Frequency of each character in s2
Then, S1 and S2 are anagrams.

'''
from collections import Counter
import unittest
import time
import os
from unittest.runner import TextTestResult
import HtmlTestRunner
#
# solution 1: using Counter.
#
# A Counter is a container that tracks how many times equivalent values are added.
# It can be used to implement the same algorithms for which other languages commonly
# use bag or multiset data structures.  Counter supports three forms of initialization.
# Its constructor can be called with a sequence of items (iterable), a dictionary
# containing keys and counts (mapping, or using keyword arguments mapping string
# names to counts (keyword args).
#
def are_anagrams(S1, S2):
    if len(S1) != len(S2):
        return False
    # use Counter to count the frequency of each character in S1, and then compare it to the frequency of each character in S2
    return Counter(S1) == Counter(S2)
    

#
# solution 2: using a dictionary.
#
# A dictionary is a collection of key-value pairs.  A dictionary in Python is a collection of items accessed by a specific key rather than by index.
# A dictionary is implemented as a hash table, which is a data structure that uses a hash function to compute an index into an array of buckets or slots, 
#
def are_anagrams_dict(S1, S2):
    if len(S1) == len(S2) == 0:
        raise ValueError("Empty string")
    if len(S1) != len(S2):
        return False
    # use a dictionary to count the frequency of each character in S1, and then compare it to the frequency of each character in S2
    d1 = {}
    d2 = {}
    for c in S1:
        if c in d1:
            d1[c] += 1
        else:
            d1[c] = 1
    for c in S2:
        if c in d2:
            d2[c] += 1
        else:
            d2[c] = 1
            
    print(d1)
    print(d2)
    # compare the two dictionaries, return boolean value.
    return d1 == d2    

class TestAnagrams(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))
    
    def test_anagrams(self):
        time.sleep(1)
        self.assertEqual(are_anagrams('danger', 'garden'), True)
        self.assertEqual(are_anagrams_dict('danger', 'garden'), True)    
        self.assertEqual(are_anagrams_dict('spark', 'kraps'), True)
        self.assertEqual(are_anagrams_dict('Roland', 'Dornal'), False)
        with self.assertRaises(ValueError):
            are_anagrams_dict('', '')
        
if __name__ == '__main__':
    if os.environ.get('UNITTEST_ONLY') != 'True':
        S1 = "danger"
        S2 = "garden"
        print(are_anagrams(S1, S2))
        print(are_anagrams_dict(S1, S2))
        S1 = "ROLAND"
        S2 = "DORNAL"
        S2 = "Dnalor"
        print(are_anagrams_dict(S1, S2))
    else:
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_reports'))
        