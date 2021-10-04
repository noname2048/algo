a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

first_min = min(min(a))
second_min = min(map(min, a))

print(first_min)
print(second_min)
