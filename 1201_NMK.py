import math
n, m, k = map(int, raw_input().split())
a = []
g = []
if m+k-1 <= n <= m*k:
    for i in range(n):
        a.append(i+1)
    g.append(0)
    g.append(k)
    n -= k
    m -= 1
    if m == 0:
        gs = 1
        r = 0
    else:
        gs = n / m
        r = n % m

    if r > 0:
        s = 1
    else:
        s = 0

    for i in range(m):
        g.append(g[-1] + gs + s)
        if r > 0:
            r -= 1
    for i in range(len(g)-1):
        reverse(a[0] + g[i], a[0] + g[i+1])
    for i in range(len(a)):
        print a[i],

else:
    print('-1')
