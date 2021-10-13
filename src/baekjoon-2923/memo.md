## 과정

1. start.py
    - 가설오류, 숫자 두개만 비교해서 될 것이라고 생각했음
1. just_sort.py
    - bf. 시간초과
1. idea.py
    - 해설을 보고 난뒤 배열 `int arrA[100]`을 이용해서 풀어보려함
1. improve_idea.py
    - idea를 링크드 리스트로 구현하여 for을 줄이려 노력. 여전히 시간초과
1. why-not.cpp
    - python이 안되길래 cpp 로 idea를 구현. 시간초과.

여기까지 보면 다른 방법이 있는거 같은데...

1. why-not-improve.cpp (92ms)
    - 다른사람 해설보고 어렴풋이 중복에 대한 처리도 중요하다고 깨달음
1. return_to_python.py (776ms)
    - why-not-inprove를 보고 python으로 옮겨옴. pypy3만 되고 python은 안됨

언어간 차이가 정말 많이 난다.
