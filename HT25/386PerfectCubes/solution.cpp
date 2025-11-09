#include <iostream>
#include <array>
#include <vector>
#include <tuple>
#include <algorithm>
#include <iterator>

using namespace std;

struct Cube {
    int a;
    int b;
    int c;
    int d;

    Cube(int a, int b, int c, int d) {
        this->a = a;
        this->b = b;
        this->c = c;
        this->d = d;
    }

    tuple<int, int, int, int> asTuple() const {
        return make_tuple(this->a, this->b, this->c, this->d);
    }

    bool operator < (Cube const& other) const {
        return this->asTuple() < other.asTuple();
    } 
};

ostream& operator << (ostream& stream, const Cube& cube) {
    return stream << "Cube = " << cube.a << ", Triple = (" << cube.b << "," << cube.c << "," << cube.d << ")";
}

vector<Cube> solve() {
    vector<Cube> cubes;
    for (int a = 2; a <= 200; ++a) {
        int target = a * a * a;
        for (int b = 2; b <= 200; ++b) {
            int secondTarget = target - b * b * b;
            if (secondTarget < 0) { break; }
            for (int c = b; c <= 200; ++c) {
                int thirdTarget = secondTarget - c * c * c;
                if (thirdTarget < 0) { break; }
                for (int d = c; d <= 200; ++d) {
                    int finalTarget = thirdTarget - d * d * d;
                    if (finalTarget > 0) {
                        continue;
                    } else if (finalTarget == 0) {
                        cubes.push_back(Cube(a, b, c, d));
                    }
                    break;
                }
            }
        }
    }
    return cubes;
}

int main() {
    auto result = solve();
    copy(result.begin(), result.end(), ostream_iterator<Cube>(cout, "\n"));
    cout << flush;
}