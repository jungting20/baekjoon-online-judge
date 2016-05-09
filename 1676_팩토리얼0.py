# -*- coding: utf-8 -*-
n = int(raw_input())
a = 0 # 5의 지수
for i in range(5, n+1):
    x = i
    while x % 5 == 0:
        x /= 5
        a += 1
print a