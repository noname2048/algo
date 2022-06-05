def solution(info, query):
    info = [i.split(" ") for i in info]
    answer = []
    for q in query:
        word = q.split("and")
        lang_c, aria_c, exp_c, food_score_c = map(lambda x: x.strip(), word)
        food_c, score_c = food_score_c.split(" ")

        temp = info
        temp = [i for i in temp if lang_c == "-" or (lang_c != "-" and lang_c == i[0])]
        temp = [i for i in temp if aria_c == "-" or (aria_c != "-" and aria_c == i[1])]
        temp = [i for i in temp if exp_c == "-" or (exp_c != "-" and exp_c == i[2])]
        temp = [i for i in temp if food_c == "-" or (food_c != "-" and food_c == i[3])]
        temp = [
            i
            for i in temp
            if score_c == "-" or (score_c != "-" and int(i[4]) >= int(score_c))
        ]
        answer += [len(temp)]
    return answer


solution(
    [
        "java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50",
    ],
    [
        "java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150",
    ],
)
