'''
Date: 01/05/2020

This problem was asked by Google.
Problem description:
====================
Suppose we represent our file system by a string in the following manner:
The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
        
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

`print("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")`

Level   Name
-----   ----
0       dir
1           subdir1
2               file1.ext           <-- this qualifies as an absolute path to a file
2               subsubdir1          <-- this qualifies as a path to a folder
1           subdir2
2               subsubdir2
3                   file2.ext       <-- this qualifies as a path
            
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

Note:
=====
The name of a file contains at least a period and an extension.  Hmmm, what about a file with no extension?
The name of a directory or sub-directory will not contain a period.  Hmmm, what about a directory with periods in its name?


Algorithm:
==========
1.  Validate input
2.  Tokenize the input string where the delimeter is '\n'.  Determine directory level by equating the number of leading tabs.
3.  Strip the leading tabs and spaces from each token, append a '/' if it is a directory
4.  Concatenate the tokens into a list of strings, each string representing an absolute path will end with at least a period and an extension.
5.  Compare the length of each string to the longest length found so far.
'''

import re as regexp
import unittest
import HtmlTestRunner
import os

#
# Bruteforce approach
#
def longest_absolute_path(input_string):
    
    # 1.  Validate input
    if not input_string:
        raise Exception("Empty input string")

    # 2.  tokenize the input string
    tokens = input_string.split('\n')

    # 3.  Determine directory level by number of leading tabs
    level = 0    
    qualified_paths = []
    prev_is_a_file = False
    tcount = 0
    longest_path = []
    print("TabCnt\tLevel\tisFile\tToken")
    print("=======\t=====\t=====\t=====")
    for token in tokens:
        if token.count('\t') == 0:  # root directory
            longest_path.append(token)
            longest_path.append('/')
            level = 0
            prev_is_a_file = False
            
            #print("TabCnt: {} token: {}".format(tcount, token))
        elif token.count('\t') > 0:
            tcount = token.count('\t', 0, len(token))
            
            if tcount > level:
                # is it a file or a directory?
                if token.count('.', 0, len(token)) == 0:
                    # a directory
                    longest_path.append(regexp.sub(r"[\n\t\s]*", "", token))
                    longest_path.append('/')
                    qualified_paths.append(''.join(longest_path))   # path could end in just a folder
                    prev_is_a_file = False
                else:
                    # a file
                    longest_path.append(regexp.sub(r"[\n\t\s]*", "", token))
                    qualified_paths.append(''.join(longest_path))   # path could end in just a file
                    longest_path = longest_path[:-1]
                    prev_is_a_file = True
                
            elif tcount == level:
                longest_path.append(regexp.sub(r"[\n\t\s]*", "", token))
                longest_path.append('/')
                prev_is_a_file = False
                
            else: # tcout <= level
                #print("Back level detected: tcount:{} level:{}".format(tcount, level))
                longest_path = longest_path[0:(tcount + 1)]
                longest_path.append(regexp.sub(r"[\n\t\s]*", "", token))
                longest_path.append('/')
                
            level = tcount
            
        print("{}\t{}\t{}\t{}".format(tcount, level, prev_is_a_file, token))    

    
    if __debug__:  # debug seems to be always ON
        # returning the number of characters in the longest path, and the longest path itself
        return len(max(qualified_paths, key=len)), max(qualified_paths, key=len)
    else:
        # command syntax: `pipenv run python -O codechallenge_104.py`
        return len(max(qualified_paths, key=len))
    
class TestLongestAbsolutePath(unittest.TestCase):
    def test_absolute_path_len(self):
        self.assertEqual(longest_absolute_path("dir\n\tsubdir1\n\t\tsubsubdir2\n\t\t\tfile.ext"), (31, 'dir/subdir1/subsubdir2/file.ext'))  
        self.assertEqual(longest_absolute_path("PythonDevSrc\n\tProjects\n\t\tCodingChallenges\n\t\t\tcodechallenge_104.py"), (59, 'PythonDevSrc/Projects/CodingChallenges/codechallenge_104.py'))
        
        
if __name__ == '__main__':
    if os.environ.get('UNITTEST_ONLY') != 'True':
        print(longest_absolute_path("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
        print()
        print(longest_absolute_path("PythonDevSrc\n\tProjects\n\t\tCodingChallenges\n\t\t\tcodechallenge_104.py"))
        print()
        print(longest_absolute_path("dir\n\tsubdir1\n\t\tsubsubdir2"))
        print()
        print(longest_absolute_path("PythonDevSrc\n\tProjects\n\t\tCodingChallenges\n\t\t\tcodechallenge_104.py"))
        
    else:    
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_reports'))
    