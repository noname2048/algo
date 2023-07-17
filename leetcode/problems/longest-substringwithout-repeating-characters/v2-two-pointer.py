class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestLenght = 0
        i, j = 0, 0

        while j < len(s):
            if s[j] not in s[i:j]:
                j += 1
                longestLenght = max(longestLenght, j - i)
            else:
                while s[i] != s[j]:
                    i += 1
                i += 1
        return longestLenght


p = Solution()
ans = p.lengthOfLongestSubstring("abcabcbb")
print(ans)
ans = p.lengthOfLongestSubstring(" ")
print(ans)
