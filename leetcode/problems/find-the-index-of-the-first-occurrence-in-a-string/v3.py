def get_lps(needle: str) -> list[int]:
    """return longest prefix suffix array"""
    lps = [0] * len(needle)
    pre = 0
    for i in range(1, len(needle)):
        while pre > 0 and needle[i] != needle[pre]:
            pre = lps[pre - 1]
        if needle[pre] == needle[i]:
            pre += 1
            lps[i] = pre
    return lps


ans = get_lps("bbabbbbabbbabba")
print(ans)


def strStr(haystack, needle):
    lps = get_lps(needle)
    needle_idx = 0
    for hay_idx in range(len(haystack)):
        while needle_idx > 0 and needle[needle_idx] != haystack[hay_idx]:
            needle_idx = lps[needle_idx - 1]
        if needle[needle_idx] == haystack[hay_idx]:
            needle_idx += 1
        if needle_idx == len(needle):
            return hay_idx - needle_idx + 1

    return -1


ans = strStr("sadbutsad", "sad")
print(ans)
ans = strStr("leetcode", "leeto")
print(ans)


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # longest prefix suffix array
        lps = [0] * len(needle)
        pre = 0
        for i in range(1, len(needle)):
            while pre > 0 and needle[i] != needle[pre]:
                pre = lps[pre - 1]
            if needle[pre] == needle[i]:
                pre += 1
            lps[i] = pre

        # needle_idx
        ni = 0
        # haystack_idx
        for hi in range(len(haystack)):
            while ni > 0 and needle[ni] != haystack[hi]:
                ni = lps[ni - 1]
            if needle[ni] == haystack[hi]:
                ni += 1
            if ni == len(needle):
                return hi - ni + 1

        return -1
