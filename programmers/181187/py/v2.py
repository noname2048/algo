# 1사분면만 조사 (y축 포함, x축 제외)

def main():
    answer = solution(2, 3)
    print(answer)


def solution(r1, r2):
    answer = 0

    for y in range(1, r2 + 1):
        for x in range(0, r2 + 1):
            if r1**2 <= x**2 + y**2 <= r2**2:
                answer += 1
    return answer * 4


main()
