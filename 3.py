"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])

        backtrack(0, target, [])
        return result

# Example usage:
if __name__ == "__main__":
    solution = Solution()

    candidates1 = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8
    print(solution.combinationSum2(candidates1, target1))  # Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

    candidates2 = [2, 5, 2, 1, 2]
    target2 = 5
    print(solution.combinationSum2(candidates2, target2))  # Output: [[1,2,2],[5]]
