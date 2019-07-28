#!/usr/bin/env python3
# coding:utf-8
name = input('请输入你的名字:')
print('hello',name,)
shengao = input('请输入你的身高（单位/米）：')
shengao = float(shengao)
tizhong = input('请输入你的体重（单位/Kg）:')
tizhong = float(tizhong)
sg = shengao**2
BMI = tizhong / sg
if BMI <18.5:
    print(name,'你的BMI指数为',BMI,',你太轻了')
elif BMI < 25:
    print(name,'你的BMI指数为',BMI,',你的体重正常')
elif BMI < 28:
    print(name,'你的BMI指数为',BMI,',你有点重啊')
elif BMI <= 32:
    print(name,'你的BMI指数为',BMI,',你太重了')
else:
    print(name,'你的BMI指数为',BMI,',你完了')