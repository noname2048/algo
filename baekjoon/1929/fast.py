# 인풋은 내 방법이랑 같다
m, n = map(int, input().split())

# li = [False, True, True, True ...]
li = [False] + [True] * ((n - 1) // 2)

# operator priority 에 따라서
# 루트(N) / 2 + 1... 나누기 2는 왜들어가는 걸까
for x in range(1, int(n ** 0.5 / 2 + 1)):

    # li[1] 부터 li[K], k는 위 참조)
    if li[x]:
        # python slicing
        # start:end:step 에서 end 를 생략하면 끝까지 인가보다
        # ???
        li[2 * x * (x + 1) :: x * 2 + 1] = [False] * (
            (((n + 1) // 2) - x * x * 2) // (x * 2 + 1)
        )
if m <= 2:
    print(2)
print(
    "\n".join(
        [
            f"{x}"
            for x, val in zip(range(m + (m & 1 == 0), n + 1, 2), li[m // 2 :])
            if val
        ]
    )
)
