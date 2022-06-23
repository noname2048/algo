cache = [[-1 for _ in range(31)] for _ in range(31)]
def solution(a, b):
    return re(b, a)

def re(a, b):
    if cache[a][b] != -1:
        return cache[a][b]
    elif a == 1 or a == b:
        cache[a][b] = 1
        return 1
    elif b == 1:
        cache[a][b] = a
        return a
    else:
        cache[a][b] = re(a - 1, b) + re(a - 1, b - 1)
        return cache[a][b]
    
if __name__ == "__main__":
    testcase = int(input())
    for _ in range(testcase):
        q = input()
        que = q.split()
        que= list(map(int, que))
        print(solution(que[0], que[1]))
