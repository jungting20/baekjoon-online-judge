# -*- coding: utf-8 -*-
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

for i in range(int(raw_input())):
    a, b = map(int, raw_input().split())
    while a != 1:
        # 1 / x ≤ a / b
        # 1 ≤ ax / b
        # b ≤ ax
        # b / a ≤ x
        x = b/a
        if b % a != 0:
            x += 1
        # a / b = a / b - 1 / x
        # a / b = (ax - b) / bx
        a = a*x-b
        b = b*x
        # a, b를 서로소로 만들어 주기 위하여
        a /= gcd(a, b)
        b /= gcd(a, b)
    print b