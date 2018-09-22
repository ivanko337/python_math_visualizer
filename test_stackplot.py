#!/usr/bin/env python3
#coding=utf-8

import matplotlib.pyplot as plt

days = [i for i in range(1, 6)]

sleepeng = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 3, 2, 3]
playing = [8, 5, 7, 8, 13]

plt.plot([], [], color='m', label='sleepeng', linewidth=5)
plt.plot([], [], color='c', label='eating', linewidth=5)
plt.plot([], [], color='r', label='working', linewidth=5)
plt.plot([], [], color='k', label='playing', linewidth=5)

plt.stackplot(days, sleepeng, eating, working, playing, colors=['m', 'c', 'r', 'k'])

plt.xlabel('x gavno')
plt.ylabel('y gavno')
plt.title('test yo')

plt.legend()
plt.show()