r = raw_input()
c = [1, 0, 0]
for i in r:
    n = ord(i)-65
    c[n], c[n-2] = c[n-2], c[n]
print(c.index(1)+1)