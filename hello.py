#!/usr/bin/env python3
# coding:utf-8
name = input('请输入你的姓名:')
print('你好,',name,)
s1 = float(input('请输入你上一次的成绩:'))
s2 = float(input('请你输入这一次的成绩:'))
r = 100 * (s2-s1) / s1
print('你好,',name,'你本次成绩提升了' '%.1f' % r,'%!')