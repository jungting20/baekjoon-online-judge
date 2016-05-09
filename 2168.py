def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return abs(a)

x, y = [int(i) for i in raw_input().split()]
crossed = x + y - gcd(x, y)
print (crossed)