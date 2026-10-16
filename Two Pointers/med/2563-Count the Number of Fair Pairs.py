# Approach: Sorting + Two Pointers + Counting Pairs
# Time: O(n log n) | Space: O(1) auxiliary, excluding sorting

from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        
        def count_less_equal(limit):
            left = 0
            right = len(nums) - 1
            count = 0

            while left < right:
                if nums[left] + nums[right] <= limit:
                    count += right - left
                    left += 1
                else:
                    right -= 1
                
            return count
        
        return count_less_equal(upper) - count_less_equal(lower - 1)