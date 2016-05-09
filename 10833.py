n = int(raw_input())
ans = 0
for i in range(n):
    x, y = map(int, raw_input().split())
    ans += y % x
print ans