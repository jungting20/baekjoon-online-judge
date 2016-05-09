n = int(raw_input())
r = [map(int, raw_input()) for i in range(n)]
for i in range(n):
    if r[i][len(r[i])-1] % 2 == 0:
        print "even"
    else:
        print "odd"