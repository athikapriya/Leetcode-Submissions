# Approach: Sorting + Two Pointers
# Time: O(n log n) | Space: O(1) auxiliary, excluding sorting

from typing import List 

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()

        minElement = 0
        maxElement = len(nums) - 1
        min_avg = float('inf')

        while minElement < maxElement:
            avg = (nums[minElement] + nums[maxElement]) / 2
            min_avg = min(min_avg, avg)
            minElement += 1
            maxElement -= 1

        return min_avg