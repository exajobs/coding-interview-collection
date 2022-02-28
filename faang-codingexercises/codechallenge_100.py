#!/bin/python3
'''
Date: 12/19/2021
This problem was asked by HackerRank.
Problem Statement: 
=================
Given the array of numbers, and a number k, return 'YES' if k exists in the array and 'No' otherwise.

Algorithm:
==========
- Validate input 
- Sort the array
- Traverse the array and check if k exists in the array
- Return 'YES' or 'NO'

Implentation:
=============
+ Sequential Algorithm
+ Shorthand Algorithm

'''
import os
import unittest
import time
import HtmlTestRunner
# Sequential Algorithm O(n)
def findNumberSequentialSearch(arr, k):
    # This function returns a STRING of 'YES' or 'NO'
    # arr: a list of numbers
    # k: the number to find in the list
    start, end = 0, len(arr)-1
    if len(arr) == 0:
        return 'NO'

    arr.sort()
    for i in range(len(arr)):
        if arr[i] == k:
            return 'YES'
    return 'NO'


# Shorthand Algorithm: O(n)
def shorthandFindNumber(arr, k):
    # This function returns a STRING of 'YES' or 'NO'
    # arr: a list of numbers
    # k: the number to find in the list
    return 'YES' if k in arr else 'NO'

#
# unittest
#
class TestFindNumber(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    def test_FindNumber(self):
        arr = [1,2,3,4,5,6,7,8,9]
        k = 1
        self.assertEqual(findNumberSequentialSearch(arr, k), 'YES')
        self.assertEqual(shorthandFindNumber(arr, k), 'YES')

    

if __name__ == '__main__':
    if os.environ['UNITTEST_ONLY'] != 'True':
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        k = 6
        print("\nTest#1: arr={}, k={}".format(arr, k))
        shorthandFindNumber(arr, k)
        arr = []
        k = 10
        print("\nTest#2: arr={}, k={}".format(arr, k))
        shorthandFindNumber(arr, k)
        arr = [21, 12, 73, 34, 85, 16, 97, 58, 29, 10]
        k = '0x10'
        print("\nTest#3: arr={}, k={}".format(arr, k))
        findNumberSequentialSearch(arr, k)
        k = 29
        print("\nTest#4: arr={}, k={}".format(arr, k))
        findNumberSequentialSearch(arr, k)
    else:
        # read the htlm output path from environment variable. e.g. local .env file.
        html_report_path = os.environ['HTML_REPORT_PATH']
        testRunner=HtmlTestRunner.HTMLTestRunner(output=html_report_path, report_title='Test Report for codechallenge_100.py')
        
        test_suite = unittest.TestSuite()
        unittest.TextTestRunner(verbosity=0).run(test_suite)
        all_test = unittest.makeSuite(TestFindNumber)
        test_suite.addTest(all_test)
        unittest.main(testRunner.run(test_suite))
        unittest.main(TestFindNumber.test_FindNumber)