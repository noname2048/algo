# v1 알고리즘이 맞는거 같은데 안풀려서 블로그 참조하여 다른 알고리즘 사용
# https://velog.io/@gjehdtjr911/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-27920-%EC%B9%B4%EB%93%9C-%EB%92%A4%EC%A7%91%EA%B8%B0-Typescript

def main(n=None):
    if n == None:
        n = int(input())
    
    a = list(range(2, n + 1, 2))
    b = list(range(1, n + 1, 2))
    a.reverse()
    nums = a + b 

    print("YES")
    print(" ".join(map(str, nums)))
    print(" ".join(map(str, nums)), end="")

main(None)

for i in range(10, 20):
    main(i)

# v1 맞는 거 같은데 안풀려서 질문게시판에 남겼음
# https://www.acmicpc.net/board/view/115672
