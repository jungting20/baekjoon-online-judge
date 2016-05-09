from __future__ import print_function

n = int(raw_input())
r = [map(str, raw_input()) for i in range(n)]

for i in range(n):
    for j in range(len(r[i])):
        if j==0:
            print(r[i][j].upper(), end='')
        else:
            print(r[i][j], end='')
    print()