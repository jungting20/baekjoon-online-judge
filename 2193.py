def fibo(n,a,b):
    return a if n==0 else fibo(n-1,b,a+b)

n=int(raw_input())
try:
    print "%d" %fibo(n,0,1)
except RuntimeError:
    print "0"