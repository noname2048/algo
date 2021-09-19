class Solution:

    def numDistinct(self, s: str, t: str) -> int:
        self.origin_word = s
        self.target_word = t
        
        self.mutable_word_list = []
        self.solve_list = []
        self.ans = 0
        self.dps(0)
        return self.ans

    def dps(self, curr_idx: int) -> None:

        if len(self.mutable_word_list) >= len(self.target_word):
            self.ans += 1
            print(self.solve_list)
            return

        for idx in range(curr_idx, len(self.origin_word)):

            w = self.origin_word[idx]
            l = len(self.mutable_word_list)

            if w == self.target_word[l]:
                self.mutable_word_list.append(w)
                self.solve_list.append(idx)
                self.dps(idx + 1)
                self.mutable_word_list.pop()
                self.solve_list.pop()

if __name__ == "__main__":
    a = Solution()
    print(a.numDistinct('babgbag', 'bag'))
