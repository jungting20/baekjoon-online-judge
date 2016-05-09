ans = 0
ls = []
for i in range(5):
    a = int(raw_input())
    ls.append(a)
    ans += a
ls.sort()
print ans/5
print ls[2]