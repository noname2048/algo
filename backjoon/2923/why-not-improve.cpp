#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    freopen("input1.txt", "r", stdin);
    ios_base::sync_with_stdio(NULL);
    cin.tie(NULL);

    int n;
    int arrA[101] =
        {
            0,
        },
        arrB[101] = {
            0,
        };

    cin >> n;
    int a, b;
    for (int i = 0; i < n; i++) {
        cin >> a >> b;
        arrA[a]++;
        arrB[b]++;

        // 복사
        vector<int> vectorA(101), vectorB(101);
        for (int j = 0; j < 101; j++) {
            vectorA[j] = arrA[j];
            vectorB[j] = arrB[j];
        }

        int localAnswer = 0;
        int ai = 100, bi = 1;  // index
        while (ai > 0 && bi < 101) {
            while (ai > 0 && vectorA[ai] == 0) ai--;
            while (bi < 101 && vectorB[bi] == 0) bi++;
            // 이후 로직을 진행하기 전 안전 종료
            if (ai < 1 || bi > 100) break;
            // 최댓값 업데이트
            localAnswer = max(localAnswer, ai + bi);
            // 중복된 숫자의 빠른 제거
            if (vectorA[ai] > vectorB[bi]) {
                vectorA[ai] = vectorA[ai] - vectorB[bi];
                vectorB[bi] = 0;
            } else {
                vectorB[bi] = vectorB[bi] - vectorA[ai];
                vectorA[ai] = 0;
            }
        }
        cout << localAnswer << "\n";
    }
}