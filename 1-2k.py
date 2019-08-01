#!/usr/bin/env python3
# coding:utf-8
import math

num1 = float(input('请输入a值:'))
num2 = float(input('请输入b值:'))
num3 = float(input('请输入c值:'))


def fc(a, b, c):
    pd = [a, b, c]
    delta = (b * b - 4 * a * c)
    for pad in pd:
        if not isinstance(pad, (int, float)):
            print('你输入的数据类型有错')
    if delta < 0:
        print('无解')
        return
    else:
        x1 = (0 - b + math.sqrt(delta)) / (2 * a)
        x2 = (0 - b - math.sqrt(delta)) / (2 * a)
        return x1, x2


print(fc(num1, num2, num3))