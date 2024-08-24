"""
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

 

Example 1:

Input: n = "123"
Output: "121"
Example 2:

Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
"""

class Solution(object):
    def nearestPalindromic(self, n):
        length = len(n)
        if n == "1":
            return "0"
        
        candidates = set()
        prefix = int(n[:(length + 1) // 2])
        
        for i in [-1, 0, 1]:
            candidate = str(prefix + i)
            if length % 2 == 0:
                candidate = candidate + candidate[::-1]
            else:
                candidate = candidate + candidate[:-1][::-1]
            candidates.add(candidate)
        
        candidates.add("9" * (length - 1))
        candidates.add("1" + "0" * (length - 1) + "1")
        candidates.discard(n)
        
        return min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))

# Example usage
solution = Solution()
print(solution.nearestPalindromic("123"))  # Output: "121"
