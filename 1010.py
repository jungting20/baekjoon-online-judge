from math import factorial
T = int(raw_input())

for i in range(T):
    N, M = [int(x) for x in raw_input().split()]
    mcn = int(factorial(M)/(factorial(N)*factorial(M-N)))
    print (mcn)