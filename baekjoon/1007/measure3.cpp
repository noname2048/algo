#include <chrono>
#include <iostream>
using namespace std;

int getSum(int number = 500000000) {
    int t = 0;
    for (int i = 0; i < number; i++) {
        t++;
    }
    return t;
}

int main(int argc, char *argv[]) {
    auto start = chrono::high_resolution_clock::now();
    int t = 0;
    for (int i = 0; i < 10; i++) {
        t = getSum();
    }
    auto finish = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::microseconds>(finish - start);
    double result = duration.count() / 1e6;

    cout.precision(6);
    cout << result << " 구아아" << endl;
    return 0;
}

// styles with vscode
// https://zamhuang.medium.com/vscode-how-to-customize-c-s-coding-style-in-vscode-ad16d87e93bf
