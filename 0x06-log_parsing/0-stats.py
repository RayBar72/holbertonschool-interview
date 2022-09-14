#!/usr/bin/python3
'''
Modulus that reads stdin lines by lines an computes metrics
'''
import sys


if __name__ == "__main__":
    total = [0]
    st_code = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    def check_match(lines):
        '''Checks for regexp match in lines.'''
        try:
            lines = lines[:-1]
            line = lines.split(" ")
            total[0] += int(line[-1])
            code = int(line[-2])
            if code in st_code:
                st_code[code] += 1
        except Exception:
            pass

    def print_stats():
        '''Prints accumulated statistics.'''
        print("File total: {}".format(total[0]))
        for k in sorted(st_code.keys()):
            if st_code[k]:
                print("{}: {}".format(k, st_code[k]))
    i = 1
    try:
        for lines in sys.stdin:
            check_match(lines)
            if i % 10 == 0:
                print_stats()
            i += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
