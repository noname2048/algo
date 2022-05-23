def solution(fees, records):
    def caculate_fee(fees, duration):
        ret = 0
        if duration <= fees[0]:
            ret = fees[1]
        elif duration > fees[0]:
            advance = duration - fees[0]
            if advance % fees[2] == 0:
                ret = fees[1] + (advance // fees[2]) * fees[3]
            else:
                ret = fees[1] + ((advance + fees[2]) // fees[2]) * fees[3]

        return ret

    cars_inpark = dict()
    minutes = dict()
    ans = dict()

    for record in records:
        temp = record.split(" ")
        time_str = temp[0]
        car_num = int(temp[1])
        in_out_str = temp[2]

        if len(in_out_str) == 2:
            start_min = int(time_str[0:2]) * 60 + int(time_str[3:5])
            cars_inpark[car_num] = start_min
        else:
            start_min = cars_inpark[car_num]
            del cars_inpark[car_num]
            end_min = int(time_str[0:2]) * 60 + int(time_str[3:5])
            duration = end_min - start_min

            if car_num in minutes:
                minutes[car_num] += duration
            else:
                minutes[car_num] = duration

    for car_num, start_min in cars_inpark.items():
        end_min = 23 * 60 + 59
        duration = end_min - start_min

        if car_num in minutes:
            minutes[car_num] += duration
        else:
            minutes[car_num] = duration

    for car_num, duration in minutes.items():
        value = caculate_fee(fees, duration)
        if car_num in ans:
            ans[car_num] += value
        else:
            ans[car_num] = value

    sorted_ans = sorted(ans.items())
    answer = [v for k, v in sorted_ans]
    return answer


def test_1():
    f = [180, 5000, 10, 600]
    r = [
        "05:34 5961 IN",
        "06:00 0000 IN",
        "06:34 0000 OUT",
        "07:59 5961 OUT",
        "07:59 0148 IN",
        "18:59 0000 IN",
        "19:09 0148 OUT",
        "22:59 5961 IN",
        "23:00 5961 OUT",
    ]
    a = [14600, 34400, 5000]

    answer = solution(f, r)
    assert a == answer


if __name__ == "__main__":
    test_1()
