from typing import List, Tuple


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """주어진 단어들을 Anagram 집합으로 그룹지어 리턴하는 함수

        주어진 단어를 단어의 수를 이용해 구분지을 수 있는 key로 만들어,
        dict을 통해 구분짓습니다.

        :params List[str] strs: 단어들의 집합
        :return List[List[str]]: 단어들을 그룹으로 나눈 결과
        """
        groups = dict()
        for str_item in strs:
            encoded = self.encode_alphabet_manual(str_item)
            if encoded in groups:
                groups[encoded].append(str_item)
            else:
                groups[encoded] = [str_item]

        ans = []
        for v in groups.values():
            ans.append(v)
        return ans

    def encode_alphabet(self, s: str) -> Tuple:
        """주어진 문자열(a-z)을 개수가 담긴 Tuple 형태로 리턴하는 함수

        (0, 2, 0, ..., 3) 와 같은 형태로 리턴합니다.

        :param str s: a-z까지 중복될 수 있는 문자열
        :return Tuple: (0, 1, 0, ..., 3) 와 같은 길이 26의 Tuple
        """
        alpha = [0] * 26
        for character in s:
            alpha[ord(character) - ord("a")] += 1
        return tuple(alpha)

    def encode_alphabet_manual(self, s: str) -> str:
        """주어진 문자열(a-z)을 개수가 담긴 str 형태로 리턴하는 함수

        'a[0]b[2]c[0]...z[3]' 와 같은 형태로 리턴합니다.

        :param str s: a-z까지 중복될 수 있는 문자열
        :return str: (0, 1, 0, ..., 3) 와 같은 길이가 정해지지 않은 문자열
        """
        alpha = [0] * 26
        for character in s:
            alpha[ord(character) - ord("a")] += 1

        ret = ""
        for i, alpha_item in enumerate(alpha):
            character = i + ord("a")
            ret += f"{character}[{alpha[i]}]"
        return ret
