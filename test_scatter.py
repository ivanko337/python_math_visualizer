#!/usr/bin/env python3
#coding=utf-8

import matplotlib.pyplot as plt
from random import randint

x = [i for i in range(1, 9)]
y = [randint(0, 10 * i) for i in range(0, 8)]

plt.scatter(x, y, label='test', color='k', s=25, marker="o")

plt.xlabel('x gavno')
plt.ylabel('y gavno')
plt.title('test yo')

plt.legend()
plt.show()