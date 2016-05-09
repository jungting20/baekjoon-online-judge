n = int(raw_input())
ls = map(int, raw_input().split())
ls.sort()
if len(ls) % 2 == 0:
    ans = ls[0] * ls[-1]
else:
    ans = ls[len(ls)/2]**2
print ans
