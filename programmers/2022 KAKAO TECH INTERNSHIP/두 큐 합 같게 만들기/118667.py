def solution(queue1, queue2):
    # 합이 짝수가 아닐경우
    total = sum(queue1) + sum(queue2)
    if total % 2 == 1:
        return -1

    # 두개로 나누어 풀기
    a1 = sub_solution(queue1, queue2, total)
    a2 = sub_solution(queue2, queue1, total)

    ans = -1
    if a1 == -1 and a2 > -1:
        ans = a2
    elif a2 == -1 and a1 > -1:
        ans = a1
    else:
        ans = min(a1, a2)

    print(ans)
    return ans


def sub_solution(q1, q2, sumation):
    q3 = q1.copy() + q2.copy()

    half = sumation / 2

    ans = -1

    def update_ans(num):
        nonlocal ans
        if ans == -1 or num < ans:
            ans = num

    i, j, s = 0, 0, 0
    while i < len(q1):
        if s < half and j < len(q3):
            s += q3[j]
            j += 1
        elif s > half:
            s -= q3[i]
            i += 1
        elif s == half:
            if j == len(q1):
                update_ans(i)
            elif j < len(q1):
                update_ans(len(q2) + j + i)
            elif j > len(q1):
                update_ans(j - len(q1) + i)
            else:
                print("Error")
            s -= q3[i]
            i += 1
        else:
            break

    return ans


Q1 = {
    "queue1": [3, 2, 7, 2],
    "queue2": [4, 6, 5, 1],
}
Q2 = {
    "queue1": [1, 2, 1, 2],
    "queue2": [1, 10, 1, 2],
}
solution(**Q2)
