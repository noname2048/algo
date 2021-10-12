import sys

sys.stdin = open("input1.txt", "r")


class MyNode:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            cls._instance.append(cls)
        else:
            cls._instance = [cls]
        return super().__new__(cls)

    def __init__(self, num, cnt, next):
        self.num = num  # 숫자
        self.cnt = cnt  # 중복수
        self.next = None  # 다음 노드

    def __str__(self):
        return f"({self.num}, {self.cnt}, {self.next})"

    def __repr__(self):
        return self.__str__()


node_a = MyNode(0, 0, None)
node_b = MyNode(101, 0, None)

n = int(input())
for i in range(n):
    a, b = map(int, input().split())

    pointer_a = node_a
    while pointer_a.next and pointer_a.next.num < a:
        pointer_a = pointer_a.next
    else:
        if pointer_a.num < a:
            temp = MyNode(a, 0, pointer_a.next)
            pointer_a.next = temp
        elif pointer_a.num == a:
            pointer_a.cnt += 1

    pointer_b = node_b
    while pointer_b.next and pointer_b.next.num > b:
        pointer_b = pointer_b.next
    else:
        if pointer_b.num > b:
            temp = MyNode(b, 0, pointer_b.next)
            pointer_b.next = temp
        elif pointer_b.num == a:
            pointer_b.cnt += 1

    pointer_a = node_a.next
    pointer_b = node_b.next
    pos_a = MyNode(pointer_a.num, 1, None)
    pos_b = MyNode(pointer_b.num, 1, None)

    g_max = 0
    for _ in range(i + 1):
        g_max = max(pointer_a.num + pointer_b.num, g_max)

        if pointer_a and pos_a.cnt == pointer_a.cnt:
            pointer_a = pointer_a.next
            pos_a.cnt = 0
        pos_a.cnt += 1

        if pointer_b and pos_b.cnt == pointer_b.cnt:
            pointer_b = pointer_b.next
            pos_a.cnt = 0
        pos_b.cnt += 1

    print(g_max)
