# -*-coding: utf-8 -*-
n, m = map(int, raw_input().split())
l = map(int, raw_input().split())
s = [0]
x = 0
for i in xrange(n):
    x += l[i]
    s.append(x)


# t = [0]*m 이것이 시간이 더 걸리는 신기한...
t = []
for i in xrange(m):
    t.append(0)
for i in xrange(n+1):
    a = s[i] % m
    t[a] += 1

ans = 0
for i in xrange(m):
    ans += t[i]*(t[i]-1)/2
print ans