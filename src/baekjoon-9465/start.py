import sys

sys.stdin = open('input.txt', 'r')
test_case = int(sys.stdin.readline())

def solution(cost, n):
    
    cache = [[0] * 2 for _ in range(n)]
    cache[0] = cost[0]
    
    cache[1][0] = cache[0][1] + cost[1][0]
    cache[1][1] = cache[0][0] + cost[1][1]
    
    if n > 2:
        for idx in range(2, n):
            cache[idx][0] = cost[idx][0] + max(cache[idx - 2][0], cache[idx - 2][1], cache[idx-1][1])
            cache[idx][1] = cost[idx][1] + max(cache[idx - 2][0], cache[idx - 2][1], cache[idx-1][0])
    
    
    # print(cache)   
    return max(cache[n - 1][0], cache[n - 1][1])

for _ in range(test_case):
    n = int(sys.stdin.readline().strip())
    
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    cost = tuple(zip(a, b))
    
    print(solution(cost, n))