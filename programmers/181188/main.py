
X_LIMIT = 100_000_001

def solution(targets):
    answer = 0

    targets.sort(key=lambda x: x[1])
    targets.sort(key=lambda x: x[0])

    queue = []

    s = 0
    e = X_LIMIT

    for idx, target in enumerate(targets):
        s = max(s, target[0])
        e = min(e, target[1])
        queue.append(target)

        if idx != len(targets) - 1:
            s_next = targets[idx + 1][0]
            e_next = targets[idx + 1][1]
            
            if e <= s_next:
                queue.clear()
                answer += 1
                
                s = s_next
                e = e_next

    if queue:
        answer += 1
    
    print(answer)

    return answer


def main():
    solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]])

main()