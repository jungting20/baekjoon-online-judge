n = int(raw_input())
ls = map(int, raw_input().split())

def longest_increasing_subsequence(d):
    # Return one of the L.I.S. of list d
    l = []
    for i in range(len(d)):
        l.append(max([l[j] for j in range(i) if l[j][-1] < d[i]] or [[]] , key=len) + [d[i]])
    return max(l, key=len)
a={}
for i in range(n):
    a[ls[i]] = i+1
b = list(a.values())

print len(longest_increasing_subsequence(b))