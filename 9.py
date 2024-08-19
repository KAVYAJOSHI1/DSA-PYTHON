"""
There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.
"""
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Initialize the total number of operations to 0
        operations = 0
        
        # Start with the smallest factor (2) and work upwards
        factor = 2
        while n > 1:
            while n % factor == 0:
                operations += factor
                n //= factor
            factor += 1
        
        return operations

# Example usage:
solution = Solution()

# Test case 1: n = 3
print("Minimum operations to get 3 'A's:", solution.minSteps(3))  # Output: 3

# Test case 2: n = 1
print("Minimum operations to get 1 'A':", solution.minSteps(1))  # Output: 0

# Test case 3: n = 4
print("Minimum operations to get 4 'A's:", solution.minSteps(4))  # Output: 4
