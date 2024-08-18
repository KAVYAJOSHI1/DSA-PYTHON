"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

 

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
"""
import heapq

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Min-heap to store the ugly numbers
        heap = [1]
        # Set to avoid duplicates
        seen = {1}
        
        # Variables for the prime factors
        primes = [2, 3, 5]
        
        ugly_number = 1
        
        for i in range(n):
            # Extract the smallest ugly number
            ugly_number = heapq.heappop(heap)
            
            # Generate new ugly numbers by multiplying with 2, 3, and 5
            for prime in primes:
                new_ugly = ugly_number * prime
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        
        return ugly_number

# Example usage:
solution = Solution()
print(solution.nthUglyNumber(10))  # Output: 12

