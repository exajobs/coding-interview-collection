'''
Date: 12/20/2021
This problem was asked by Google.
Problem Statement:
==================
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

Algorithm:
==========
- Validate input e.g. Array should contain more than one element.
- Sort the array
- Traverse the array, for each element verify that its summation with another element in the array is k
- Return the two elements that add up to k

Implentation:
=============
+ Sequential Algorithm
+ Shorthand Algorithm
'''

# brute force: O(n^2)
def findTwoNumbers(arr, k):
    # This function returns a tuple of two numbers that add up to k
    # arr: a list of numbers
    # k: the number to find in the list
    if k.__str__().isnumeric == False:
        return None

    if len(arr) < 2:
        return None
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == k:
                return (arr[i], arr[j])
    return None


# Shorthand algorythm: O(n)
def shorthandFind2Numbers(arr, k):
   [ print (x,y) for x in arr for y in arr if x + y == k and x != y ]
   return None


if __name__ == '__main__':
    arr = [10, 15, 3, 7]
    k = 17
    print("\nTest#1 (findTwoNumbers): arr={}, k={}".format(arr, k))
    print(findTwoNumbers( arr, k ))  
    arr = [4,7,12,9,33]
    k = 21
    print("\nTest#2 (findTwoNumbers): arr={}, k={}".format(arr, k))
    print(findTwoNumbers( arr, k ))

    print("\nTest#3 (shorthandFind2Numbers): arr={}, k={}".format(arr, k))
    shorthandFind2Numbers( arr, k )