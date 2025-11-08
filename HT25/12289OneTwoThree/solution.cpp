#include <iostream>
#include <array>

using namespace std;

bool matching(string w1, string w2) {
    if (w1.size() != w2.size()) return false;

    size_t misses = 0;

    for (size_t i = 0; i < w1.size(); i++) {
        misses += w1[i] != w2[i];
    }

    return misses < 2;
}

void printMatching(string word) {
    const array<string, 3> numbers = {"one", "two", "three"};

    for (int i : {0, 1, 2}) {
        if (matching(word, numbers[i])) {
            cout << i + 1 << endl;
            return;
        }
    }
}

int main() {
    int cases;
    for(cin >> cases; cases > 0; cases--) {
        string word;
        cin >> word;
        printMatching(word);
    }

    return 0;
}