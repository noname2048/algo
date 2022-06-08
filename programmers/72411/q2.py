from collections import defaultdict


def solution(orders, course):
    ans = []
    for c in course:
        word_dict = defaultdict(int)
        for o in orders:
            t = list()
            combination(o, c, word_dict, 0, t)

        mx = -1
        for k, v in word_dict.items():
            if v >= 2:
                mx = max(v, mx)
        for k, v in word_dict.items():
            if v == mx:
                ans += [k]
    return sorted(ans)


# 조합을 구현하라
def combination(elements, target_len, adder, start_idx, comb):
    if target_len == len(comb):
        temp = sorted(comb)
        adder["".join(temp)] += 1
        return

    curr_len = len(comb)
    remains = target_len - curr_len
    end_idx = len(elements) - remains
    for i in range(start_idx, end_idx + 1):
        new_comb = comb + [elements[i]]
        combination(elements, target_len, adder, i + 1, new_comb)


def test_1():
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2, 3, 4]
    result = ["AC", "ACDE", "BCFG", "CDE"]
    ans = solution(orders, course)
    assert result == ans


test_1()
