from collections import Counter
from itertools import combinations


def solution(orders, course):
    orders = [sorted(order) for order in orders]
    answer = []

    for course_size in course:
        combs = []
        for order in orders:
            combs += combinations(sorted(order), course_size)
        temp = Counter(combs).most_common()
        if temp and temp[0][1] >= 2:
            answer += [k for k, v in temp if v == temp[0][1]]

    answer = sorted(["".join(ans) for ans in answer])
    return answer


def test_1():
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2, 3, 4]
    result = ["AC", "ACDE", "BCFG", "CDE"]
    ans = solution(orders, course)
    assert result == ans


test_1()
