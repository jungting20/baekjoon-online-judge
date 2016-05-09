n = int(raw_input())
c = 987654321
def cnt(a, s):
    global c
    if a != 1:
        if a % 2 == 0:
            cnt(a / 2, s + 1)
        if a % 3 == 0:
            cnt(a/3, s+1)
        else:
            cnt(a-1, s+1)
    else:
        if c > s:
            c = s
cnt(n, 0)
print c