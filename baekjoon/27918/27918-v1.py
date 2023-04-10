# 탁구 경기
# 84ms
import sys

input = sys.stdin.readline

n = int(input().strip())
score = []
for _ in range(n):
    alpha = input().strip()
    score.append(alpha)


D = 0
P = 0
for ch in score:
    if ch == "D":
        D += 1
    else:
        P += 1

    diff = D - P
    if diff <= -2 or 2 <= diff:
        break

print(f"{D}:{P}")
