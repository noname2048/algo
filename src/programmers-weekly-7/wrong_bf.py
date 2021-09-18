# bf 솔루션: 크기비교
def solution(enter, leave):
    
    ans = [0 for _ in range(len(enter) + 1)]
    cache = [[-1, -1] for _ in range(len(enter) + 1)]

    for (order, ele) in enumerate(zip(enter, leave)):
        en, le = ele
        cache[en][0] = order + 1
        cache[le][1] = order + 1

    for (idx, target) in enumerate(range(1, len(enter) + 1)):
        for subtarget in leave:

            if target == subtarget:
                continue

            target_enter_order = cache[target][0]
            target_leave_order = cache[target][1]
            subtarget_enter_order = cache[subtarget][0]
            subtarget_leave_order = cache[subtarget][1]

            willbe_minus = (target_enter_order - subtarget_enter_order) * (target_leave_order - subtarget_leave_order)

            if willbe_minus < 0:
                ans[target] += 1

    return ans[1:]

        
    
if __name__ == "__main__":
    qs = [
            # [[1, 3 , 2], [1, 2, 3]],
            [[1, 4, 2, 3], [2, 1, 3, 4]],
            # [[3, 2, 1], [2, 1, 3]],
    ]

    for q in qs:
        print(solution(q[0], q[1]))
