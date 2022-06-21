def solution(n, arr1, arr2):
    answer = []

    arr = [arr1[i] | arr2[2] for i in range(n)]
    for num in arr:
        bin_str = f"{num:020b}"[-n:]
        answer += ["".join("#" if temp == "1" else " " for temp in bin_str)]
    return answer


ans = solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
print(ans)
