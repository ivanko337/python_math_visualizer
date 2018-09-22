#!/usr/bin/env python3
#coding=utf-8

import matplotlib.pyplot as plt

populations_ages = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102, 110, 120, 121, 122, 130, 111, 115, 112, 80, 75, 65, 54, 44, 43, 42, 48]

bins = [i for i in range(0, 140) if i % 10 == 0]

plt.hist(populations_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x gavno')
plt.ylabel('y gavno')
plt.title('test yo')
plt.legend()
plt.show()