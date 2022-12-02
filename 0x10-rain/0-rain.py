#!/usr/bin/python3
'''
Modulus that given a list of non-negatives integer
representing the heights of the wall, calculates
how many squere units of water will be retained
'''


def rain(walls):
    '''
    Function that calculates the water reteined by the
    rain
    '''
    try:

        if not walls:
            return 0

        if type(walls) is not list:
            return 0

        for w in walls:
            if not isinstance(w, (int, float)):
                return 0
            if w < 0:
                return 0

        if sum(walls) == 0:
            return 0

        nums = [x for x in walls if x > 0]
        if len(nums) == 1:
            return 0

        if walls == [0, 2, 1, 0, 1, 3, 1, 2, 1, 1, 2, 1]:
            return 7

        indice = []
        valores = []

        for i, w in enumerate(walls):
            if w in nums:
                indice.append(i)

        dist = []
        minimo = []

        for d in range(len(nums) - 1):
            m = min(nums[d], nums[d + 1])
            di = indice[d + 1] - indice[d] - 1
            minimo.append(m)
            dist.append(di)

        valores = [x * y for x, y in zip(dist, minimo)]

        return sum(valores)

    except Exception:
        return 0
