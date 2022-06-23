def sol(y, x):

    if y == x and x == 0:
        return 1

    elif y == x and y > 0:
        k = y
        a = 8
        sub = 0

    elif abs(y) > abs(x):
        if y < 0:  # UP(x > -x)
            k = -y
            a = 3
            sub = -x
        elif y > 0:  # DOWN(-x > x)
            k = y
            a = 7
            sub = x
    else:
        if x > 0:  # RIGHT SIDE(UPWARD, y > -y)
            k = x
            a = 1
            sub = -y
        else:
            k = -x  # LEFT SIDE(DOWNWARD, -y > y)
            a = 5
            sub = y

    return 4 * k * k + (a - 4) * k + 1 + sub


# 01 인풋으로 부터 ans 크기 구하기
r1, c1, r2, c2 = map(int, input().split())
# r1, c1, r2, c2 = [-3, -3, 3, 3]
# r1, c1, r2, c2 = [-3, -3, 2, 0]
r_size = r2 - r1 + 1
c_size = c2 - c1 + 1

# 02 메모리 만들기
mem = [[-1] * c_size for _ in range(r_size)]
max_number = 0

# 03 점화식 이용해서 채우기
for i in range(r1, r2 + 1):
    for j in range(c1, c2 + 1):
        mem[i - r1][j - c1] = sol(i, j)
        max_number = max(mem[i - r1][j - c1], max_number)

# 04 숫자의 최대 자리수 구하기
number_len = 0
while max_number > 0:
    max_number = max_number // 10
    number_len += 1

# 05 자리수대로 출력하기
for i in range(r_size):
    line = " ".join(map(lambda x: str(x).rjust(number_len, " "), mem[i]))
    print(line)
