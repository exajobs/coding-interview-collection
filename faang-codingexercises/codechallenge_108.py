'''
Problem statement:
==================
Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.

Constraints:
============
k == lists.length
lists[i] is sorted in ascending order.


Examples:
=========
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Input: lists = [[],[1],[2,3,4,5,6]]
Expected output: ['1'->'2'->'3'->'4'->'5'->'6']

'''

import unittest
import HtmlTestRunner
import os, time
from unittest.runner import TextTestResult

#
# using the + operator
#
def mergeSlists(lists):
    if len(lists) == 0:
        return None
    elif len(lists) == 1:
        return lists[0]
    else:
        for l in lists:
            if l is None:
                lists.remove(l)
        ret = lists[0] + mergeSlists(lists[1:])

        return sorted(ret, key = int)

def main():
    L1 = ['5','1','3','2','4']
    L2 = ['8','10','9','11','7','-11']
    mergedList = sorted([*L1, *L2], key = int)
    print(mergedList)
    print(mergeSlists([[5,1,3,2,4], [8,10,9,11,7], [-1, -2, -3, -4, -5]]))
    print(mergeSlists(lists = [[],[1],[2,3,4,5,6]]))

class TestMergeSortedLists(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))
        
    def test_kSortedList(self):
        time.sleep(1)
        self.assertEqual(mergeSlists([[5,1,3,2,4], [8,10,9,11,7], [-1, -2, -3, -4, -5]]), [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11])
        time.sleep(1)
        self.assertEqual(mergeSlists(lists = [[],[1],[2,3,4,5,6]]), [1,2,3,4,5,6]) 

if __name__ == '__main__':
    if os.environ.get('UNITTEST_ONLY') != 'True':
        main()
    else:
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_reports'))    


'''
Output:
======
#
# python3 codechallenge_108.py main()
#
PS D:\devel\GIT\DailyCodingChallenge> pipenv run python .\codechallenge_108.py
Loading .env environment variables...
['-11', '1', '2', '3', '4', '5', '7', '8', '9', '10', '11']
[-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
[1, 2, 3, 4, 5, 6]

#
# python3 codechallenge_108.py unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_reports'))
#
PS D:\devel\GIT\DailyCodingChallenge> pipenv run python .\codechallenge_108.py
Loading .env environment variables...

Running tests... 
----------------------------------------------------------------------
 test_kSortedList (__main__.TestMergeSortedLists) ... OK (0.000000)s
----------------------------------------------------------------------
Ran 1 test in 0:00:00
OK
Generating HTML reports...
test_reports\TestResults___main__.TestMergeSortedLists_2022-01-25_15-17-14.html
'''