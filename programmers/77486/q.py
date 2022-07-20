from collections import defaultdict

parent_dict = {}
value_dict = defaultdict(int)


def bottom_up(index, amount):
    value = amount * 100
    pa = parent_dict[index]
    while pa and value > 0:
        fee = int(value * 0.1)
        value -= fee
        value_dict[index] += value
        value = fee

        # next while
        index = pa
        pa = parent_dict.get(index, None)


def solution(enroll, referral, seller, amount):
    for ch, pa in zip(enroll, referral):
        parent_dict[ch] = pa

    for se, am in zip(seller, amount):
        bottom_up(se, am)

    answer = [value_dict[en] for en in enroll]
    return answer
