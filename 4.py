"""
The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

 

Example 1:

Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Example 2:

Input: nums = [1,1,1], k = 2
Output: 0
Example 3:

Input: nums = [1,6,1], k = 3
Output: 5
 

Constraints:

n == nums.length
2 <= n <= 104
0 <= nums[i] <= 106
1 <= k <= n * (n - 1) / 2
"""
class Solution:
    def smallestDistancePair(self, nums, k):
        def countPairs(mid):
            count = 0
            j = 0
            for i in range(len(nums)):
                while j < len(nums) and nums[j] - nums[i] <= mid:
                    j += 1
                count += j - i - 1
            return count
        
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        
        while left < right:
            mid = (left + right) // 2
            if countPairs(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return left

def main():
    # Example inputs
    nums1 = [1, 3, 1]
    k1 = 1
    nums2 = [1, 1, 1]
    k2 = 2
    nums3 = [1, 6, 1]
    k3 = 3
    
    # Create a Solution object
    solution = Solution()
    
    # Compute and print the results for each test case
    print("Output for nums1 =", nums1, "and k1 =", k1, "is:", solution.smallestDistancePair(nums1, k1))
    print("Output for nums2 =", nums2, "and k2 =", k2, "is:", solution.smallestDistancePair(nums2, k2))
    print("Output for nums3 =", nums3, "and k3 =", k3, "is:", solution.smallestDistancePair(nums3, k3))

if __name__ == "__main__":
    main()
