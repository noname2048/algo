def solution(survey, choices):
    hash = {"RT":0, "CF":0, "JM":0, "AN":0}
    for sur, choi in zip(survey, choices):
        if sur not in hash.keys():
            sur = sur[::-1]
            hash[sur] -= choi - 4
        else:
            hash[sur] += choi - 4
    
    result = ""
    for name, value in hash.items():
        if value > 0:
            result += name[1]
        else:
            result += name[0]
    return result
