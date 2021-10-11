import sys

sys.stdin = open("input4.txt", "r")
n = int(input())
parent = map(int, input().split())

child = [[] for _ in range(n)]
for idx, ele in enumerate(parent):
    if ele != -1:
        child[ele].append(idx)

deleted_dict = {}
delete_root = int(input())
stack = [delete_root]
while stack:
    here = stack.pop()
    if here not in deleted_dict:
        deleted_dict[here] = 1
        stack += child[here]

ans = 0
for idx in range(n):
    if not child[idx] and idx not in deleted_dict:
        ans += 1

print(ans)
