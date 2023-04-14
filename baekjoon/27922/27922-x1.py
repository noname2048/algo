# https://www.acmicpc.net/source/58575653
# 배울점:
# readline 을 테스트 할 때 굉장히 간편하게 구성했음
# 나누어서 sort 할 배열을 만든것
# 슬라이싱 기법 쓴거
# sum 을 이용해 빠르게 합산한 것

import sys

# sys.stdin=open('input.txt')
input = sys.stdin.readline


def sol():
    n, k = map(int, input().split())
    d12 = []
    d23 = []
    d31 = []
    for i in range(n):
        a, b, c = map(int, input().split())
        d12.append(a + b)
        d23.append(b + c)
        d31.append(c + a)
    d12.sort(reverse=True)
    d23.sort(reverse=True)
    d31.sort(reverse=True)
    print(max(sum(d12[:k]), sum(d23[:k]), sum(d31[:k])))


sol()
