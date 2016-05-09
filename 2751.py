import sys
l = []
for _ in range(input()):
    l.append(int(sys.stdin.readline()))
l.sort()
for i in range(len(l)):
    print l[i]