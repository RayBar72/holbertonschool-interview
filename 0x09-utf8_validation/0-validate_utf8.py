#!/usr/bin/python3
'''
Modulus that has function  that determines if a given data set represents
a valid UTF-8 encoding
'''


def validUTF8(data):
    '''
    Function that determines if a given data set represents a valid UTF-8
    '''
    if type(data) is not list:
        return False
    if data == []:
        return False
    for i in data:
        if type(i) is not int:
            return False
        if i < 0:
            return False
        if i > 256:
            return False
        if i == None:
            return False
        if i == False:
            return False

    data = [str(bin(x)).split('b')[1] for x in data]

    for i in range(len(data)):
        if len(data[i]) < 8:
            data[i] = ('0' * (8 - len(data[i]))) + data[i]
        elif len(data[i]) > 8:
            return False

    for i in range(len(data)):
        if data[i][:5] == '11110':
            try:
                if not (data[i + 1] or data[i + 2] or data[i + 3]):
                    return False
                if data[i + 1] != data[i + 2] != data[i + 3] != '10':
                    return False
            except Exception:
                return False

        elif data[i][:4] == '1110':
            try:
                if not (data[i + 1] or data[i + 2]):
                    return False
                if data[i + 1] != data[i + 2] != '10':
                    return False
            except Exception:
                return False

        elif data[i][:3] == '110':
            try:
                if not (data[i + 1]):
                    return False
                if data[i + 1] != '10':
                    return False
            except Exception:
                return False

        elif data[i][0] == '1':
            return False

    return True
