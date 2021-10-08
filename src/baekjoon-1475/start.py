from collections import defaultdict

n = input()

cache = defaultdict(int)
for char in str(n):
    cache[char] += 1

m = (cache.pop("6", 0) + cache.pop("9", 0) + 1) // 2
ans = max(max(cache.values()) if cache else 0, m)
print(ans)
