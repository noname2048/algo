def solution(N, stages):
    count = [0] * (N + 2)
    for stage in stages:
        count[stage] += 1

    accumulated_count = [0] * (N + 2)
    accumulated_count[N + 1] = count[N + 1]

    fail_rates = []  # (fail_rate, stage)
    for i in range(N, 0, -1):
        accumulated_count[i] = accumulated_count[i + 1] + count[i]
        if accumulated_count[i] == 0:
            fail_rates += [(0, i)]
        else:
            fail_rates += [(-count[i] / accumulated_count[i], i)]
    fail_rates.reverse()
    fail_rates.sort()
    answer = [stage for _, stage in fail_rates]
    return answer


ans = solution(5, [1, 1, 1])
print(ans)
