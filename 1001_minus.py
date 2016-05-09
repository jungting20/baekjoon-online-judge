# a=int(raw_input())
# b=int(raw_input())
#
# print(a-b)

import sys
r = lambda: sys.stdin.readline()

a, b = map(int, r().split())
print(a-b)