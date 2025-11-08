#include <iostream>
#include <array>
#include <iterator> 

using namespace std;

template<typename aIt, typename bIt>
int solve(aIt aBegin, aIt aEnd, bIt bBegin, bIt bEnd, int carryIn = 0) {
    if (aBegin == aEnd && bBegin == bEnd) {
        return 0;
    } else if (aBegin == aEnd) {
        int val = *bBegin - '0';
        int carry = val + carryIn >= 10;
        return carry + solve(aBegin, aEnd, bBegin + 1, bEnd, carry);
    } else if (bBegin == bEnd) {
        int val = *aBegin - '0';
        int carry = val + carryIn >= 10;
        return carry + solve(aBegin + 1, aEnd, bBegin, bEnd, carry);
    }

    int a = *aBegin - '0';
    int b = *bBegin - '0';
    int carry = a + b + carryIn >= 10;

    return carry + solve(aBegin + 1, aEnd, bBegin + 1, bEnd, carry);
}

int main() {
    string a;
    string b;

    while (cin >> a >> b && !(a == "0" && b == "0")) {
        int carries = solve(a.rbegin(), a.rend(), b.rbegin(), b.rend());
        if (carries == 0) {
            cout << "No carry operation." << endl;
        } else if (carries == 1) {
            cout << "1 carry operation." << endl;
        } else {
            cout << carries << " carry operations." << endl;
        }
    }

    return 0;
}