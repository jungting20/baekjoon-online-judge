a=[]
for i in range(int(raw_input())):
    n = int(raw_input())
    if n == 0:
        del a[-1]
    else:
        a.append(n)
print sum(a)