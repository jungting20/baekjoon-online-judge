n, m = map(int, raw_input().split())
A = []
for i in xrange(n):
    A.append(map(int, raw_input().split()))
# A = [map(int, raw_input().split()) for i in range(n)]

m, k = map(int, raw_input().split())
B = []
for i in xrange(m):
    B.append(map(int, raw_input().split()))
# B = [map(int, raw_input().split()) for j in range(m)]

for i in xrange(n):
    for j in xrange(k):
        cnt = 0
        for x in xrange(m):
            cnt += A[i][x] * B[x][j]
        print cnt,
    print
# c = [[sum(a[i][j]*b[j][k] for j in range(m)) for k in range(l)] for i in range(n)]
# for i in range(n):
#     print' '.join(str(x) for x in c[i])