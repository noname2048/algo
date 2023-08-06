from abc import ABCMeta, abstractmethod


class Problem(metaclass=ABCMeta):
    @abstractmethod
    def searchInsert(self, nums: list[int], target: list[int]) -> int:
        pass


class Solution(Problem):
    def searchInsert(self, nums: list[int], target: int) -> int:
        nums_len = len(nums)
        start, end = 0, nums_len
        mid = (start + end) // 2

        while start < end:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
                mid = (start + end) // 2
            else:
                end = mid
                mid = (start + end) // 2

        return mid

    @classmethod
    def pub_serach_insert(cls, nums: list[int], target: list[int]) -> int:
        return -1


class FakeSolution(Problem):
    pass


# FakeSolution()
#
# TypeError: Can't instantiate abstract class FakeSolution with abstract method searchInsert


# ans = Solution.pub_serach_insert([1, 2, 4, 6], 7)
# print(ans)
#
# works

solution = Solution()
ans = solution.searchInsert([1, 2, 3, 6], 7)
print(ans)
