y, x = 0, 0
dir_y = [0, -1, 0, 1]
dir_x = [1, 0, -1, 0]

r1, c1, r2, c2 = map(int, input().split())
# r1, c1, r2, c2 = [-3, -3, 3, 3]
# r1, c1, r2, c2 = [-3, -3, 2, 0]
r_size = r2 - r1 + 1
c_size = c2 - c1 + 1

mem = [[-1] * c_size for _ in range(r_size)]
total_element = r_size * c_size
element_counter = 0

number = 1
base = 0
base_distance = 1

if r1 <= 0 <= r2 and c1 <= 0 <= c2:
    # logging.debug(f"원점 {-r1 + 1}, {-c1 + 1}")
    mem[-r1][-c1] = 1
    element_counter += 1

cond = True
while cond:

    for i in range(base_distance):
        y += dir_y[base]
        x += dir_x[base]
        number += 1

        if r1 <= y <= r2 and c1 <= x <= c2:
            mem[y - r1][x - c1] = number
            element_counter += 1

            if element_counter >= total_element:
                cond = False

    base = (base + 1) % 4
    if base % 2 == 0:
        base_distance += 1

number_len = 0
while number > 0:
    number = number // 10
    number_len += 1

for i in range(r_size):
    line = " ".join(map(lambda x: str(x).rjust(number_len, " "), mem[i]))
    print(line)
