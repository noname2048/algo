# (알고리즘 분류를 본뒤에) 어떻게 그리디로 풀 것인가

import sys
from collections import defaultdict

sys.stdin = open("p2.txt", "r")
input = sys.stdin.readline().rstrip()


def main():
    graph = defaultdict(dict)

    n, m = list(map(int, input().split()))
    for _ in range(m):
        u, v, d = list(map(int, input().split()))
        graph[u][v] = graph[v][u] = d

    answer = main(n, m, graph)
    print(answer)

# 분할과 정복은 언제나 옳다
# case 1: 2개의 별개의 간선을 선택
# case 2: 3개의 이어진 간선을 선택
def solve(n, m, graph):
    # 2개의 간선이 별개의 간선이라는 것을 어떻게 알 수 있는가?
    # a. 그냥 sort 하고 위에서 부터 선택가능한 2개를 고른다 
    # a-2. 이 경우 2등과 3등을 고르는게 1등과 4등을 고르는 것보다 좋을 수 있는가
    # (4) | - (3) - (1) - (2) - 
    # 
    pass 

                

