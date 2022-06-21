def solution1(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i | j)[2:])
        a12 = a12.rjust(n, "0")
        a12 = a12.replace("1", "#")
        a12 = a12.replace("0", " ")
        answer.append(a12)
    return answer


def solution2(n, *maps):
    return [line(n, a | b) for a, b in zip(*maps)]


def line(n, x):
    return "".join(" #"[int(i)] for i in f"{x:016b}"[-n:])
