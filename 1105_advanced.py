a, b = map(int, raw_input().split())
i = 10**10
r = 0
while i:
    if a / i % 10 != b / i % 10:
        break
    if a / i % 10 == 8:
        r += 1
    i /= 10
print r