import q


def solution(queue1, queue2):
    total = sum(queue1) + sum(queue2)
    if total % 2 == 1:
        return -1

    half = total / 2
    queue3 = queue1 + queue2 + queue1

    s = 0
    e = len(queue1)
    k = sum(queue1)
    answer = 0

    while True:
        if s >= len(queue1) + len(queue2):
            return -1

        elif k < half:
            k += queue3[e]
            e += 1
            if e > len(queue3):
                return -1
        elif k > half:
            k -= queue3[s]
            s += 1
        else:
            print(answer)
            return answer

        answer += 1
    

solution(**q.Q1)
