# https://www.acmicpc.net/source/58139168
v = input().translate(str.maketrans("CP", "UD"))
u, d = v.count("U"), v.count("D")
r = ""
if u > -(-d // 2):
    r += "U"
if d:
    r += "DP"
print(r if r else "C")
