# -*- coding: utf-8 -*-
import math
n=int(raw_input())
list = [map(int, raw_input().split()) for i in range(n)]
for i in range(n):
    a = float("%.11f" % (list[i][0] ** (1.0/3.0)))
    b = int((a * (10.0 ** 11)) / 10)
    print "%.10f" % (b/(10.0 ** 10))
    # print "%.10f" % (int((float("%.11f" % (list[i][0] ** (1.0/3.0))) * (10.0 ** 11)) / 10)/(10.0 ** 10))

# 1234567890 이 15번 반복된 150자리에 대해 에러가 발생한다.
'''
Traceback (most recent call last):
  File "C:/Users/user/PycharmProjects/baekjoon_prob/3783_��������_fail.py", line 3, in <module>
    list = [map(int, raw_input().split()) for i in range(n)]
OverflowError: range() result has too many items
에러가 발생한다.
'''

