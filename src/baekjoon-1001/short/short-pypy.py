import logging

logging.basicConfig(filemode="w", filename="log.txt", level=logging.INFO)

for _ in range(int(input())):
    k, n = map(int, input().split())
    a = b = 1
    logging.info((a, b))
    for i in range(min(k, n - k)):
        a *= n - i
        b *= i + 1
        logging.info((a, b))
    print(a // b)
