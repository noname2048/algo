from typing import List, Tuple


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alpha_count = [0] * 26

        i, j = 0, 0
        while j != len(s):
            if j - i == 0:
                j += 1
                continue

            next = ord(s[j + 1]) - ord("a")
            if alpha_count[next] != 0:
                pass
