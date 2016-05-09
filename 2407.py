# -*- coding:utf-8 -*-

n, m = [int(x) for x in raw_input().split()];

def findPrime(n):   # 소수찾기 함수
    for num in range(2, int(n)):
        isPrime = True
        for prime in primeNum:
            if (num % prime == 0):
                isPrime = False
                break
        if isPrime:
            primeNum.append(num)
    return primeNum

def intFactorization(n, factor):    # 소인수분해 함수
    for i in range(len(primeNum)):
        while (n % primeNum[i] == 0):
            factor[i] += 1
            n = n/primeNum[i]

primeNum = []
primeNum = findPrime(100)

factor_N = [0 for i in range(len(primeNum))]
factor_M = [0 for i in range(len(primeNum))]
factor_NM = [0 for i in range(len(primeNum))]

result = 1

for i in range(n, 1, -1):
    intFactorization(i, factor_N)
for i in range(m, 1, -1):
    intFactorization(i, factor_M)
for i in range(n-m, 1, -1):
    intFactorization(i, factor_NM)

for i in range(len(primeNum)):
    factor = factor_N[i] - factor_M[i] - factor_NM[i]
    result *= primeNum[i]**factor

print (result)