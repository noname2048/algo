def solution(info, query):
    info = [i.split(" ") for i in info]
    answer = []
    for q in query:
        word = q.split("and")
        lang_c, aria_c, exp_c, food_score_c = map(lambda x: x.strip(), word)
        food_c, score_c = food_score_c.split(" ")

        result = 0
        for lang, aria, exp, food, score in info:
            cond = 0
            if lang_c == "-" or (lang_c != "-" and lang_c == lang):
                cond += 1
            if aria_c == "-" or (aria_c != "-" and aria_c == aria):
                cond += 1
            if exp_c == "-" or (exp_c != "-" and exp_c == exp):
                cond += 1
            if food_c == "-" or (food_c != "-" and food_c == food):
                cond += 1
            if score_c == "-" or (score_c != "-" and int(score) >= int(score_c)):
                cond += 1
            if cond == 5:
                result += 1

        answer += [result]
    return answer
