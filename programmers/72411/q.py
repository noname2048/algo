# 메뉴 리뉴얼
from collections import defaultdict


def solution(orders, course):

    # 사전만들기
    # 서브문자열인지 확인하면서 추가하기
    # 2 이상일 경우 리턴하기

    word_dict = defaultdict(int)
    for c in reversed(course):
        for o in orders:
            len_o = len(o)
            if len_o < c:
                continue
            for i in range(len_o - c + 1):
                new_course = o[i : i + c]
                word_dict[new_course] += 1

    new_word_dict = word_dict.copy()
    for k, v in word_dict.items():
        if v < 2:
            del new_word_dict[k]
    word_dict = new_word_dict.copy()

    tags = []
    for c in reversed(course):
        tags.append([k for k in word_dict.keys() if len(k) == c])

    for tag in tags:
        for w in tag:
            in_flag = False
            for k in word_dict.keys():
                if w != k and w in k:
                    in_flag = True
                    break
            if in_flag:
                del new_word_dict[w]

    answer = sorted(new_word_dict.keys())
    return answer


def test_1():
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2, 3, 4]
    result = ["AC", "ACDE", "BCFG", "CDE"]
    assert result == solution(orders, course)


def test_2():
    orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
    course = [2, 3, 5]
    result = ["ACD", "AD", "ADE", "CD", "XYZ"]
    assert result == solution(orders, course)


def test_3():
    orders = ["XYZ", "XWY", "WXA"]
    course = [2, 3, 4]
    result = ["WX", "XY"]
    assert result == solution(orders, course)


test_1()
