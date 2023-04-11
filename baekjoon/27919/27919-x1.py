# https://www.acmicpc.net/source/58251960
u, c, d, p  = map(input().count, ("UCDP"))
uc, dp = u + c, d + p
print("U" * (uc > dp - dp // 2) + "DP" * (dp > 0))
