# 탁구 경기
# 다른 사람 코드 참조
# 60ms
import sys

input = sys.stdin.readline


def main():
    D = P = 0
    for _ in range(int(input())):
        if input().rstrip() == "D":
            D += 1
        else:
            P += 1
        if abs(D - P) > 1:
            print(f"{D}:{P}")
            return
    print(f"{D}:{P}")

main()
