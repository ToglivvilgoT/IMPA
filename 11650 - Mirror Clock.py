

def mirror_minute(minute: int):
    minute = 60 - minute

    if minute == 60:
        minute = 0

    return minute


def mirror_hour(hour: int, mirrored_minute: int):
    hour = 12 - hour

    if mirrored_minute != 0:
        hour -= 1

    hour %= 12

    if hour == 0:
        hour = 12

    return hour


def get_number_formated(n: int):
    if n < 10:
        return '0' + str(n)
    else:
        return str(n)


def solve(hour: int, minute: int):
    minute = mirror_minute(minute)
    hour = mirror_hour(hour, minute)

    print(get_number_formated(hour) + ':' + get_number_formated(minute))


def get_input():
    hour, minute = map(lambda x: int(x), input().split(':'))

    return (hour, minute)


if __name__ == '__main__':
    test_cases = int(input())

    for test_case in range(test_cases):
        solve(*get_input())