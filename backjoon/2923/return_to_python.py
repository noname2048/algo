import sys

sys.stdin = open("input1.txt", "r")
# 어려워서 다음을 참조 https://jaimemin.tistory.com/1013 (감사합니다)
a_list = [0] * 101
b_list = [0] * 101

n = int(sys.stdin.readline())
for i in range(n):
    # 인풋 반영
    a, b = map(int, sys.stdin.readline().strip().split())
    a_list[a] += 1
    b_list[b] += 1

    # 원본 복제와 변수 설정
    a_copy_list = [e for e in a_list]
    b_copy_list = [e for e in b_list]
    local_max = 0
    ai, bi = 100, 1

    # ai(ASC) bi(DESC)
    while ai >= 1 and bi <= 100:
        while ai >= 1 and a_copy_list[ai] == 0:
            ai -= 1
        while bi <= 100 and b_copy_list[bi] == 0:
            bi += 1
        # 하위 로직에 대한 방어적 탈출
        if ai <= 0 or bi >= 101:
            break
        # 최댓값 갱신
        local_max = max(local_max, ai + bi)
        # 중복된 숫자의 빠른 제거
        if a_copy_list[ai] > b_copy_list[bi]:
            a_copy_list[ai] -= b_copy_list[bi]
            b_copy_list[bi] = 0
        else:
            b_copy_list[bi] -= a_copy_list[ai]
            a_copy_list[ai] = 0

    print(local_max)
