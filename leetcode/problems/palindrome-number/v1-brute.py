class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        reversedS = s[::-1]
        return s == reversedS


solution = Solution()
print(solution.isPalindrome(121))
