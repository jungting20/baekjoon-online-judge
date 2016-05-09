n = int(raw_input())
r = map(int, raw_input().split())
b = list(set(r))
b.sort()
x = ""
for i in range(len(b)):
    x += "{}".format(str(b[i]))
    x += " "
print x