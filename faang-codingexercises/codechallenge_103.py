'''
This problem was asked by Twitter.

Problem statement:
==================
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

-  record(order_id): adds the order_id to the log
-  get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.

Fore thought:
============
Data structures in this case is used for the Relational Database Management System (Array of structure). so, possible structure where all entries 
must be of the same data type such as list can be classified into linear and non-linear data structures.
Although not the best at efficency, linear data structures contain Stacks and Queues fits the requiremnts.
Otherwise, non-linear data structure such as a hash table would be more efficient.

Stack is a container of objects that can be inserted or removed according to LIFO (Last in First Out) pop() method is used during disposal in Python
Should we use a stack?  Built-in list is a stack.  So, it is still a list.  The biggest issue is that it can run into speed issues as it grows. The items in a list are stored with the goal of providing fast access to random elements in the list. At a high level, this means that the items are stored next to each other in memory.
If your stack grows bigger than the block of memory that currently holds it, then Python needs to do some memory allocations. This can lead to some .append() calls taking much longer than other ones.
There is a less serious problem as well. If you use .insert() to add an element to your stack at a position other than the end, it can take much longer. 
We should never use list for any data structure that can be accessed by multiple threads. list is not thread-safe.

Next best thing is a queue.  A queue is a FIFO (First in First Out) data structure.  It is a linear data structure that can be accessed by multiple threads.
Still, both stacks and queues are stored in blocks of contiguous memory.  

Fortunately, the constant time .append() and .pop() operations make deque an excellent choice for implementing a Python stack if your code doesn’t use threading.
While the built-in library interface for list and deque were similar, LifoQueue uses .put() and .get() to add and remove data from the stack.

Implementations:
----------------
1.  Bruteforce approach: Singly linked list
2.  Use a stack to store the last N order_ids
3.  Use a queue to store the last N order_ids
4.  Use a deque to store the last N order_ids
'''
import unittest
import random
import collections
import time
import os
import HtmlTestRunner

# ----------------------------------
# Brute force -- Singly linked list:
#-----------------------------------
class SlRecord(object):
    def __init__(self, record_id=None, next_record=None):
        self.record_id = record_id
        self.next_record = next_record
#
# add a record to the end of the linked list: O(n)
#
def addRecord(head, record_id):
    if head is None:
        head = SlRecord(record_id)
        return head
    curr = head
    while curr.next_record is not None:
        curr = curr.next_record
    curr.next_record = SlRecord(record_id)
    return head

#
# Traverse the linked list and return the record at index i: O(n)
#
def getRecord(head, idx):
    if head is None:
        return None
    curr = head
    while curr.next_record is not None and idx > 0:
        curr = curr.next_record
        idx -= 1
    return curr.record_id

#
# Traverse the linked list and return the last record: O(n)
#
def getLastRecord(head):
    if head is None:
        return None
    curr = head
    while curr.next_record is not None:
        curr = curr.next_record
    return curr.record_id

