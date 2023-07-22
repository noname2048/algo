from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_set = set(nums)
        n = len(num_set)
        nums[:n] = sorted(list(num_set))

        return n


solution = Solution()
ans = solution.removeDuplicates([0, 1, 1, 2])
print(ans)
