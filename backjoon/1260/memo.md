## 쉬운데 틀렸던 이유

-   그저 v를 맨처음에 path 에 넣어주지 않아서 생긴 일이였음 (문제를 잘 읽자)

## 하다보니 조금... 그래..

-   visited 가 dict 의 형태를 띄는것이 빠르다
-   dfs와 bfs의 구조를 완전히 이해하면 순서 조정을 통해 최소한의 if 만 넣을 수 있다. (10ms 단축 가능)
-   deque 의 import 속도 보다 그냥 list를 쓰는게 빠르다. (어우...) (약 20ms 단축 가능)
-   입력값이 많으면 많을 수록 input() 보다 sys.stdin.readline() 이 훨씬 빠르다 (500ms -> 100ms)

## 과정

-   start (600ms)
-   imporve (120ms)
-   -   여기서 visited가 list로 바뀜
-   -   deque 계속 해서 사용
-   -   sys.stdin.readline 사용
-   more-improve (90ms)
-   -   dict 로 돌아옴
-   -   deque 대신 list 사용
-   -   dfs, bfs 구조 파악
-   -   -   dfs 는 거꾸로된 스택을 그냥 뒤에다 통짜로 추가하고, pop 한뒤 방문여부 체크
-   -   -   bfs 는 방문여부 체크는 추가할때만 한다(어짜피 먼저 방문한다)
-   -   -   요약: dfs는 추가하고 나중에 방문할때 확인, bfs는 추가할때 확인 (그외는 확인이 필요하지 않다.)
