#include <iostream>
#include <algorithm>

using namespace std;

int solution(int r1, int r2) {
    int answer = 0;

    for (int x = 1; x <= r2; x++) {
        double y2 = floor(sqrt(r2*r2 - x*x));
        double y1 = ceil(sqrt(max(r1*r1 - x*x, 0)));
        answer += (int)y2 - (int)y1 + 1;
    }

    return answer * 4;
}

int main() {
    int answer = solution(2, 3);
    cout << answer << endl;
}
