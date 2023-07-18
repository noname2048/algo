class Solution:
    def isPalindrome(self, x: int) -> bool:
        tempX = x
        if tempX < 0:
            return False

        reversedX = 0
        while tempX > 0:
            reversedX *= 10
            reversedX += tempX % 10
            tempX = tempX // 10

        return x == reversedX


solution = Solution()
print(solution.isPalindrome(121))
