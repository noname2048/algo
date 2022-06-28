#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <map>
#include <set>
using namespace std;

int testcase;
int n, k;
int duration[1001];
int cache[1001];
map<int, set<int>> m;

int recursion(int idx) {
    if (cache[idx] > 0) return cache[idx];

    if (m.find(idx) == m.end()) {
        cache[idx] = duration[idx];
        return cache[idx];
    }

    set<int> &tmp = m[idx];
    set<int>::iterator it;
    int mx = -1;
    for (it = tmp.begin(); it != tmp.end(); it++) {
        int parent = *it;
        int local = recursion(parent);
        if (mx < local) mx = local;
    }
    cache[idx] = mx + duration[idx];
    return cache[idx];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("data.txt", "r", stdin);

    cin >> testcase; 
    for (int i = 0; i < testcase; i++) {
        fill_n(cache, 10001, -1);
        m.clear();
        cin >> n >> k;
        for (int j = 0; j < n; j++) {
            cin >> duration[j + 1];
        }
        for (int x = 0; x < k; x++) {
            int parent, child;
            cin >> parent >> child;
            if (m.find(child) != m.end()) {
                map<int, set<int>>::iterator it = m.find(child);
                set<int> &tmp = it->second;
                tmp.insert(parent);
            }
            else {
                set<int> tmp;
                tmp.insert(parent);
                m[child] = tmp;
            }
        }
        int w;
        cin >> w;
        int ret = recursion(w);
        cout << ret << endl;
    }
    return 0;
}