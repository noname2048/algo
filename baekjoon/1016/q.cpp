#include <iostream>
#include <vector>
using namespace std;

int mn, mx;
vector<long long> doubles;

int main(int argc, char *argv[]) {
    ios::sync_with_stdio(false);
    // cout.tie(NULL);
    cin.tie(NULL);

    cin >> mn >> mx;
    for (long long i = 2; i * i <= mx; i++) {
        doubles.push_back(i * i);
    }
    int cnt = 0;
    for (long long num = mn; num <= mx; num++) {
        bool isDoubleNum = false;
        for (long long double_idx = 0; doubles[double_idx] <= num && double_idx < doubles.size(); double_idx++) {
            int target = doubles[double_idx];
            if (num % target == 0) {
                isDoubleNum = true;
                break;
            }
        }
        if (isDoubleNum == false) cnt++;
    }
    cout << cnt << endl;
    return 0;
}
