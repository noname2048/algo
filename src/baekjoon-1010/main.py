import logging

logging.basicConfig(filename="log.txt", filemode="w", level=logging.INFO)

def solution(q: list):
    a, b = q
    return re(b, a)

cache = [[-1 for _ in range(30)] for _ in range(30)]
def re(a, b):
    logging.info("re({}, {})".format(a, b))

    if cache[a][b] != -1:
        return cache[a][b]
    elif a == 1 or a == b:
        cache[a][b] = 1
        return 1
    elif b == 1:
        cache[a][b] = a
        return a
    else:
        cache[a][b] = re(a - 1, b) + re(a - 1, b - 1)
        return cache[a][b]

if __name__ == "__main__":
    que = [[2, 2], [1, 5], [13, 29]]
    ans = list(map(solution, que))
    print(ans)
    logging.info("cache")
    for row in cache:
        logging.info([f"{ele:02d}" for ele in row])
