"""
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.

 

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
"""

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Calculate the bit length of the number
        bit_length = num.bit_length()
        
        # Create a bitmask of the same length as the number, filled with 1's
        bitmask = (1 << bit_length) - 1
        
        # XOR the number with the bitmask to get the complement
        return num ^ bitmask

# Example usage:
sol = Solution()
print(sol.findComplement(5))  # Output: 2
print(sol.findComplement(1))  # Output: 0
