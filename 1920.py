def binSrch(a, begin, end, target):
    if begin > end:
        return 0

    mid = (end + begin) / 2

    if a[mid] == target:
        return 1
    elif target < a[mid]:
        return binSrch(a, begin, mid-1, target)
    else:
        return binSrch(a, mid+1, end, target)

raw_input()
a = map(int, raw_input().split())
raw_input()
b = map(int, raw_input().split())

a.sort()

for i in range(len(b)):
    print binSrch(a, 0, len(a)-1, b[i])



