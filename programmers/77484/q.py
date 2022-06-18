def solution(lottos, win_nums):
    none_zero_lottos = [num for num in lottos if num != 0]
    zeros = 6 - len(none_zero_lottos)
    hit = 0
    for num in none_zero_lottos:
        if num in win_nums:
            hit += 1
    return [min(7 - (zeros + hit), 6), min(7 - hit, 6)]
