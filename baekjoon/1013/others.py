import sys


def check(x):
    global pat
    if x == len(pat):
        return "YES"
    if pat[x : x + 2] == "01":
        if check(x + 2) == "YES":
            return "YES"
    elif pat[x : x + 3] == "100":
        for i in range(x + 3, len(pat)):
            if pat[i] == "1":
                for j in range(i, len(pat)):
                    if pat[j] == "0":
                        break
                    if check(j + 1) == "YES":
                        return "YES"
                break
    return "NO"


n = int(sys.stdin.readline().split()[0])
for _ in range(n):
    pat = sys.stdin.readline().split()[0]
    print(check(0))
