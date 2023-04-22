import sys
import math

# sys.stdin = open("p2.txt")
input = sys.stdin.readline

def main():
    n, k, l = list(map(int, input().rstrip().split()))
    m = list(map(int, input().rstrip().split()))
    t = list(map(int, input().rstrip().split()))

    # effective of cola
    cola = list(map(lambda x: [0, x], range(n + l + 1)))
    for ti in t:
        for li in range(l):
            cola[ti + li][0] += 1

    # sort and calc
    cola.sort(reverse=True)
    m.sort(reverse=True)

    max_cap = 0
    for i in range(n):
        max_cap += math.floor(m[i] / (2 ** cola[i][0]))

    print(max_cap)

main()