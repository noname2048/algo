def main(n=None):
    if n == None:
        n = int(input())
    nums = [-1] * n
    orders = [-1] * n

    idx = 0
    for i in range(n - 1, 0, -2):
        nums[idx] = i
        idx += 1
    nums[idx] = n
    idx += 1
    for i in range(2 - n % 2, n - 1, 2):
        nums[idx] = i
        idx += 1

    idx = 0
    for i in range(1, n + 1, 2):
        orders[idx] = i
        idx += 1
    for i in range(n - n % 2, 0, -2):
        orders[idx] = i
        idx += 1

    print("YES")
    print(*nums, sep=" ")
    print(*orders, sep=" ")


for i in range(10, 20):
    main(i)

# 분명 맞는 거 같은데 안풀려서 질문게시판에 남겼음
# https://www.acmicpc.net/board/view/115672
