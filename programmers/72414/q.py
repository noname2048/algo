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
    play_sec = str_to_sec(play_time) + 1
    adv_sec = str_to_sec(adv_time) + 1

    q = []
    for log in logs:
        times = log.split("-")
        st, ed = map(str_to_sec, times)
        q.append((st, 1, times[0]))
        q.append((ed + 1, -1, times[1]))

    q.sort()

    part = []
    prev = 0
    viewer = 0
    for item in q:
        here, event, _ = item

        if here == prev:
            viewer += event
        else:
            duration = here - prev - 1
            part.append((prev, here, duration, viewer))

            prev = here
            viewer += event
    else:
        if prev != play_sec:
            duration = play_sec - prev - 1
            part.append((prev, play_sec, duration, viewer))

    mx = 0
    mx_pos = 0
    limit = len(part)

    for idx, item in enumerate(part):
        if item[0] + adv_sec > play_sec:
            break

        total = 0

        st = part[idx][0]
        ed = st + adv_sec

        k = idx
        while k < limit and part[k][1] < ed:
            _, _, duration, viewer = part[k]
            total += duration * viewer
            k += 1
        else:
            total += (ed - part[k][0] - 1) * part[k][3]

        if total > mx:
            mx = total
            mx_pos = st

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
