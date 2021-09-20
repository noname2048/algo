class Solution:

    def numDistinct(self, s: str, t: str) -> int:
        self.question = s
        self.target = t
        
        self.alpa_list = [[] for _ in range(52)]
        for (idx, q) in enumerate(self.question):
            if q.islower:
                self.alpa_list[ord(q) - ord('a') + 26].append(idx)
            else:
                self.alpa_list[ord(q) - ord('A')].append(idx)

        self.curr_word = []
        self.vec = []
        self.ans = 0
        self.dps()
        return self.ans

    def dps(self):

        l = len(self.curr_word)
        if l >= len(self.target):
            self.ans += 1
            print(self.vec)
            return

        next_w = self.target[l]
        if next_w.islower:
            next_alpha = ord(next_w) - ord('a') + 26
        else:
            next_alpha = ord(next_w) - ord('A')
        
        for next_idx in self.alpa_list[next_alpha]:
            if not self.vec or next_idx > self.vec[-1]:
                self.curr_word.append(next_w)
                self.vec.append(next_idx)
                self.dps()
                self.vec.pop()
                self.curr_word.pop()

if __name__ == "__main__":
    a = Solution()
    # print(a.numDistinct('babgbag', 'bag'))
    # print(a.numDistinct('rabbbit', 'rabbit'))
    print(a.numDistinct('CBAZTAAABBCTA', 'CAT'))
