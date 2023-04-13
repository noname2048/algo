# v2 에서 누가 만들어둔 코드를 역공학으로 분석해보니
# order 가 말도 안되는 수준으로 나와서
# 다시 생각해보았는데 ci, c1, c2 .. 가 해당 카드의 순서가 아님을 알아내었음
# v2를 이 방식으로 수정


def main(n=None):
    if n == None:
        n = int(input())

    a = list(range(1, n + 1, 2))
    b = list(range(2, n + 1, 2))
    a.reverse()
    nums = a + b
    orders = [(n - 1) // 2 + 1]

    next = 1
    for _ in range(0, n - 1):
        idx = orders[-1] - 1
        here = nums[idx]
        orders.append((idx + 1) + (here * next))
        next *= -1

    print("YES")
    print(" ".join(map(str, nums)))
    print(" ".join(map(str, orders)))


for i in range(4, 6):
    main(i)
