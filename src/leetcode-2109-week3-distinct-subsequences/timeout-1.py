# import logging
from typing import List, Tuple
# logging.basicConfig(filename="log.txt", filemode="w", level=logging.INFO)

class Solution:

    def numDistinct(self, s: str, t: str) -> int:
        self.origin_word = s
        self.len_origin = len(self.origin_word)
        self.target_word = t
        self.len_target = len(self.target_word)
        
        return self.dps(0, '', [])

    def dps(self, curr_idx: int, word: str, vec: List[int]) -> int:

        if len(word) >= self.len_target:
            # logging.info(word)
            # logging.info(vec)
            return 1

        temp_sum = 0
        for next_idx in range(curr_idx, self.len_origin):
            if len(word) >= self.len_target:
                break

            if self.origin_word[next_idx] == self.target_word[len(word)]:
                new_word = f'{word}{self.origin_word[next_idx]}'
                new_vec = [*vec, next_idx]
                temp_sum += self.dps(next_idx + 1, new_word, new_vec)

        return temp_sum

if __name__ == "__main__":
    a = Solution()
    print(a.numDistinct('babgbag', 'bag'))
