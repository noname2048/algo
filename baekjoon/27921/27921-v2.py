# v1 으로 부터 컨볼루젼 에러 해결
import sys


# def pretext():
#     def inner():
#         with open("p9.txt", "r") as f:
#             content = f.readlines()
#             yield from content

#     temp = inner()

#     def readline():
#         return next(temp)

#     return readline


# input = pretext()
input = sys.stdin.readline


def main():
    h1, w1 = map(int, input().split())
    arr1 = []
    for _ in range(h1):
        arr1.append(input().rstrip())

    h2, w2 = map(int, input().split())
    arr2 = []
    for _ in range(h2):
        arr2.append(input().rstrip())

    coin = 0
    for y in range(h1):
        for x in range(w1):
            if arr1[y][x] == "O":
                coin += 1

    max_overlap_one_count = 0
    for over_y in range(-(h1 - 1), h2):
        for over_x in range(-(w1 - 1), w2):
            overlap_one_count = 0
            for y in range(h1):
                for x in range(w1):
                    y2 = over_y + y
                    x2 = over_x + x
                    if 0 <= y2 < h2 and 0 <= x2 < w2:
                        if arr1[y][x] == "O" and arr2[y2][x2] == "O":
                            overlap_one_count += 1
            max_overlap_one_count = max(overlap_one_count, max_overlap_one_count)
            # if overlap_one_count > 0:
            #     # print(over_y, over_x, overlap_one_count)

    print(coin - max_overlap_one_count)


main()
