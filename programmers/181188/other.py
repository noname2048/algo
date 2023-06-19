def solution(targets):
    answer = 0

    # 끝나는 시간을 기준으로 정렬
    targets.sort(key=lambda x: x[1])

    # 마지막 로켓 위치
    available_intercept_pos = 0

    for s, e in targets:
        # 이전의 로켓으로 요격 불가능하면 
        if available_intercept_pos <= s:
            answer += 1
            available_intercept_pos = e 
    
    return answer
    