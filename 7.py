class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        m, n = len(points), len(points[0])
        prev_row = points[0]
        
        for r in range(1, m):
            left_max = [0] * n
            right_max = [0] * n
            
            # Calculate left max for current row
            left_max[0] = prev_row[0]
            for c in range(1, n):
                left_max[c] = max(left_max[c - 1] - 1, prev_row[c])
            
            # Calculate right max for current row
            right_max[-1] = prev_row[-1]
            for c in range(n - 2, -1, -1):
                right_max[c] = max(right_max[c + 1] - 1, prev_row[c])
            
            # Calculate the max points for the current row
            curr_row = points[r]
            for c in range(n):
                curr_row[c] += max(left_max[c], right_max[c])
            
            prev_row = curr_row
        
        return max(prev_row)

# Example usage:
solution = Solution()
points = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]
print(solution.maxPoints(points))  # Output should be 9
