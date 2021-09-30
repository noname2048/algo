def solution(sizes):
    max_x = max_y = 0

    for x, y in sizes:
        if x > y:
            a, b = y, x
        else:
            a, b = x, y
        
        max_x = max(max_x, a)
        max_y = max(max_y, b)
    
    answer = max_x * max_y
    return answer


qs = []
q = [[60, 50], [30, 70], [60, 30], [80, 40]]
qs.append(q)
q = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
qs.append(q)
q = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
qs.append(q)

for q in qs:
    print(solution(q))
