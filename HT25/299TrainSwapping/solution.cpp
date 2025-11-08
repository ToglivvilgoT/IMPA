#include <iostream>
#include <array>
#include <vector>

using namespace std;

using It = vector<int>::iterator;

vector<int> getInput(int size) {
    vector<int> lst = {};
    for(int i = size; i; --i) {
        int next;
        cin >> next;
        lst.push_back(next);
    }
    return lst;
}

inline void swap(It first, It second) {
    int temp = *first;
    *first = *second;
    *second = temp;
}

int bubble(It const start, It const last) {
    int swaps = 0;
    for (auto curr = start; curr != last; ++curr) {
        if (*curr > *(curr + 1)) {
            swap(curr, curr + 1);
            ++swaps;
        }
    }
    return swaps;
}

int solve(It const start, It const last) {
    int total = 0;
    while (true) {
        int iter = bubble(start, last);
        if (iter == 0) {
            return total;
        }
        total += iter;
    }
}

int main() {
    int cases;
    cin >> cases;
    for (int i = cases; i; i--) {
        int size;
        cin >> size;
        auto inp = getInput(size);
        if (inp.empty()) {
            cout << "Optimal train swapping takes 0 swaps." << endl;
        } else {
            auto res = solve(inp.begin(), inp.end() - 1);
            cout << "Optimal train swapping takes " << res << " swaps." << endl;
        }
    }
    return 0;
}