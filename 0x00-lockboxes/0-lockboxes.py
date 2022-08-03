#!/usr/bin/python3
'''Method that determines if all the boxes can be opened'''


def canUnlockAll(boxes):
    '''Returns True if all boxes can be unlocked'''
    if type(boxes) is not list:
        return False
    if len(boxes) == 0:
        return False
    for i in range(1, len(boxes) - 1):
        c = False
        for j in range(len(boxes)):
            c = i in boxes[j] and i != j
            if c:
                break
        if c is False:
            return False
    return True
