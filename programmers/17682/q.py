import re


def solution(dart_result):
    round_pattern = re.compile(r"[0-9]+[A-Z][*#]*")
    scores = [0] * 4
    rounds = round_pattern.findall(dart_result)
    for idx, round in enumerate(rounds):
        for character in round:
            if ord("0") <= ord(character) <= ord("9"):
                scores[idx + 1] *= 10
                scores[idx + 1] += ord(character) - ord("0")
            elif character == "S":
                pass
            elif character == "D":
                scores[idx + 1] = scores[idx + 1] * scores[idx + 1]
            elif character == "T":
                scores[idx + 1] = scores[idx + 1] * scores[idx + 1] * scores[idx + 1]
            elif character == "*":
                scores[idx + 1] *= 2
                scores[idx] *= 2
            elif character == "#":
                scores[idx + 1] *= -1
    return sum(scores)


ans = solution("1S2D*3T")
print(ans)
