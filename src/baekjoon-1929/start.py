import sys
import math

# n, m = map(int, sys.stdin.readline().split())
n, m = map(int, input().split())
# n, m = 3, 16

sosu = [1] * 1000002
sosu[0] = 0
sosu[1] = 0

max_divider = int(math.sqrt(m))

i = 2
while i <= max_divider + 1:
    # 배수는 소수에서 제외
    j = 2
    temp = i * j
    while temp <= m:
        sosu[temp] = 0
        j += 1
        temp = i * j

    # 다음 소수가 아닌 수를 지정
    i += 1
    while sosu[i] == 0:
        i += 1

ans = [idx + n for (idx, x) in enumerate(sosu[n : m + 1]) if x]
for e in ans:
    print(e)
