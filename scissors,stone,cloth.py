#!/usr/bin/env python3
# coding:utf-8
import random
a = int(input('请输入你的出拳结果,1为剪刀，2为石头，3为布:'))
b = random.randint(1,3)
if (a==1 and b==3) or (a==2 and b==1) or (a==3 and b==1):
    print('恭喜，你赢了。')
elif a==b:
    print('你与电脑打了平局')
else:
    print('电脑战胜了你')