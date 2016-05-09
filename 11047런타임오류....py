import sys
a = map(int, raw_input().split())
n = a[0]
k = a[1]
l = []
for _ in range(n):
    l.append(int(sys.stdin.readline()))

cnt = 0
while k != 0:
    i = 0
    while k - l[i] > 0:
        i += 1
    if k - l[i] < 0:
        i -= 1

    j = 2
    while k - j * l[i] > 0:
        j += 1
    if k - j * l[i] < 0:
        j -= 1

    k -= j * l[i]
    cnt += j

print cnt