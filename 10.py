"""
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

 

Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
Example 2:

Input: piles = [1,2,3,4,5,100]
Output: 104
"""
class Solution(object):
    def stoneGameII(self, piles):
        n = len(piles)
        suffixSum = [0] * n
        
        # Precompute the suffix sums
        suffixSum[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffixSum[i] = piles[i] + suffixSum[i + 1]
        
        # Memoization cache
        dp = {}

        def helper(i, M):
            if i >= n:
                return 0
            if (i, M) in dp:
                return dp[(i, M)]
            
            maxStones = 0
            for X in range(1, min(2 * M, n - i) + 1):
                # Remaining stones minus the best Bob can get
                maxStones = max(maxStones, suffixSum[i] - helper(i + X, max(M, X)))
            
            dp[(i, M)] = maxStones
            return maxStones
        
        return helper(0, 1)

def main():
    # Example 1
    piles1 = [2, 7, 9, 4, 4]
    solution = Solution()
    result1 = solution.stoneGameII(piles1)
    print(f"Maximum stones Alice can get for piles {piles1}: {result1}")
    
    # Example 2
    piles2 = [1, 2, 3, 4, 5, 100]
    result2 = solution.stoneGameII(piles2)
    print(f"Maximum stones Alice can get for piles {piles2}: {result2}")

if __name__ == "__main__":
    main()
