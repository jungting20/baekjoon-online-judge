from __future__ import print_function
import sys
r = lambda: sys.stdin.readline()

n = int(r())
x = map(int, r().split())
x.sort()
m = int(r())
y = map(int, r().split())

def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[midpoint+1:], item)

for i in xrange(m):
    print (int(binarySearch(x, y[i])), end=" ")
