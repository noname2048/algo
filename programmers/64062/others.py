# 고재철의 풀이

def solution(stones, k):
    answer = 0
    start, end = 0, max(stones)
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for s in stones:
            if s - mid < 0:
                count += 1
            else:
                count = 0
            if count == k:
                end = mid - 1
                break
        if count < k:
            answer = mid
            start = mid + 1

    return answer