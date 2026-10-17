# Approach: Sorting + Two Pointers + Hashset
# Time: O(n log n) | Space: O(n) auxiliary, excluding sorting

from typing import List 

class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1
        average = set()

        while left < right:
            avg = (nums[left] + nums[right]) / 2
            average.add(avg)

            left += 1
            right -= 1
        
        return len(average)