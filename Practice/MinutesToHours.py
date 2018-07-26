import sys


def MinutesToHours(minutes):
    "calculation minutes to hours"
    result = divmod(int(minutes), 60)
    return result[0], result[1]


def main(minutes):
    "print result"
    a, b = MinutesToHours(minutes)
    print('{} H, {} M'.format(a, b))


if __name__ == '__main__':
    if int(sys.argv[1]) < 0:
        try:
            raise ValueError('A value error happened.')
        except ValueError:
            print('ValueError: Input number cannot be negative')
    else:
        main(sys.argv[1])
