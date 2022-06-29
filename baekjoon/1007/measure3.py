import timeit


def sum(number=16_500_000):
    t = 0  # total
    for _ in range(1, number + 1):
        t += 1
    return t


result = timeit.timeit("sum()", number=10, globals=globals())
print(result)
