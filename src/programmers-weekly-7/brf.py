from collections import deque

def solution(enter, leave):
    l = len(enter)
    ans = [0 for _ in range(l + 1)]
    cache = [set() for _ in range(l + 1)]

    room = set()

    enter_idx = 0 
    leave_idx = 0

    while leave_idx < l:

        if leave[leave_idx] in room:
            for i in room:
                cache[i] |= room - {i} 
            room.remove(leave[leave_idx])
            leave_idx += 1

        else:
            if enter_idx >= l:
                break
            room.add(enter[enter_idx])
            enter_idx += 1

    ans = list(map(len, cache))[1:]

    return ans

if __name__ == "__main__":
    qs = [
        [[1, 3, 2], [1, 2, 3]],
        [[1, 4, 2, 3], [2, 1, 3, 4]],
        [[3, 2, 1], [2, 1, 3]],
        [[1, 4, 2, 3], [2, 1, 4, 3]],
    ]
    for q in qs:
        enter, leave = q
        print(solution(enter, leave))
