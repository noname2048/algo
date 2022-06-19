def solution(N, stages):
    person_count = len(stages)
    count = [0] * (N + 2)
    for stage in stages:
        count[stage] += 1

    fail_rates = {}

    for stage in range(1, N + 1):
        if person_count == 0:
            fail_rates[stage] = 0
        else:
            fail_rates[stage] = count[stage] / person_count
            person_count -= count[stage]

    return sorted(fail_rates, key=lambda x: fail_rates[x], reverse=True)
