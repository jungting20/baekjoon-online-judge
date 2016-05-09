# -*- coding: utf-8 -*-
a, b, v = map(int, raw_input().split())
l = 0   # 올라간 거리
cnt = 0     # 올라가는데 걸린 시간
while True:
    l += a
    cnt += 1
    if l >= v:
        break
    l -= b
print cnt