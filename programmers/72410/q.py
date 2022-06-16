import re


def solution(new_id):
    id = list(new_id)
    # lv1 ~ 2
    new_id = []
    diff = ord("A") - ord("a")
    for character in id:
        new_character = character
        if ord("A") <= ord(character) <= ord("Z"):
            new_character = chr(ord(character) - diff)
        elif character in list("~!@#$%^&*()=+[{]}:?,<>/"):
            new_character = ""

        new_id += [new_character]
    new_id = "".join(new_id)

    # lv3
    new_id: str = re.sub(r"[.]+", ".", new_id)
    new_id = list(new_id)

    # lv4
    if len(new_id) > 0 and new_id[0] == ".":
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == ".":
        new_id = new_id[:-1]

    # lv5
    if len(new_id) == 0:
        new_id += ["a"]

    # lv6
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if len(new_id) > 0 and new_id[-1] == ".":
        new_id = new_id[:-1]

    # lv7
    while len(new_id) <= 2:
        new_id += [new_id[-1]]

    return "".join(new_id)


# ans = solution("...!@BaT#*..y.abcdefghijklm")
# ans = solution("z-+.^.")
# ans = solution("=.=")
# ans = solution("123_.def")
ans = solution("abcdefghijklmn.p")
print(ans)
