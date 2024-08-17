"""You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve."""
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
