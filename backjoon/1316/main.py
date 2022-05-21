
def solution(word):

    used_set = set()

    idx = 0
    l = len(word)
    while(idx < l):
        
        alpha_idx = ord(word[idx])
        if alpha_idx in used_set:
            return 0
        else:
            while(idx + 1 < l and word[idx] == word[idx + 1]):
                idx += 1
            used_set.add(alpha_idx)
            idx += 1

    return 1


if __name__ == "__main__":
   
    # word_list = []
    # for _ in range(int(input())):
    #     word_list.append(input())

    word_list = [
        'happy',
        'new',
        'year',
        'aba',
        'abab',
        'abcabc'
    ]

    ans = 0
    for word in word_list:
        ans += solution(word)

    print(ans)
