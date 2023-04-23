# v1 이 시간초과를 냄에 따라 
# 중간에 있는 컨볼루젼을 콜라의 수 인 k * l 가 아닌
# n * l 형태로 변경
# 아마 역시 시간초과 날 것 같음. heapq 를 이용해야하나?
# 여젼히 시간초과, 누적합을 이용해야 할 것 같음

import math
import sys

sys.stdin = open("p1.txt")
input = sys.stdin.readline

def main():
    n, k, l = list(map(int, input().split()))
    m = list(map(int, input().split()))
    t = list(map(int, input().split()))

    cola_status = [0] * n
    cola_effect = list(map(lambda x: [0, x], range(n)))
    for c in t:
        cola_status[c - 1] += 1

    for i in range(n):
        for j in range(l):
            idx = i - 1 - j
            if 0 <= idx < n:
                cola_effect[i][0] += cola_status[idx]

    cola_effect.sort(reverse=True)
    m.sort(reverse=True)

    max_cap = 0
    for i in range(n):
        max_cap += math.floor(m[i] / (2 ** cola_effect[i][0]))

    print(max_cap)

main()
