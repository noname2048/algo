from math import gcd

# debug = True
# if debug:
#     import sys
#     import logging

#     sys.stdin = open("input1.txt", "r")
#     logging.basicConfig(filename="log.txt", filemode="w", level=logging.DEBUG)

# 문제 제시 조건 n[1, 15], nums(n개), k[1, 100]
n = int(input())
num = [""] * n
for i in range(n):
    num[i] = input()
k = int(input())

# dp_cache[1 <= 상태 << 2^n - 1][0 <= 나머지 <= k] = 가능한 경우의 수
dp_cache = [[-1] * k for _ in range(int(pow(2, n)) - 1 + 1)]
# 이때 초기화는 1개 순열만 선택했을때
for i in range(n):
    for j in range(k):
        dp_cache[1 << i][j] = 0
    temp = int(num[i]) % k
    dp_cache[1 << i][temp] = 1

# remainder_cache[i] = num[i] 를 k 로 나눈 나머지
remainder_cache = [0] * n
for i, e in enumerate(num):
    remainder_cache[i] = int(num[i]) % k

# digit_cache[i] = 10 ^ i 수를  k 로 나눈 나머지
digit_cache = [0] * 51
digit_cache[0] = 1 % k
for i in range(1, 51):
    digit_cache[i] = digit_cache[i - 1] * 10 % k


def re(state, remain):
    # 상태가 bin(1111) 일때
    # bin(0111)[0~k] bin(1011)[0~k] bin(1101)[0~k] bin(1110)[0~k] 을 호출하는 재귀함수
    # 즉 현재 상태보나 낮은 상태값을 재귀로 호출한다
    # "dp[상태][나머지] = 존재 할 수 있는 순열 수"를 참조
    # dp[0][아무거나] = 0

    if dp_cache[state][remain] != -1:
        # if debug:
        #     logging.debug(f" = re({state}, {remain}) = {dp_cache[state][remain]}")
        return dp_cache[state][remain]

    # if debug:
    #     logging.debug(f"open - re({state}, {remain})")

    # 현 state 초기화
    for i in range(k):
        dp_cache[state][i] = 0

    # 현 state 채우기
    for included_number in range(n):
        if state & (1 << included_number):
            last_state = state & ~(1 << included_number)
            e = len(num[included_number])

            for candidated_remains in range(k):
                # 점화식
                # (abc * 100 + de) % k
                # (abc % k) * (100 % k) + de % k
                # (x % k) * y + z
                x = re(last_state, candidated_remains)
                y = digit_cache[e]
                z = remainder_cache[included_number]

                next_reamin = ((x % k) * y + z) % k
                dp_cache[state][next_reamin] += x

    # if debug:
    # logging.debug(f"close - re({state}, {remain}) = {dp_cache[state][remain]}")

    return dp_cache[state][remain]


ans_state = pow(2, n) - 1
ans = re(ans_state, 0)
total = sum(dp_cache[ans_state])
g = gcd(ans, total)
print(f"{int(ans/g)}/{int(total/g)}")
