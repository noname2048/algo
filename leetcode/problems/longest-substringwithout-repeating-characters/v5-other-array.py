class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charArray = [-1] * 128
        left = 0

        for right in range(n):
            if charArray[ord(s[right])] >= left:
                left = charArray[ord(s[right])] + 1
            charArray[ord(s[right])] = right
            maxLength = max(maxLength, right - left + 1)

        return maxLength
