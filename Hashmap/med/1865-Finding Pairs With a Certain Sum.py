# Approach: Hash Map (Frequency Counter)
# Time: O(n + m) initialization, O(1) average add(),
#       O(n) average count()
# Space: O(m) auxiliary

from typing import List
from collections import Counter

class FindSumPairs:

    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_value = self.nums2[index]
        self.freq[old_value] -= 1
        self.nums2[index] += val
        new_value = self.nums2[index]
        self.freq[new_value] += 1

    def count(self, tot: int) -> int:
        res = 0

        for num in self.nums1:
            need = tot - num
            res += self.freq[need]

        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)