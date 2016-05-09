n, m = [int(x) for x in raw_input().split()]
def exp5(a):
    cnt = 0
    while a >= 5:
        cnt += a/5
        a /= 5
    return cnt
def exp2(a):
    xcnt = 0
    while a >= 2:
        xcnt += a / 2
        a /= 2
    return xcnt
print min(exp5(n) - exp5(m) - exp5(n-m), exp2(n) - exp2(m) - exp2(n-m))

# n, m = map(int, raw_input().split())
# p, q=0, 0
# for i in range(30):
#     r = 2**(i+1)
#     s = 5**(i+1)
#     p += n/r - m/r - (n-m)/r
#     q += n/s - m/s - (n-m)/s
# print q if p>q else p