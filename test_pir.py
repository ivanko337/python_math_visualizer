#!/usr/bin/env python3
#coding=utf-8

import matplotlib.pyplot as plt

slices = [7, 2, 2, 13]
activities = ['sleep', 'eating', 'play', 'work']
color=['c', 'm', 'r', 'b']

plt.pie(slices, labels=activities, colors=color, startangle=90, shadow=True, explode=(0, 0.1, 0, 0), autopct='%1.1f%%')

plt.title('Pie gavno')
plt.show()