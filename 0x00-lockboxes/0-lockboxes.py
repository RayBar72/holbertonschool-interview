#!/usr/bin/env python3
'''Method that determines if all the boxes can be opened'''


def canUnlockAll(boxes):
    '''Returns True if all boxes can be unlocked'''
    for i in range(len(boxes) - 1):
        c = i + 1
        if c in boxes[i]:
            pass
            # print('c es {}'.format(c))
        else:
            # print('c es {}'.format(c))
            return False
    return True
