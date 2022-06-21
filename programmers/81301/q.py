def solution(s):
    word = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    nums = "1234567890"
    ans = ""
    i = 0
    while len(s) > i:
        if s[i] in nums:
            ans += s[i]
            i += 1
        for j in range(i + 1, len(s) + 1):
            if s[i:j] in word:
                ans += str(word[s[i:j]])
                i = j
                break
    return int(ans)


ans = solution("one4seveneight")
print(ans)
