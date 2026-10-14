# 1. Two Sum (Easy)
# https://leetcode.com/problems/two-sum/
# Approach: hash map of value -> index
# Time: O(n) | Space: O(n)

from typing import List

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, n in enumerate(nums):
            need = target - n
            if need in seen:
                return [seen[need], i]
            seen [n] = i