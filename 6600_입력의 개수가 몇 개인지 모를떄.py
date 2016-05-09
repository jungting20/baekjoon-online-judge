import math

while True:
    try:
        n = map(float, raw_input().split())
        abc = math.sqrt((n[0] - n[2]) ** 2 + (n[1] - n[3]) ** 2) * math.sqrt(
            (n[2] - n[4]) ** 2 + (n[3] - n[5]) ** 2) * math.sqrt((n[0] - n[4]) ** 2 + (n[1] - n[5]) ** 2)
        s = 0.5 * math.fabs((n[0] * n[3] + n[2] * n[5] + n[4] * n[1]) - (n[2] * n[1] + n[4] * n[3] + n[5] * n[0]))
        r = abc / (4.0 * s)
        print "%.2f" % (2.0 * 3.141592654589793 * r)
    except EOFError:
        break