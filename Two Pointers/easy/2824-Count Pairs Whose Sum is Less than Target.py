# 2824. Count Pairs Whose Sum is Less than Target (Easy)
# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/
# Approach: Sorting + Two Pointers
# Time: O(n log n) | Space: O(1) auxiliary

from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1
        count = 0

        while left < right:
            if nums[left] + nums[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1

        return count