# 재수정

import re

# 소수 구하는 함수
def is_prime(num):
    if num < 2:
        return False

    sqrt = int(num**0.5)
    for i in range(2, sqrt + 1):
        if num % i == 0:
            return False
    else:
        return True


def solution(n, k):
    k_base_str = ""
    while n > 0:
        n, r = n // k, n % k
        k_base_str = str(r) + k_base_str

    extracted_int_str = re.sub(r"[0]+", "-", k_base_str)
    extracted_int_str = extracted_int_str.split("-")

    answer = 0
    for int_str in extracted_int_str:
        if len(int_str) > 0:
            n = int(int_str)
            if is_prime(n):
                answer += 1

    return answer


def detail_error(k_base_str):
    extracted_int_str = re.sub(r"[0]+", "-", k_base_str)
    extracted_int_str = extracted_int_str.split("-")

    for int_str in extracted_int_str:
        if len(int_str) <= 0:
            print(extracted_int_str, int_str)


def test_1():
    n, k = 437674, 3
    ans = solution(n, k)
    assert ans == 3


def test_2():
    n, k = 110011, 10
    ans = solution(n, k)
    assert ans == 2
