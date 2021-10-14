#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
#include <sstream>
#include <cstdlib>
#include <limits>

using namespace std;

int n, e;
int a, b, c;
vector<int> vertexValue;
vector<vector<pair<int, int>>> dEdge;
vector<int> dpCache;

int global_max_cost;
vector<int> global_path;

int dfs(int here, int cost, vector<int> &path) {
    if (dpCache[here] == numeric_limits<int>::max() || dpCache[here] < cost) {
        dpCache[here] = cost;

        if (global_max_cost < cost) {
            global_max_cost = cost;
            global_path = path;
        }

        for (int i = 0; i < dEdge[here].size(); i++) {
            int next = dEdge[here][i].first;
            int newCost = cost + vertexValue[next] - dEdge[here][i].second;
            path.push_back(next);
            dfs(next, newCost, path);
            path.pop_back();
        }
        return dpCache[here];
    }
    else {
        return dpCache[here];
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    freopen("input1.txt", "r", stdin);

    int testCase;
    cin >> testCase;
    for (int i = 0; i < testCase; i++) {
        cin >> n >> e;

        // vertexValue 할당하기
        vertexValue = vector<int> (n + 2);
        dpCache = vector<int> (n + 2, numeric_limits<int>::max());

        string temp;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        getline(cin, temp);
        stringstream ss(temp);
        for (int j = 0; j < n - 1; j++) {
            getline(ss, temp, ' ');
            vertexValue[j + 1] = atoi(temp.c_str());
        }
        getline(ss, temp);
        vertexValue[n] = atoi(temp.c_str());

        // dEdge 할당하기
        dEdge = vector<vector<pair<int, int>>> (e + 2, vector<pair<int, int>> ());
        for (int j = 0; j < e; j++) {
            cin >> a >> b >> c;
            dEdge[a].push_back(make_pair(b, c));
        }

        // 각종 초기화
        global_max_cost = 0;
        global_path = vector<int> ();
        vector<int> initPath = vector<int>(1, 1);
        int value = dfs(1, vertexValue[1], initPath);
        cout << global_max_cost << " " << global_path.size() << "\n";
        
        int t = global_path.size() - 1;
        for (int j = 0; j < t; j++) {
            cout << global_path[j] << " ";
        }
        cout << global_path[global_path.size() - 1] << "\n";
    }

    return 0;
}