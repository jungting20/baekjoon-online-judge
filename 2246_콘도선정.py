n = int(raw_input())
cnt = 0
m = 30000
for i in xrange(n):
    d, c = map(int, raw_input().split())
    if d+c < m:
        m = d+c
        cnt = 1
    elif d+c == m:
        cnt += 1
    else:
        pass
print cnt