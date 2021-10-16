// #include <cstdio>
#include <iostream>

using namespace std;

int arrA[101] = {
    0,
};
int arrB[101] = {
    0,
};
int n;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    // freopen("input1.txt", "r", stdin);

    cin >> n;
    int a, b;
    for (int i = 0; i < n; i++) {
        cin >> a >> b;

        arrA[a] += 1;
        arrB[b] += 1;

        int g_max = 0;
        int x = 1, y = 100;
        int xCnt = 0, yCnt = 0;

        for (int j = 0; j < i + 1; j++) {
            if (xCnt == arrA[x]) {
                xCnt = 0;
                x += 1;
            }
            while (arrA[x] == 0) {
                x += 1;
            }
            if (yCnt == arrB[y]) {
                yCnt = 0;
                y -= 1;
            }
            while (arrB[y] == 0) {
                y -= 1;
            }
            xCnt += 1;
            yCnt += 1;

            g_max = (g_max > x + y ? g_max : x + y);
        }
        cout << g_max << "\n";
    }
    return 0;
}