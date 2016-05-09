n = map(int, raw_input().split())

def gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        temp = a
        a = b
        b = temp % b

    return a
print gcd(n[0], n[1])
print n[0] * n[1] / gcd(n[0], n[1])