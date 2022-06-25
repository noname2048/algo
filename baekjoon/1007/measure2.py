"""
python 디폴트 라이브러리인 comb가 빠를까,
내가 짠 comb가 빠를까
"""
import string

s = list(range(20))


def comb(items, r):
    ans = []

    def re(index, start, choice):
        nonlocal items, r, ans
        if index == r:
            ans.append(choice)
            return

        remain = r - index
        for i in range(start, len(items) - remain + 1):
            re(index + 1, i + 1, choice + [s[i]])

    re(0, 0, [])
    return


from itertools import combinations
import timeit

a = timeit.timeit("ans = comb(s, 10)", number=20, globals=globals())
b = timeit.timeit("ans = combinations(s, 10)", number=20, globals=globals())
print(a)  # 4.1
print(b)  # 1.5
