#!/usr/bin/python3
'''
Modulus that has function  that determines if a given data set represents
a valid UTF-8 encoding
'''


def validUTF8(data):
    '''
    Function that determines if a given data set represents a valid UTF-8
    '''
    b = 0
    for n in data:
        byte = n & 0xFF
        if b:
            if byte >> 6 != 2:
                return False
            b -= 1
            continue
        while (1 << abs(7 - b)) & byte:
            b += 1
        if b == 1 or b > 4:
            return False
        b = max(b - 1, 0)
    return b == 0
