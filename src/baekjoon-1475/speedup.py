n = str(input().strip())
cache = [0] * 10
for idx, num in enumerate("0123456789"):
    cache[idx] = n.count(num)

cache[6] = (cache[6] + cache[9] + 1) // 2
print(max(cache[:-1]))
