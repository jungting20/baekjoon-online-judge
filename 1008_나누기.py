from __future__ import division

import sys
r = lambda: sys.stdin.readline()

a, b = map(int, r().split())
print("{0:.11f}".format(a/b))