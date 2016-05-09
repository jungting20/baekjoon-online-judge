# -*- coding:utf-8 -*-
a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
r = raw_input()
d = {i: r.count(i) for i in a}
c = 0   # 홀수개수가 있는 알파벳이 몇 개인가
b = ''
s = ''  # 홀수개수가 있는 알파벳의 정체
for i in a:
    if d[i] % 2:
        c += 1
        s = i
for i in a:
    b += i * (d[i] // 2)
if c < 2:
    print(b+s+b[::-1])
else:
    print("I'm Sorry Hansoo")