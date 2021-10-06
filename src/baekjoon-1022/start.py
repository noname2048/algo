# import logging

# logging.basicConfig(filename="log.txt", filemode="w", level=logging.DEBUG)
from enum import Enum

pos = [0, 0]


class Dir(Enum):
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3


dir_pos = [[0, 1], [-1, 0], [0, -1], [1, 0]]

# r1, c1, r2, c2 = map(int, input().split())
r1, c1, r2, c2 = [-7, -7, 7, 7]
# r1, c1, r2, c2 = [-3, -3, 2, 0]
r_size = r2 - r1 + 1
c_size = c2 - c1 + 1

mem = [[-1] * c_size for _ in range(r_size)]

number = 1
base = 0
base_distance = 1

if r1 <= 0 <= r2 and c1 <= 0 <= c2:
    # logging.debug(f"원점 {-r1 + 1}, {-c1 + 1}")
    mem[-r1][-c1] = 1

cond = True
while cond:
    for i in range(base_distance):
        pos[0] += dir_pos[base][0]
        pos[1] += dir_pos[base][1]
        number += 1

        if r1 <= pos[0] <= r2 and c1 <= pos[1] <= c2:
            # logging.debug(f"{pos} -> {pos[0] - r1}, {pos[1] - c1}")
            mem[pos[0] - r1][pos[1] - c1] = number

            if min(map(min, mem)) > 0:
                cond = False

    base = (base + 1) % 4
    if base % 2 == 0:
        base_distance += 1

max_number = max(max(mem))
number_len = 0
while max_number > 0:
    max_number = max_number // 10
    number_len += 1

for i in range(r_size):
    line = " ".join(map(lambda x: str(x).rjust(number_len, " "), mem[i]))
    print(line)
