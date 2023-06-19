//
// Created on 2023/06/19.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(const vector<int>& a, const vector<int>& b) {
    return a[1] < b[1];
}

int solution(vector<vector<int>> targets) {
    int answer = 0;
    sort(targets.begin(), targets.end(), cmp);

    int t = -1;
    for (auto& target: targets) {
        if (t <= target[0]){
            t = target[1];
            answer++;
        }
    }

    return answer;
}

int main() {
    vector<vector<int>> targets {
        {4,5},{4,8},{10,14},{11,13},{5,12},{3,7},{1,4}
    };
    cout << solution(targets) << endlt a;
    return 0;
}
