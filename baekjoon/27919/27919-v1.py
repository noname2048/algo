import sys

input = sys.stdin.readline


def main():
    uc = 0
    dp = 0
    for ch in input().rstrip():
        if ch in ("U", "C"):
            uc += 1
        else:
            dp += 1

    if uc > dp:
        if dp > 0:
            print("UDP")
        else:
            print("U")
        return
    elif dp >= uc:
        # D, P 가능
        # U가 가능한가?
        if uc > 0 and uc > (dp + 1) // 2:
            print("UDP")
        else:
            print("DP")
        return


main()
