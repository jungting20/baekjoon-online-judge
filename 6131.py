n = int(raw_input())
ans = 0
for b in range(1, 501):
    for a in range(b, 501):
       if a**2 - b**2 == n:
           ans += 1
print ans