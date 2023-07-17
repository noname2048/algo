class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstring = ""

        _len = len(s)
        for i in range(_len):
            localSubset = self.getLongestSubstring(s[i:])
            if len(localSubset) > len(longestSubstring):
                longestSubstring = localSubset

            if len(longestSubstring) > _len - i:
                break

        return len(longestSubstring)

    def getLongestSubstring(self, s: str) -> str:
        subset = ""
        strUsage = {}
        _len = len(s)
        for i in range(_len):
            if s[i] in strUsage:
                return subset
            else:
                strUsage[s[i]] = True
                subset += s[i]
        return subset


p = Solution()
# ans = p.lengthOfLongestSubstring("abcabcbb")
# print(ans)
ans = p.lengthOfLongestSubstring(" ")
print(ans)
