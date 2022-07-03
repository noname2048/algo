#include <iostream>
#include <vector>
using namespace std;

typedef unsigned long long int64;
int64 mn = 1, mx = 1e12;
vector<int64> square;

int main(int argc, char *argv[]) {
    ios::sync_with_stdio(false);

    cin >> mn >> mx;
    for (int64 i = 2, tmp = i * i; tmp < mx; i++) square.push_back(tmp);

    int64 cnt = 0;
    for (int64 num = mn; num <= mx; num++) {
        bool isDoubleNum = false;
        // 순회하면서 체크하기
        for (int64 idx = 0; idx < square.size() && square[idx] <= num; idx++) {
            int64 tmp = square[idx];
            if (num % tmp == 0) {
                isDoubleNum = true;
                break;
            }
        }
        if (isDoubleNum == false) cnt++;
    }
    cout << cnt << endl;
    return 0;
}
