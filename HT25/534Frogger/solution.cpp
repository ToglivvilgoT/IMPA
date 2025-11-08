#include <iostream>
#include <queue>
#include <vector>
#include <set>
#include <cmath>

#define Stone pair<int, int>

using namespace std;

double getDist(Stone* a, Stone* b) {
    int x1 = a->first;
    int x2 = b->first;
    int y1 = a->second;
    int y2 = b->second;

    double dx = abs(x1 - x2);
    double dy = abs(y1 - y2);

    return sqrt(dx * dx + dy * dy);
}

double solve(Stone* stones, int stonesLen) {
    Stone* target = stones + 1;
    priority_queue<pair<double, Stone*>, vector<pair<double, Stone*>>, greater<pair<double, Stone*>>> queue;
    set<Stone*> visited;
    queue.push({0, stones});

    while (!queue.empty()) {
        pair<double, Stone*> p = queue.top();
        double dist = p.first;
        Stone* curr = p.second;
        queue.pop();
        if (visited.count(curr)) {
            continue;
        }
        visited.insert(curr);
        if (curr == target) {
            return dist;
        }

        Stone* end = stones + stonesLen;
        for(Stone* next = stones; next != end; next++) {
            if (visited.count(next)) {
                continue;
            }
            double nextDist = getDist(curr, next);
            nextDist = max(nextDist, dist);
            queue.push({nextDist, next});
        }
    }
}

int main() {
    for (int i = 1; true; i++) {
        int stonesLen;
        cin >> stonesLen;
        if (!stonesLen) {
            break;
        }

        pair<int, int>* stones = new pair<int, int>[stonesLen];

        for (int i = 0; i < stonesLen; i++) {
            pair<int, int>& stone = stones[i];
            cin >> stone.first >> stone.second;
        }

        double result = solve(stones, stonesLen);

        cout << "Scenario #" << i << endl << "Frog Distance = ";
        printf("%.3f", result);
        cout << endl << endl;

        delete[] stones;
    }
    
    return 0;
}