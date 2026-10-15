# 2351. First Letter to Appear Twice(easy)
# https://leetcode.com/problems/first-letter-to-appear-twice/
# Time: O(n) | Space: O(n)

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()

        for char in s:
            if char in seen:
                return char
            
            seen.add(char)