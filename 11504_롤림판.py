n = int(raw_input())
x = map(int, raw_input().split())
print x
a = 0
b = 0

lst = [map(int, raw_input().split()) for i in range(2)]
print lst

for i in range(x[1]):
    d = lst[0][i]
    e = lst[1][i]
    a = a * 10 + d
    b = b * 10 + e
print a, b

con = map(int, raw_input().split())
print con

ans = 0
