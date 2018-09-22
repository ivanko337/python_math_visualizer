#!/usr/bin/env python3
#coding=utf-8

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [5, 8, 10]
y = [12, 16, 6]

x2 = [6, 9, 11]
y2 = [6, 15, 7]

plt.bar(x, y, label='First Line', linewidth=3) # plot
plt.bar(x2, y2, label='Second Line', linewidth=3) # plot
plt.legend()

plt.title('gavno2')
plt.ylabel('y-gavno')
plt.xlabel('x-gavno')

plt.show()