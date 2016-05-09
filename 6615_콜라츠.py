def coll(x):
    

while True:
    n, m = map(int, raw_input().split())
    if n==0 and m==0:
        break
    else:

        print("%d needs %d steps, %d needs %d steps, they meet at %d", %(n, coll(n), m, coll(m), t))