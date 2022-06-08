from collections import defaultdict


def solution(info, query):
    answer = []
    groups = defaultdict(list)

    for item in info:
        key, score = item.rsplit(" ", 1)
        score = int(score)
        add_key_in_groups(key, score, groups)

    for k, v in groups.items():
        v.sort()

    for q in query:
        raw_key, score = q.rsplit(" ", 1)
        score = int(score)
        key = raw_key.replace(" and ", "")
        answer += [get_answer(key, score, groups)]

    return answer


def add_key_in_groups(key, score, groups):
    words = key.split(" ")

    def re(index, curr):
        if index == 4:
            groups[curr] += [score]
            return

        re(index + 1, curr + words[index])
        re(index + 1, curr + "-")

    re(0, "")


def get_answer(key, score, groups):
    target_group = groups[key]
    st, ed = 0, len(target_group) - 1
    if ed < 0:
        return 0

    while st <= ed:
        mi = (st + ed) // 2
        if target_group[mi] < score:  # ASC
            st = mi + 1
        else:
            ed = mi - 1

    return len(target_group) - st


ans = solution(
    [
        "java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50",
    ],
    [
        "java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150",
    ],
)
print(ans)
