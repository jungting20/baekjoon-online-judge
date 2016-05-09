n = int(raw_input())
ls = [map(int, raw_input().split()) for i in range(n)]
def gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        temp = a
        a = b
        b = temp % b

    return a

for i in range(n):
    print ls[i][0] * ls[i][1] / gcd(ls[i][0], ls[i][1])