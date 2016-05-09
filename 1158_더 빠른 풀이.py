n, m = map(int, raw_input().split())
s, i, j = range(1, n+1), 0, []
while s:
    i = (i + m - 1) % len(s)
    j += [s.pop(i)]
# print str(j)[:]
# print str(j)[1:-1]
print'<' + str(j)[1:-1] + '>'