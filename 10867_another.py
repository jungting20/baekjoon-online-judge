from __future__ import print_function
a = input()
data = map(int, raw_input().split())
b = {}
for i in data:
    b.setdefault(i, 0)
    '''
    setdefault(key[, default])
    If key is in the dictionary, return its value.
    If not, insert key with a value of default and return default.
    default defaults to None.
    '''
c = []
for k in b.keys():
    c.append(k)
c.sort()
for i in c:
    print (i, end=' ')