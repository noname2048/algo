import sys

sys.stdin = open("p1.txt", "r")
input = lambda: sys.stdin.readline().strip()

def thousand2abc(n):
    return n // 100, n // 10, n % 10

def abc2thousand(a, b, c):
    return a * 100 + b * 10 + c

def main():
    n = int(input())
    t = list(map(int, input().split()))

    # 그리디로 풀 수 있는 점화식 발견 실패
    # dp 나 탐색에서 수를 줄일 수 있는 방안으로

    cache = [[0] * 1000 for _ in range(n)]

    k = t[0]
    cache[0][abc2thousand(k, 0, 0)] = k

    for n_idx in range(1000):
        for status_idx in range(1000):
            if cache[n_idx - 1][status_idx] != -1:
                status = thousand2abc(status_idx)
                for i in range(3):
                    diff = (status[i] - t[n_idx] + 10) % 10
                    status[i] = t[n_idx]

                    new_status = abc2thousand(*status)
                    if cache[n_idx][new_status] == -1: # 결과값 없음
                        cache[n_idx][new_status] = cache[n_idx][status] + diff
                    else: # 최소 결과값 사용
                        cache[n_idx][new_status] = min(cache[n_idx][new_status], cache[n_idx][status] + diff)

        a, b, c = thousand2abc(i)
        cache[i][i] = abs(t[0] - abc2thousand(a, b, c))

    def re(idx):
        if idx == n:
            return

        for a in range(10):
            for b in range(10):
                for c in range(10):
                    if cache[idx][a][b][c] != -1:
                        t[n-1][a] = 
