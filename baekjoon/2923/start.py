min_a = 100
max_a = 1

min_b = 100
max_b = 1

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())

    min_a = min(min_a, a)
    max_a = max(max_a, a)

    min_b = min(min_b, b)
    max_b = max(max_b, b)

    print(max(min_a + max_b, max_a + min_b))
