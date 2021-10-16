import sys

sys.stdin = open("input1.txt", "r")

n = int(input())
(*p_list,) = map(int, input().split())  # parent_list
r = int(input())  # remove

c_list = [[] for _ in range(n)]
for i, parent in enumerate(p_list):
    parent != -1 and c_list[parent].append(i)

root = p_list.index(-1)
top_down = lambda x: x - r and (sum([top_down(child) for child in c_list[x]]) or 1)

print(top_down(root))
