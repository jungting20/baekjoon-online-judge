def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

for i in range(int(raw_input())):
    a, b = map(int, raw_input().split())
    while a != 1:
        x = b/a
        if b % a != 0:
            x += 1
        a = a*x-b
        b = b*x
        g = gcd(a, b)
        a /= g
        b /= g
    print b