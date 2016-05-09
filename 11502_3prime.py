from __future__ import print_function

primes = []
for i in range(2, 1001):
    sw = 0
    for j in range(2, i):
        if i % j == 0:
            sw = 1
    if sw:
        continue
    primes.append(i)
print(primes)
ans = []
for i in range(1000):
    ans.append([0, 0, 0])

for a in primes:
    for b in primes:
        if b < a:
            continue
        for c in primes:
            if c < b:
                continue
            if a + b + c < 1001:
                ans[a + b + c - 1] = [a, b, c]

for i in range(int(raw_input())):
    n = int(raw_input())
    print(ans[n-1][0], end=" ")
    print(ans[n-1][1], end=" ")
    print(ans[n-1][2], end=" ")