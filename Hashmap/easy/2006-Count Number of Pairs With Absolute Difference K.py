# Approach: Hash Map (Counter)
# Time: O(n) | Space: O(n)

from collections import Counter
from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        count = 0

        for num in freq:
            count += freq[num] * freq.get(num + k, 0)

        return count