# 소수 구하는 부분을 수정해보기로 결정
# -> 한문제 오류남 (반례가 뭐지)
import re


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
    # quotient, remainder
    k_str = ""
    while n != 0:
        n, r = n // k, n % k
        k_str += str(r)

    k_str = k_str[::-1]
    k_str = re.sub(r"[0]+", " ", k_str)
    nums = k_str.split(" ")
    nums = list(map(int, nums))

    answer = 0
    for n in nums:
        if is_prime(n):
            answer += 1

    return answer


def test_1():
    n, k = 437674, 3
    ans = solution(n, k)
    assert ans == 3


def test_2():
    n, k = 110011, 10
    ans = solution(n, k)
    assert ans == 2


if __name__ == "__main__":
    test_2()
