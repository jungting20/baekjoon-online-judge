from __future__ import print_function
ans = 0
m = 0
n = 0
for i in range(9):
    a = raw_input().split()
    if ans <= max(a):
        ans = max(a)
        m = i+1
        n = a.index(max(a))+1
print(ans)
print(m, end=" ")
print(n, end=" ")