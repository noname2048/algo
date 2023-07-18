class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        prev_value = 0
        for c in s:
            value = self.symbolToValue(c)
            if prev_value < value:
                ans += value - prev_value * 2
            else:
                ans += value
            prev_value = value

        return ans

    def symbolToValue(self, symbol):
        table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        return table[symbol]


solution = Solution()
# ans = solution.romanToInt("LVIII")
# print(ans)
ans = solution.romanToInt("MCMXCIV")
print(ans)
