#include <iostream>

using namespace std;

double getAverage(int* grades, int students) {
    int total = 0;
    int* end = grades + students;
    for (; grades != end; grades++) {
        total += *grades;
    }
    return (double)total / (double)students;
}

int getAboveAverage(int* grades, int students, double average) {
    int aboveAverage = 0;
    int* end = grades + students;
    for (; grades != end; grades++) {
        if (*grades > average) {
            aboveAverage++;
        }
    }
    return aboveAverage;
}

void solve(int* grades, int students) {
    double average = getAverage(grades, students);
    int aboveAverage = getAboveAverage(grades, students, average);
    double abovePercent = (double)100 * (double)aboveAverage / (double)students;

    std::printf("%.3f", abovePercent);
    cout << "%" << endl;
}

int main() {
    int cases;
    for (cin >> cases; cases > 0; cases--) {
        int students;
        cin >> students;
        int* grades = new int[students];
        int* end = grades + students;
        for (int* curr = grades; curr != end; curr++) {
            cin >> *curr;
        }
        solve(grades, students);
        delete grades;
    }
    return 0;
}