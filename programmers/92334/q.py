from collections import defaultdict


def solution(id_list, report, k):
    warn = defaultdict(set)
    subs = defaultdict(int)

    for r in report:
        a, b = r.split(" ")
        warn[b] |= {a}

    for key, v in warn.items():
        if len(v) >= k:
            for s in v:
                subs[s] += 1
            subs[k] += 1

    answer = [subs[id] for id in id_list]
    return answer


def test_1():
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
    k = 2
    assert [2, 1, 1, 0] == solution(id_list, report, k)


def test_2():
    id_list = ["con", "ryan"]
    report = ["ryan con", "ryan con", "ryan con", "ryan con"]
    k = 3
    assert [0, 0] == solution(id_list, report, k)


test_1()
