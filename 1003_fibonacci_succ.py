def fibo(n,a,b):
    return a if n==0 else fibo(n-1,b,a+b)

n=int(raw_input())
for i in range(n):
    n2= int(raw_input())
    try:
        zero=fibo(n2,1,0)
        one=fibo(n2,0,1)
        print "%d %d" %(zero, one)
    except RuntimeError:
        print "1 0"