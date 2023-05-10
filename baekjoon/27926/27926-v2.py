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
    # 이경우 1과 4를 골라야 하는 이유는 123 이 이어진 간선이기 때문인데, 이는 case 2에서 최대값이 된다.
    # case 1이 이어진 간선이 아니면서 최대값을 만족하려면, 자연수 범위에서는 없다.
    # p3.txt 를 이를 바탕으로 만든다.
    # 즉 case 1에서는 2개의 간선을 이어지든, 이어지지 않든 고르는 것이 최대값이다.

    # case 2에서는 연결할 수 있는 점중 가장 가중치가 큰을 놈을 고르면, 
    # 문제가 생길 수 있는 케이스가 있다. p6를 참고하라.
    # 가장 큰 간선을 고른뒤, 3순위 간선까지만 고려하면
    # 1, 2순위가 사이클을 이루는 경우, 1, 3을 선택하거나, 2, 3을 선택하는 것으로
    # 최대 순위를 결정 할 수 있다.
    # 단, 가장 큰 간선을 고르는 기준은 잘못될 가능 성이 있으므로 (p7 참조)
    # 모든 간선에 대해 123 순위를 고려하는 전범위 탐색을 시행해야 한다.
    pass 

                

