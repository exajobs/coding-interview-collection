'''
Problem statement:
==================
Implement the Fibonacci sequence using linear algerbra eigenvetor and matrices.

Assume F0 = 0 and F1 = 1.  Fk+1 = Fk + Fk-1

Algerbracal eigenvector:
========================
    u1 = [[1,1],[1,0]]
    uk+1 = [[1,1],[1,0]] * uk
i.e.    
    u1 = [[1,1],[1,0]]
    u2 = [[1,1],[1,0]] * u1
    u3 = [[1,1],[1,0]] * u2
    
'''

import numpy as np
import math
import unittest, os, time, HtmlTestRunner

lmbd_1 = (1 + np.sqrt(5))/2
lmbd_2 = (1 - np.sqrt(5))/2

a = np.matrix([[1,1],[1,0]])
s = np.matrix([[lmbd_1, lmbd_2],[1, 1]])
s_inv = np.matrix([[1, -lmbd_2],[-1, lmbd_1]]) * (1/np.sqrt(5))
eig_val = np.matrix([[lmbd_1, 0], [0, lmbd_2]])
u_0 = np.matrix([[1],[0]])

def eigen_vector_k(k):
    return eig_val ** k

def u_k(k):
    return s * eigen_vector_k(k) * s_inv * u_0

def fib(n):
    f_n = u_k(n)[1,0]
    return int(round(f_n))

class FiboForLarge:
    def __init__(self, start_val, k):
        self.start_val = start_val
        self.k = k
        self.k_vals = fib_next_k(start_val, k)
        
    def __str__(self):
        return str(self.k_vals)
    
    def fib_this(self, start_val):
        return int(round(start_val * 1.61803))
    
    def fib_for_k(self, k):
        return [self.k_vals.append(fib_this(self.k_vals[i])) for i in range(k)]
    
#
# using the golden ratio, to achieve relative accuracy on LARGE numbers in the fib sequence
#
def fib_w_goldenratio(n):
    # ref: https://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form
    # Computing a large Fn using the golden ratio: eigenvalue=1.61803
    return int(round(n * 1.61803))

#
# given a large starting value, compute the next k values in the fibonacci sequence
#
def fib_next_k(start_val, k):
    k_vals = []
    k_vals.append(fib_w_goldenratio(start_val))
    [k_vals.append(fib_w_goldenratio(k_vals[i])) for i in range(k)]
    return k_vals
        

class TestFibonacci(unittest.TestCase):
    def test_fib_next_k(self):
        self.assertEqual(fib_w_goldenratio(218922995834555138048), 354223974950185271296)
        #self.assertEqual(fib_next_k(7540113804746344448, 5), [12200130339493728256, 19740176893211037696, 31940198418522255360, 51680199247121563648])
        #self.assertEqual(fib_next_k(218922995834555138048, 10), [354223974950185271296, 354223974950185271296, 354223974950185271296, 354223974950185271296, 354223974950185271296, 354223974950185271296, 354223974950185271296, 354223974950185271296, 354223974950185271296, 354223974950185271296])

if __name__ == '__main__':
    if os.environ.get('UNITTEST_ONLY') != 'True':
        [print(fib(i)) for i in range(100)]
        print(fib_w_goldenratio(218922995834555138048))
        print()
        print(fib_next_k(7540113804746344448, 5))
        print()
        print(fib_next_k(218922995834555138048, 10))
    else:
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_reports'))
    