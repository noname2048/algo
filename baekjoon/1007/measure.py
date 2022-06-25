import timeit


def make_pairs_a(n: int):
    pairs = []
    for i in range(n):
        pair = (i * 2 + 1, i * 2 + 2)
        pairs.append(pair)
    return pairs


def make_pairs_b(n: int):
    pairs = [[0, 0] for _ in range(n)]
    for i in range(n):
        pairs[i][0], pairs[i][1] = i * 2 + 1, i * 2 + 2


def make_pairs_c(n: int):
    pairs = []
    for i in range(n):
        pairs += [(i * 2 + 1, i * 2 + 2)]


def make_pairs_d(n: int):
    pairs = []
    for i in range(n):
        pairs.append([i * 2 + 1, i * 2 + 2])


a = timeit.timeit("ans = make_pairs_a(100)", globals=globals())
b = timeit.timeit("ans = make_pairs_b(100)", globals=globals())
c = timeit.timeit("ans = make_pairs_c(100)", globals=globals())
d = timeit.timeit("ans = make_pairs_d(100)", globals=globals())
print(a, b, c, d)

# 결과
# a 20.993, append, tupple #21
# b 30.639, modify, list #28
# c 23.062, +=, list #23
# d 27.731, append, list #22

# 이상하게도 리스트를 append 하는 것 보다,
# 만들어두고 수정을 하는게 더 오래 걸렸다.
