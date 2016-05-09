n = int(raw_input())
for i in xrange(n):
    angel = map(int, raw_input().split())
    devil = map(int, raw_input().split())
    a = 0
    d = 0
    al = [1, 2, 3, 3, 4, 10]
    dl = [1, 2, 2, 2, 3, 5, 10]
    for j in range(6):
        a += angel[j]*al[j]
    for k in range(7):
        d += devil[k]*dl[k]
    if a > d:
        print "Battle %d: Good triumphs over Evil" % (i+1)
    elif a < d:
        print "Battle %d: Evil eradicates all trace of Good" % (i+1)
    else:
        print "Battle %d: No victor on this battle field" % (i+1)