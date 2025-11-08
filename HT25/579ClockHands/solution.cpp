#include <iostream>

using namespace std;

int main() {
    while(true) {
        int hour;
        int minute;
        cin >> hour;
        cin.ignore();
        cin >> minute;
        if (hour == 0 && minute == 0) {
            break;
        }
        int minuteDegres = minute * 60;
        int hourDegres = hour * 5 * 60 + minute * 5;

        int angle = minuteDegres - hourDegres;
        if (angle < -1800) {
            angle += 3600;
        } else if (angle < 0) {
            angle *= -1;
        } else if (angle > 1800) {
            angle = 3600 - angle;
        }
        printf("%.3F\n", (float)angle / 10);
    }
    return 0;
}