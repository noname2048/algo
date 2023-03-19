def solution(survey, choices):
    RTCFJMAN = [0] * 8
    s = "RTCFJMAN"
    for sur, choi in zip(survey, choices):
        RTCFJMAN[s.index(sur[1])] += choi - 4

    answer = ""
    for i in range(4):
        if RTCFJMAN[2 * i + 0] < RTCFJMAN[2 * i + 1]:
            answer += s[2 * i + 1]
        else:
            answer += s[2 * i]

    return answer
