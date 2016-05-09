n = int(raw_input())
d = [1]
for i in xrange(1, n+1):
    if i & 1:
        d.append(d[i-1])
    else:
        d.append((d[i-1] + d[i>>1]) % 1000000000)
print d[n]