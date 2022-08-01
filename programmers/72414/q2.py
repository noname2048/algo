from sys import stdin

input = stdin.readline


def str_to_sec(s: str):
    hours, minutes, seconds = s.split(":")
    return int(seconds) + int(minutes) * 60 + int(hours) * 3600


def sec_to_str(i: int):
    hours, i = divmod(i, 3600)
    minutes, i = divmod(i, 60)
    seconds = i
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def solution(play_time, adv_time, logs):
    play_sec = str_to_sec(play_time)
    adv_sec = str_to_sec(adv_time)

    cache = [0] * (play_sec + 1)
    for log in logs:
        times = log.split("-")
        st, ed = map(str_to_sec, times)
        cache[st] += 1
        cache[ed] -= 1

    for idx in range(1, len(cache)):
        cache[idx] += cache[idx - 1]

    st = 0
    ed = adv_sec
    total = sum(cache[st:ed])

    mx = total
    mx_pos = st

    for idx in range(0, play_sec - adv_sec + 1):
        total -= cache[idx]
        total += cache[idx + adv_sec]

        if mx < total:
            mx = total
            mx_pos = idx + 1

    answer = sec_to_str(mx_pos)
    return answer


def test_case_1():
    play_time = "02:03:55"
    adv_time = "00:14:15"
    logs = [
        "01:20:15-01:45:14",
        "00:40:31-01:00:00",
        "00:25:50-00:48:29",
        "01:30:59-01:53:29",
        "01:37:44-02:02:30",
    ]
    result = "01:30:59"
    ans = solution(play_time, adv_time, logs)
    assert result == ans


def test_case_2():
    play_time = "99:59:59"
    adv_time = "25:00:00"
    logs = [
        "69:59:59-89:59:59",
        "01:00:00-21:00:00",
        "79:59:59-99:59:59",
        "11:00:00-31:00:00",
    ]
    result = "01:00:00"
    ans = solution(play_time, adv_time, logs)
    assert result == ans


def test_case_3():
    play_time = "50:00:00"
    adv_time = "50:00:00"
    logs = [
        "15:36:51-38:21:49",
        "10:14:18-15:36:51",
        "38:21:49-42:51:45",
    ]
    result = "00:00:00"
    ans = solution(play_time, adv_time, logs)
    assert result == ans


if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
