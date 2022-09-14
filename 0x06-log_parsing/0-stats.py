#!/usr/bin/python3
'''
Modulus that reads stdin line by line an computes metrics
'''
import sys


if __name__ == '__main__':
    total = 0
    i = 0
    st_code = {}

    def printres(total, st_code):
        '''
        Prints the results of the computed metrics
        '''
        print('File size: {}'.format(total))
        orden = sorted(st_code)
        for o in orden:
            print('{}: {}'.format(o, st_code[o]))

    try:
        for lines in sys.stdin:
            line = lines.split()
            i += 1
            posible = [200, 301, 400, 401, 403, 404, 405, 500]
            try:
                t0 = int(line[-1])
            except Exception:
                t0 = 0
            total += t0
            try:
                t1 = int(line[-2])
                if t1 in posible:
                    if t1 not in st_code:
                        st_code[t1] = 1
                    else:
                        st_code[t1] += 1
            except Exception:
                pass
            if i % 10 == 0:
                printres(total, st_code)
    except KeyboardInterrupt:
        printres(total, st_code)
        raise
    print(total, st_code)
