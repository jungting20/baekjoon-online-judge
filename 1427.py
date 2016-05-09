from __future__ import print_function
a = raw_input()
l = []
for i in range(len(a)):
    l.append(a[i])
l.sort()
l.reverse()
for i in range(len(a)):
    print(l[i], end="")