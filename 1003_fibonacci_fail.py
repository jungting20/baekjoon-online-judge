# -*- coding: utf-8 -*-

N = map(int, raw_input())
A = [map(int, raw_input()) for i in range(N[0])]

#0이 몇 번 출력되는지
def fibonacci_0(n):
    if n==0:
        return 1
    elif n==1:
        return 0
    else:
        return fibonacci_0(n-1)+fibonacci_0(n-2)

# 1이 몇 번 출력되는지
def fibonacci_1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_1(n - 1) + fibonacci_1(n - 2)


for j in range(N[0]):
    num = 0
    for i in range(1,len(A[j])+1):
        num += pow(10,len(A[j])-i)*A[j][i-1]
    print fibonacci_0(num), fibonacci_1(num)