#
# Randomly generate a number of length n, prepend with 'O-'
#
def generate_order_id(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return 'O-{}'.format(random.randint(range_start, range_end))  

#
# Unit test:
#
class TestOrderLog(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    # run all test methods                
    def test_MultiLog(self):
        time.sleep(1)
        test_SinlglyLinkedList()
        time.sleep(1)
        test_Stack()
        time.sleep(1)
        test_Queue()
    # test the singly linked list implementation
    def test_SinglyLinkedList(self):
        time.sleep(1)
        test_SinlglyLinkedList()
    # test the stack implementation
    def test_Stack(self):    
        time.sleep(1)
        test_Stack()
    # test the queue implementation
    def test_Queue(self):
        time.sleep(1)
        test_Queue()

        
def test_SinlglyLinkedList():
    order_log = SlRecord()
    for i in range(1000):
        order_log = addRecord(order_log, generate_order_id(10))
    print("Unit test (Singly linked list):")
    print("\tRecordID at Idx#3:" , getRecord(order_log, 3))
    print("\tLast recordID: ", getLastRecord(order_log))
    
def test_Queue():
    order_log = collections.deque()
    for i in range(1000):
        order_log.append(generate_order_id(10))
    print("Unit test (Queue):")
    print("\tRecordID at Idx#500:" , order_log[500])
    print("\tLast recordID: ", order_log.pop())

def test_Stack():
    sLog = []
    for i in range(1000):
        sLog.append(generate_order_id(10))
    print("Unit test (Stack):")
    print("\tLast recordID: ", sLog[-1])


class TestQueue(unittest.TestCase):
    def test_Queue(self):
        test_Queue()
class TestStack(unittest.TestCase):
    def test_Stack(self):
        test_Stack()
    
if __name__ == '__main__':
    if os.environ.get('UNITTEST_ONLY') != 'True':
        # non-unit tests
        slLog = SlRecord()
        for i in range(10):
            slLog = addRecord(slLog, generate_order_id(50))
        print("Test#1 (Singly linked list):")
        print("\t", getLastRecord(slLog))
        
        # dequeue:
        qLog = collections.deque()
        for i in range(10):
            qLog.append(generate_order_id(50))
        print("Test#2 (Queue):")
        print("\t", qLog[-1])
        
        # stack:
        sLog = []
        for i in range(10):
            sLog.append(generate_order_id(50))
        print("Test#3 (Stack):")
        print("\t", sLog[-1])
        print()
        
    else:
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_reports'))

        #  # read the htlm output path from environment variable. e.g. local .env file.
        # html_report_path = os.environ['HTML_REPORT_PATH']
        # testRunner=HtmlTestRunner.HTMLTestRunner(output=html_report_path, report_title='Test Report for codechallenge_103.py')
        # test_suite = unittest.TestSuite()
        # unittest.TextTestRunner(verbosity=0).run(test_suite)
        
        # all_test = unittest.makeSuite(TestOrderLog)
        # test_suite.addTest(all_test)
        # test_suite.addTest(TestOrderLog("test_Stack")) 
        # test_suite.addTest(TestOrderLog("test_Queue"))
        # unittest.main(testRunner.run(test_suite)) 

         
'''
Run-time output:
===============

D:\devel\git\DailyCodingChallenge> pipenv run python .\codechallenge_103.py
Loading .env environment variables...
Unit test (Singly linked list):
        RecordID at Idx#3: O-9488088207
        Last recordID:  O-9025266467   
Unit test (Stack):
        Last recordID:  O-6591925839
Unit test (Queue):
        RecordID at Idx#500: O-4837286473 
        Last recordID:  O-5362379084      
__main__.TestOrderLog.test_MultiLog: 3.057
Unit test (Queue):
        RecordID at Idx#500: O-9615193617
        Last recordID:  O-6697089552     
__main__.TestOrderLog.test_Queue: 1.001  
Unit test (Singly linked list):
        RecordID at Idx#3: O-1433269688
        Last recordID:  O-3696427905
__main__.TestOrderLog.test_SinglyLinkedList: 1.042
Unit test (Stack):
        Last recordID:  O-8051504149
__main__.TestOrderLog.test_Stack: 1.011
----------------------------------------------------------------------
Ran 4 tests in 6.106s

OK

Running tests...
----------------------------------------------------------------------
 test_MultiLog (__main__.TestOrderLog) ... OK (3.042136)s
 test_Queue (__main__.TestOrderLog) ... OK (1.001401)s
 test_SinglyLinkedList (__main__.TestOrderLog) ... OK (1.017831)s
 test_Stack (__main__.TestOrderLog) ... OK (1.005817)s
 test_Stack (__main__.TestOrderLog) ... OK (1.010090)s
 test_Queue (__main__.TestOrderLog) ... OK (1.009727)s

----------------------------------------------------------------------
Ran 6 tests in 0:00:08

OK



Generating HTML reports...
test_reports\TestResults___main__.TestOrderLog_2022-01-04_21-41-46.html
Unit test (Singly linked list):
        RecordID at Idx#3: O-7905126100
        Last recordID:  O-6590755604
Unit test (Stack):
        Last recordID:  O-6961104592
Unit test (Queue):
        RecordID at Idx#500: O-7933390793
        Last recordID:  O-8689457315
__main__.TestOrderLog.test_MultiLog: 3.060
.Unit test (Queue):
        RecordID at Idx#500: O-1287470987
        Last recordID:  O-6002949287
__main__.TestOrderLog.test_Queue: 1.002
.Unit test (Singly linked list):
        RecordID at Idx#3: O-6167847554
        Last recordID:  O-6331368071
__main__.TestOrderLog.test_SinglyLinkedList: 1.042
.Unit test (Stack):
        Last recordID:  O-3799353418
__main__.TestOrderLog.test_Stack: 1.001
.
----------------------------------------------------------------------
Ran 4 tests in 6.136s

OK

'''    
    