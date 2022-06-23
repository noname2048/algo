import sys

sys.stdin = open("input.txt", "r")
###
class Solution:
    n = 0
    dp = []
    cost_list = []
    pseudo_inf = 9000000

    def __init__(self, cost_list):
        self.cost_list = cost_list

    def solve(self):
        self.n = len(self.cost_list)
        self.dp = [[self.pseudo_inf] * 3 for _ in range(self.n)]

        ans = self.pseudo_inf
        for idx in range(3):
            ans = min(ans, self.re(0, idx))

        return ans

    def re(self, house, choice):
        if self.dp[house][choice] != self.pseudo_inf:
            return self.dp[house][choice]

        if house >= self.n - 1:
            return self.cost_list[house][choice]

        new_cost = self.cost_list[house][choice] + min(
            self.re(house + 1, (choice + 1) % 3),
            self.re(house + 1, (choice + 2) % 3),
        )

        return new_cost


cost_list = []

for house in range(int(input())):
    cost_list.append(list(map(int, input().split())))
s = Solution(cost_list)
print(s.solve())
