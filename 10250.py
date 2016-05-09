for i in xrange(int(raw_input())):
    h, w, n = map(int, raw_input().split())
    n -= 1
    print("%d%02d" % (n % h+1, n/h+1))