import sys

def pretext():
    def init():
        with open("p1.txt", "r") as f:
            content = f.readlines()
        yield from content

    gen = init()

    def inner():
        return next(gen)

    return inner


input = pretext()
# input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    lectures = []
    for i in range(n):
        lecture_info = list(map(int, input().split()))
        ab = lecture_info[0] + lecture_info[1]
        bc = lecture_info[1] + lecture_info[2]
        ac = lecture_info[0] + lecture_info[2]
        lectures.append((ab, bc, ac))
    
    answer = 0
    for i in range(3):
        lectures.sort(key=lambda x: -x[i])
        local_sum = 0 
        for j in range(k):
            local_sum += lectures[j][i]
        answer = max(answer, local_sum)
    
    print(answer)

main()
