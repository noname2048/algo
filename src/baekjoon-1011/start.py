class Solution:
    def __init__(self, x, y):
        self.d = y - x

    def solve(self):
        base = 1
        threshold = 1

        while self.d > threshold:
            base += 1
            threshold += (base - 1) // 2 + 1
            # print(threshold)

        return base


test_case = int(input())
for i in range(test_case):
    x, y = list(map(int, input().split()))

    print(Solution(x, y).solve())
