'''
Date: 01/17/2019

Problem description:
===================
This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, 
since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.


Algorithm:
==========
Input: A list of numbers
Output: An integer

Pseudo code:
1.  Check for valid input
2.  Write a function to return the sum of elements in a contiguous sub array.
    if the sum is less than 0, return 0.  (I looked up at the Kadane's algorithm for this task and it made just a bit of sense)!
3.  Write a main function that take a given array of numbers and iterate though
    to producw sub arrays.  Feed each sub array to the function in step2 and keep
    track of the returned sum.
    if the returned sum if larger, sum is now the new sum.
4.  return sum
 
'''



#
# return cumulative sum of elements in the array
#
def culmulative_sum(arr=[]):
    if len(arr) == 0:
        return 0
    else:
        cur_sum = arr[0]
        for i in arr[1:]:
            cur_sum += i
        return cur_sum

#
# Feed each sub array into the cumulative_sum function 
# return highest sum among the sub arrays 
# O(n)
#
def highest_sum(arr=[]):
    start,end=0,len(arr)
    j=end
    sum_so_far = 0

    while start < end-1:
        subarr = arr[start:j] 
        print("DBUG--(sub array): {}".format(subarr))
        j-=1

        new_sum = culmulative_sum(subarr)
        if sum_so_far < int(new_sum):
            sum_so_far = int(new_sum)

        if j<start+2:
            start+=1
            j=end

    return sum_so_far

#
# unittest
#
def test_highest_sum():
    A = [34, -50, 42, 14, -5, 86]
    assert highest_sum(A) == 137
    A = [-5, -1, -8, -9, -19]
    assert highest_sum(A) == 0


#
# client programm
#
def main():
    A = [34, -50, 42, 14, -5, 86]
    print("\n\nTest1:\nGiven an array of [{}]".format(', '.join(str(i) for i in A)))
    print("The largest sum of its contiguous subarrays is {}".format(highest_sum(A)))
    A = [-5, -1, -8, -9]
    print("\n\nTest2:\nGiven an array of [{}]".format(', '.join(str(i) for i in A)))
    print("The largest sum of its contiguous subarrays is {}".format(highest_sum(A)))

if __name__ == '__main__':
    main()


'''
Run-time output:
===============
(DailyCodingChallenge-w82MASqp) markn@u17101vaio:~/devel/python-prj/DailyCodingChallenge$ python codechallenge_034.py 


Test1:
Given an array of [34, -50, 42, 14, -5, 86]
DBUG--(sub array): [34, -50, 42, 14, -5, 86]
DBUG--(sub array): [34, -50, 42, 14, -5]
DBUG--(sub array): [34, -50, 42, 14]
DBUG--(sub array): [34, -50, 42]
DBUG--(sub array): [34, -50]
DBUG--(sub array): [-50, 42, 14, -5, 86]
DBUG--(sub array): [-50, 42, 14, -5]
DBUG--(sub array): [-50, 42, 14]
DBUG--(sub array): [-50, 42]
DBUG--(sub array): [42, 14, -5, 86]
DBUG--(sub array): [42, 14, -5]
DBUG--(sub array): [42, 14]
DBUG--(sub array): [14, -5, 86]
DBUG--(sub array): [14, -5]
DBUG--(sub array): [-5, 86]
The largest sum of its contiguous subarrays is 137


Test2:
Given an array of [-5, -1, -8, -9]
DBUG--(sub array): [-5, -1, -8, -9]
DBUG--(sub array): [-5, -1, -8]
DBUG--(sub array): [-5, -1]
DBUG--(sub array): [-1, -8, -9]
DBUG--(sub array): [-1, -8]
DBUG--(sub array): [-8, -9]
The largest sum of its contiguous subarrays is 0
(DailyCodingChallenge-w82MASqp) markn@u17101vaio:~/devel/python-prj/DailyCodingChallenge$ pytest codechallenge_034.py 
===================================== test session starts =====================================
platform linux -- Python 3.6.4, pytest-4.0.2, py-1.7.0, pluggy-0.8.0
rootdir: /home/markn/devel/python-prj/DailyCodingChallenge, inifile:
collected 1 item                                                                              

codechallenge_034.py .                                                                  [100%]

================================== 1 passed in 0.02 seconds ===================================

'''
