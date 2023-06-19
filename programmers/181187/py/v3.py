# 한칸씩 이동하며 출발과 끝을 구해 빼보기
# x축 포함, y축 제외
import math


def main():
    answer = solution(2, 3)
    print(answer)


def solution(r1, r2):
    answer = 0

    for x in range(1, r2 + 1):
        y2 = math.floor(math.sqrt(r2**2 - x**2))
        y1 = math.ceil(math.sqrt(max(r1**2 - x**2, 0)))
        answer += y2 - y1 + 1

    return answer * 4


main()
