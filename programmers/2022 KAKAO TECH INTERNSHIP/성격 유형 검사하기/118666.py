class MBTI:
    # abcdefghijklmnopqrstuvwxyz

    RT = 0
    CF = 0
    JM = 0
    AN = 0

    def add(self, category: str, reply: int):
        forward_or_backward = 1
        if category not in ("RT", "CF", "JM", "AN"):
            category = ''.join(reversed(category))
            forward_or_backward = -1

        if reply - 4 == 0:
            return

        align = (reply - 4) * forward_or_backward
        if category == "RT":
            self.RT += align
        elif category == "CF":
            self.CF += align
        elif category == "JM":
            self.JM += align
        elif category == "AN":
            self.AN += align
        else:
            print("error")
            exit()

    def ans(self):
        ret = ""
        ret += "R" if self.RT <= 0 else "T"
        ret += "C" if self.CF <= 0 else "F"
        ret += "J" if self.JM <= 0 else "M"
        ret += "A" if self.AN <= 0 else "N"
        return ret


def solution(survey, choices):
    mbti = MBTI()
    for sur, choi in zip(survey, choices):
        mbti.add(sur, choi)

    print(mbti.ans())
    return mbti.ans()

solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])
# AN+1 CF-1 MJ-2 RT+3 AN-1