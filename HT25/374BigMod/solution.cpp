#include <iostream>

using namespace std;

int solve(long long b, const long long p, const long long m) {
    b %= m;

    if (p == 0) {
        return 1;
    }
    else if (p % 2 == 1) {
        return (b * solve(b, p - 1, m)) % m;
    }
    else {
        long long result = solve(b, p / 2, m);
        result *= result;
        return result % m;
    }
}

int main() {
    long long b, p, m;
    while (cin >> b >> p >> m) {
        cout << solve(b, p, m) << endl;
    }

    return 0;
}