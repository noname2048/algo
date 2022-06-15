arr = [1, 2, 5, 6, 20]
k = 5

arr = [1, 2, 3, 4, 5, 6, 8, 9, 10]
k = 100

arr = [10, 1000]
k = 900

# 제안했던 테스트
# 1. arr가 빈칸이면?
# 2. 빽빽한 arr + k
# 3. 빈칸 수보다 작은 k
# 4. 빈칸 수보다 큰 k

def solution(arr, k):
    empty_number_count = arr[-1] - len(arr)

    if empty_number_count == k:
        return len(arr) + k

    elif empty_number_count < k:
        return arr[-1] + (k - empty_number_count)

    else:
        #  empty_number_count > k:
        for arr_index in range(len(arr)):
            local_empty_number_count = arr[arr_index] - (arr_index + 1)
            if local_empty_number_count >= k:
                return (arr[arr_index] - 1) - (local_empty_number_count - k)


ans = solution(arr, k)
print(ans)

# 생각이 잘 안난다면 좀더 열심히 변수명을 세분화해서 지어보자

# 피드백
# - 변수 이름 괜찮게 쓰는것 같아요
# - 주석 좋아요
# - 이해력은 보통인것 같아요
# - 구현하는데 시간이 오래 걸려요

# 리팩토링의 정의가 무엇일까요?
