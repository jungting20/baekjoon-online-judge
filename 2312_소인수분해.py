# -*- coding: utf-8 -*-
def getprime(val):
    for x in range(2, val+1):
        exponent = 0    # 인수가 곱해진 횟수
        while val % x == 0:
            exponent += 1
            val /= x
        if exponent != 0:
            print ("%d %d" % (x, exponent))

T = int(raw_input())

for i in range(T):
    N = int(raw_input())
    getprime(N)