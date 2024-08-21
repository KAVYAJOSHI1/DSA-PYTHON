"""
There is a strange printer with the following two special properties:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.
"""
class Solution(object):
    def strangePrinter(self, s):
        if not s:
            return 0
        
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = min(dp[i][k] + dp[k + 1][j] for k in range(i, j))
        
        return dp[0][n - 1]

def main():
    solution = Solution()
    s = "aaabbb"
    result = solution.strangePrinter(s)
    print(result)  # Expected output: 2

if __name__ == "__main__":
    main()
