'''
Date: 10/18/2019

Problem description:
===================
This problem was asked by Microsoft.
Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.
Given the root to such a tree, write a function to evaluate it.
For example, given the following tree:
    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).

Algorithm:
==========
!!! WARNING:  This is a complex, time consuming interview question.

Assume the tree is not ballanced.  Hence, expect expressions such as 3*4+5 or 3-2+4+5 or 3*4+5*6. 
The root determines where to place the parenthesis.
Topdown tasks: 
	On whiteboard, make the assumption that the rooted tree exists (to save time)
	1. Retrieve
	2. Parse
	3. Evaluate
	Here, we have to construct the tree, fill it before we can get the answer out.
	1. Construct class Tree
	2. Fill
	3. Retrieve
	4. Parse
	5. Evaluate	

Input: a rooted tree containing a mathematical expression
Output: A numer
 
Pseudo code:
1.  Construct a root tree class including insert method
2.  Write a function to traverse and return a string representing the mathematical expression
3.  Import modules SymPy [https://docs.sympy.org/latest/tutorial/manipulation.html#understanding-expression-trees]
4.  Write a function to evaluate the string expression

'''            

import sympy
import ast
import operator as op

class Tree:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.right = right
        self.left = left

    def insert(self, item, ):
        if self.item:
            # left branches
            if self.left is None:
                self.left = Tree(item)
            else:
                self.left.insert(item)

            # right branches
            if self.right is None:
                self.right = Tree(item)
            else:
                self.right.insert(item)

        else:
            # root
            self.item = item


    def tree_to_str(self, mystr=""):
        if self.left:
            self.left.tree_to_str(mystr)
        mystr += str(self.item)
        if self.right:
            self.right.tree_to_str(mystr)

        return mystr

        
def parse_assemble_str(mystr):
    # expect mystr === 3+4*5+6
    # transform to subs = {a:3, b:4, c:5, d:6}
    # and ops = "(a + b) * (c + d)"
    s_cnt = 0
    o_cnt = 0
    symbols = "abcdefghijklmnopqrstuvwxyz"
    sub_str = ""
    for char in mystr:
        if char.isdigit():
            sub_str += symbols[s_cnt]
            sub_str += ':'
            sub_str += str(char)
            sub_str += ','
            s_cnt += 1
        if char.ispace:
            pass
        if char.isalpha():
            ops_str += str(char) + symbols[o_cnt]
    sub_str



# supported operators
operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
             ast.USub: op.neg}

def eval_(node):
    if isinstance(node, ast.Num): # <number>
        return node.n
    elif isinstance(node, ast.BinOp): # <left> <operator> <right>
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    elif isinstance(node, ast.UnaryOp): # <operator> <operand> e.g., -1
        return operators[type(node.op)](eval_(node.operand))
    else:
        raise TypeError(node)


def eval_expr(expr):
    """
    >>> eval_expr('2^6')
    4
    >>> eval_expr('2**6')
    64
    >>> eval_expr('1 + 2*3**(4^5) / (6 + -7)')
    -5.0
    """
    return eval_(ast.parse(expr, mode='eval').body)



def demo_eval_expr(my_expr=[]):

	# define a whitelist of symbols
	a, b, c, d = sympy.symbols('a b c d')

	# let say my_expr = "(2 + 5) * (3 + 9)"
	# construct d_expr = {a:2, b:5, c:3, d:9}
	
	return int(sympy.sympify("(a + b) * (c + d)").evalf(subs={a:2, b:5, c:3, d:9})) 

print(demo_eval_expr())
EXPR=Tree('*')
EXPR.insert(3)
EXPR.insert('+')
EXPR.insert(4)
EXPR.insert(5)
EXPR.insert('+')
EXPR.insert(6)
print(EXPR.tree_to_str())
