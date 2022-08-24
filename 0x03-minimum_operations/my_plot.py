#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(1, 20, 20)

y = [0, ]
ops = [0, ]
op = 0
n = 1

for x in X:
    n += n
    op += 2
    y.append(n)
    ops.append(op)

plt.plot(ops, y)
plt.xlabel('Operaciones')
plt.ylabel('Hs duplicando')
plt.ylim(0, 1050000)
plt.show()

print(ops)
print(y)