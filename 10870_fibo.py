def fibo(n, a, b):
    return a if n == 0 else fibo(n-1, b, a+b)

n = int(raw_input())
zero = fibo(n, 0, 1)
print "%d" % zero