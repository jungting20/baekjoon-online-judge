import math
f = math.factorial; a, b = map(int, raw_input().split()); print f(a)/f(b)/f(a-b)
