from __future__ import print_function
import sys
r = lambda: sys.stdin.readline()

n = int(r())
x = map(int, r().split())
m = int(r())
y = map(int, r().split())

for i in xrange(m):
    if y[i] in x:
        print ("1", end=" ")
    else:
        print ("0", end=" ")
