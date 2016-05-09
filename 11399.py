n = int(raw_input())
l = map(int, raw_input().split())
l.sort()
ans = 0
for i in range(n):
    ans += l[i] * (n-i)
print ans