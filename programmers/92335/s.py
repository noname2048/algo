# k진수에서 소수 개수 구하기
# 2022 카카오 블라인드 채용
# 레벨2
import re


def prime_func():
    idx = 2
    prime = {2: True}

    def inner(num):
        nonlocal idx, prime

        sqrt = int(num**0.5) + 1
        for i in range(idx + 1, sqrt + 1):
            # 소수 저장소의 증가
            for p in prime.keys():
                if i % p == 0:
                    break
            else:
                prime[i] = True

        for p in prime.keys():
            if num % p == 0:
                return False
        else:
            return True

    return inner


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

    is_prime = prime_func()

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
