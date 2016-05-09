# -*- coding: utf-8 -*-

n = map(str, raw_input().split())
x = n[0]
y = n[1]
x = x[::-1].lstrip('0')
y = y[::-1].lstrip('0')
# 이렇게 reversed() 함수를 사용하는 방법도 있음
# s = ''.join(reversed(s))

print str(int(x)+int(y))[::-1].lstrip('0')