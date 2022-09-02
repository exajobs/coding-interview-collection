/*
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
Example 2:
Input: 
bits = [1, 1, 1, 0]
Output: False
Explanation: 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
Note:

1 <= len(bits) <= 1000.
bits[i] is always 0 or 1.
*/

// https://leetcode.com/problems/1-bit-and-2-bit-characters/solution/
class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int pos = 0;
        // Go through bits
        while (pos < bits.length - 1) {
            // if 1, pos + 2; if 0, pos + 1
            pos += bits[pos] + 1;
        }
        return pos == bits.length - 1;
    }

    /* public boolean isOneBitCharacter(int[] bits) {
        // From len - 2
        int i = bits.length - 2;
        // until encounter 0
        while (i >= 0 && bits[i] > 0) i--;
        // check if second last zero is even
        return (bits.length - i) % 2 == 0;
    } */
}
