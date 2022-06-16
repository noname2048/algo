import re


def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub(r"[^a-z0-9-_.]", "", new_id)
    new_id = re.sub(r"^.|.$", "", new_id)
    new_id = "a" if len(new_id) == 0 else new_id[:15]
    new_id = new_id[:-1] if new_id[-1] == "." else new_id
    new_id = new_id.ljust(3, new_id[-1]) if len(new_id) < 3 else new_id
    return new_id
