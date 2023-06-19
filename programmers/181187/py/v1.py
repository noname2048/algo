def main():
    answer = solution(2, 3)
    print(answer)


def solution(r1, r2):
    answer = 0

    for y in range(-r2, r2 + 1):
        for x in range(-r2, r2 + 1):
            if r1**2 <= x**2 + y**2 <= r2**2:
                answer += 1
    return answer


main()
