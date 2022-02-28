'''
Date: 12/25/2021

Problem Statement:
==================
This problem was asked by Google.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

Algorithm:
==========
1.  Validate input, remove leading zeros.
2.  Initialize the hash table( or dictionary) to store the mapping of characters to numbers.
3.  Iterate through the message, splicing [ #step 4]. and i is incremented by 1.
4.  - Splice the message into a list of characters.  Assume uni-directional splicing.
    - Iterate through the list of characters, for each element, permutate the list of characters.
    - For each permutation, check if the key is in the dictionary.if found in the dictionary, append the value to the list.
    Note: It is posible that the key is not in the dictionary. and the value is an empty string.  
    
5.  Convert list into set to remove duplicates.  Then, return the list count.

Note: 
=====
Sometimes, the strategy for understanding the problem is to brute force it.  Then, refinement is less error prone.

Note: (list splicing) 
=====================
[:2] corresponds to [start=default:stop=2]
[1:] corresponds to [start=1:stop=default]
'''
import unittest

class Enigma:
    def __init__(self, message, dictEncodedMsg):
        self.message = message
        self.dictEncodedMsg = dictEncodedMsg
    
    @property
    def encodedValue(self):
        return self.dictEncodedMsg
    
    def encodedValue(self, key):
        if key in self.dictEncodedMsg:
            return self.dictEncodedMsg[key]
        else:
            return ''
                
    
    def addElement(self, result_lst, tmp_lst):
        #print (tmp_lst)
        [i for i in tmp_lst if i != '']

        if len(tmp_lst) > 0: result_lst.append(''.join(tmp_lst))
        #print (result_lst)
        return result_lst
        
    def countDecoding(self):
        # remove leading zeros
        self.message = self.message.lstrip('0')   
        
        tmp_lst = []
        result_lst = []
        
        # edge case:
        if len(self.message) == 0:
            raise ValueError("Empty message")
            

        # slpit message string into list of charaters
        msgKey = list(self.message)
    
        #
        # Base case: each element is individually matched with the dictionary
        #
        [tmp_lst.append(self.encodedValue(''.join(msgKey[idx]))) for idx in range(0, len(msgKey))]
        result_lst.append(''.join(tmp_lst))
        
        #
        # Iterable case: 1st element is matched with the dictionary, 
        # 2nd concat 3rd element is matched with the dictionary, 
        # then 3rd element is matched with the dictionary,...
        #
        # Permutate the list of characters.    
        for i in range(0, len(msgKey)):
            tmp_lst = []
            [tmp_lst.append(self.encodedValue(''.join(msgKey[:idx]))) for idx in range(i, len(msgKey))]
            result_lst.append(''.join(tmp_lst))

            tmp_lst = []
            [tmp_lst.append(self.encodedValue(''.join(msgKey[idx:]))) for idx in range(i, len(msgKey))]
            result_lst.append(''.join(tmp_lst))

        tmp_lst = []
        
        # Flip the list of characters in msgKey
        msgKey = msgKey[::-1]
        for i in range(0, len(msgKey)):
            tmp_lst = []
            [tmp_lst.append(self.encodedValue(''.join(msgKey[:idx]))) for idx in range(i, len(msgKey))]
            result_lst.append(''.join(tmp_lst))

            tmp_lst = []
            [tmp_lst.append(self.encodedValue(''.join(msgKey[idx:]))) for idx in range(i, len(msgKey))]
            result_lst.append(''.join(tmp_lst)) 


            

        # remove duplicates
        result_lst = list(set(result_lst))
        
        # remove elements with length 1
        final_result = [i for i in result_lst if len(i) >= 2]    
        
        print(final_result)
        return len(final_result)

class TestDecoder(unittest.TestCase):
    def test_decode(self):
        mesg = '111'
        encodedMsg = {'1':'a', '2':'b', '3':'c', '4':'d', '5':'e', '6':'f', '7':'g', '8':'h', '9':'i', '10':'j', '11':'k', '12':'l', '13':'m', '14':'n', '15':'o', '16':'p', '17':'q', '18':'r', '19':'s', '20':'t', '21':'u', '22':'v', '23':'w', '24':'x', '25':'y', '26':'z'}
        enigma = Enigma(mesg, encodedMsg)
   
        self.assertEqual(enigma.countDecoding(), 3)
        enigma = Enigma('1211', encodedMsg)
        self.assertEqual(enigma.countDecoding(), 5)
        enigma = Enigma('1234', encodedMsg)
        self.assertEqual(enigma.countDecoding(), 3)
        # enigma = Enigma('asasdggsad', encodedMsg)
        # with self.assertRaises(ValueError):
        #     enigma.countDecoding()
    
if __name__ == '__main__':
    mesg = '111'
    encodedMsg = {'1':'a', '2':'b', '3':'c', '4':'d', '5':'e', '6':'f', '7':'g', '8':'h', '9':'i', '10':'j', '11':'k', '12':'l', '13':'m', '14':'n', '15':'o', '16':'p', '17':'q', '18':'r', '19':'s', '20':'t', '21':'u', '22':'v', '23':'w', '24':'x', '25':'y', '26':'z'}
    enigma = Enigma(mesg, encodedMsg)
    print(enigma.countDecoding())
    
          
    unittest.main()
    