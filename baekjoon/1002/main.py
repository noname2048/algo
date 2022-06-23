from math import sqrt

def d(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
def solution(x1, y1, r1, x2, y2, r2):
    dist = d(x1, y1, x2, y2)
    r = r1 + r2

    # print(dist, r)
    
    if x1 == x2 and y1 == y2 and r1 == r2:
        return -1
    
    if dist > r:
        return 0
    elif dist == r:
        return 1
    elif dist < r:
        if dist + r1 == r2 or dist + r2 == r1: 
            return 1
        elif dist + r1 < r2 or dist + r2 < r1:
            return 0
        elif dist + r1 > r2 or dist + r2 > r1:
            return 2
        else:
            return 2
    
if __name__ == "__main__":
    for testcase in range(int(input())):
        q = list(map(int, input().split()))
        
        print(solution(*q))
