import sys

sys.stdin = open("input.txt", "r")

cost_list = []
n = int(input())
for house in range(n):
    cost_list.append(list(map(int, input().split())))

r, g, b = cost_list[0]
for idx in range(1, n):
    cr, cg, cb = cost_list[idx]
    r, g, b = [cr + min(g, b), cg + min(r, b), cb + min(r, g)]

print(min([r, g, b]))
