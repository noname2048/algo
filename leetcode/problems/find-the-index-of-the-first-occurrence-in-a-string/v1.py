class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        i = 0
        while i < n:
            j = 0
            while haystack[i + j] == needle[j]:
                j += 1
                if j == m:
                    return i
                if i + j == n:
                    return -1
            i += 1
        return -1


solution = Solution()
ans = solution.strStr("sadbutsad", "sad")
print(ans)
ans = solution.strStr("leetcode", "leeto")
print(ans)
