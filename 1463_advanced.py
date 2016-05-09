f = lambda n, s: s if n == 1 else min(f(n-1, s+1)if n % 3 else f(n/3, s+1) if n % 2 else f(n/2, s+1), 99)
print f(input(), 0)