# v2의 timeout 을 더 효과적으로 대처해보자.
import sys
from collections import defaultdict

sys.stdin = open("p2.txt", "r")
input = lambda: sys.stdin.readline().rstrip()

def main():
    edges = []
    n, m = list(map(int, input().split()))
    for _ in range(m):
        u, v, d = list(map(int, input().split()))
        edges.append((u, v, d))
    answer = solve(n, m, edges)
    print(answer)

class Buffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.idx = 0
    
    def push(self, item):
        self.buffer[self.idx] = item
        self.idx = (self.idx + 1) % self.size

    @property
    def all(self):
        return self.buffer

def solve(n, m, edges):
    # case 01
    buffer = Buffer(2)
    temp_max = -1
    for _ in range(2):
        for u, v, d in edges:
            if temp_max < d:
                temp_max = d
                buffer.push(d)            
    answer = sum(buffer.all)
    
    # case 02
    edge_dict = defaultdict(dict)
    for u, v, d in edges:
        edge_dict[u][v] = d
        edge_dict[v][u] = d

    for node in edge_dict.keys():
        edge_dict[node] = dict(sorted(edge_dict[node].items(), key=lambda x: x[1], reverse=True))
    
    for edge in edges:
        local_answer = -1
        u, v, d = edge
        result_u = [(-1, 0), (-1, 0)]
        result_v = [(-2, 0), (-2, 0)]

        local_u = {k: v for k, v in edge_dict[u].items() if k != v}   
        local_v = {k: v for k, v in edge_dict[v].items() if k != u}

        u_keys = list(local_u.keys())
        u_values = list(local_u.values())
        v_keys = list(local_v.keys())
        v_values = list(local_v.values())

        if len(u_keys) > 0:
            result_u[0] = (u_keys[0], u_values[0])
        if len(u_keys) > 1:
            result_u[1] = (u_keys[1], u_values[1])

        if len(v_keys) > 0:
            result_v[0] = (v_keys[0], v_values[0])
        if len(v_keys) > 1:
            result_v[1] = (v_keys[1], v_values[1])
        
        if result_u[0][0] == result_v[0][0]:
            a = result_u[0][1] + result_v[1][1]
            b = result_v[0][1] + result_u[1][1]
            local_answer = max(a, b)
        else:
            local_answer = result_u[0][1] + result_v[0][1]
        answer = max(answer, local_answer + d)

    return answer

main()
